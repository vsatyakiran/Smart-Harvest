import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle, json
from flask import Flask, render_template, url_for, request
import warnings
warnings.filterwarnings('ignore')

with open('Model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('labels.pkl', 'rb') as f:
    labels = pickle.load(f)
with open('StatesSeason.json', 'r') as f:
    common_label = json.load(f)

# i = np.array([[ 21.9989826 ,  56.31006755,   6.98571967, 136.8274312 ,
#          20.        ,  19.        ,  18.        ,  55.        ,
#          23.        ]])
# r = model.predict_proba(i)
# print(r)
# print(labels.inverse_transform([8]))
# print(common_label)

#Flask
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def prediction():
    temp = float(request.form['temp'])
    humidity = float(request.form['humidity'])
    ph = float(request.form['ph'])
    rainfall = float(request.form['rainfall'])
    season = str(request.form['season'])
    state = str(request.form['state'])
    nitrogen = float(request.form['nitrogen'])
    phosphorous = float(request.form['phosphorous'])
    potassium = float(request.form['potassium'])

    #Encode
    print("Enocde")
    season = common_label[season]
    state  = common_label[state]
    print("Encode")
    query = np.array([temp, humidity, ph, rainfall, season, state, nitrogen, phosphorous, potassium]).reshape(1, -1)
    print(query)
    # Model
    result = model.predict_proba(query)[0]
    # Top 5 loosers
    top_gainers = np.argsort(-result)[:5]
    top_gainers = labels.inverse_transform(top_gainers)
    # Top 5 ganiers
    top_loosers = np.argsort(result)[:5]
    top_loosers = labels.inverse_transform(top_loosers)
    # f"Top Gainers:{top_gainers}<br>Top Loosers:{top_loosers}"
    return render_template('crop_results.html', top_gainers = top_gainers,top_loosers=top_loosers )

if __name__ == "__main__":
    app.run(debug=True)