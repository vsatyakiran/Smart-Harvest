import pandas as pd
import numpy as np
from flask import Flask, url_for, request, render_template, Markup
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle, json
import warnings
import requests

warnings.filterwarnings('ignore')

from fertilizer import fertilizer_dic

with open('Model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('labels.pkl', 'rb') as f:
    labels = pickle.load(f)
with open('StatesSeason.json', 'r') as f:
    common_label = json.load(f)

print(model.classes_)

app = Flask(__name__,static_url_path='/static')

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/choose')
def choose():
    return render_template('Choose.html')

@app.route('/details')
def details():
    return render_template('Details.html')

@app.route('/fertilizer_details')
def fertilizer_details():
    return render_template('Fertilizer_details.html')

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
    return render_template('Crop_data.html', top_gainers = top_gainers,top_loosers=top_loosers )


@app.route('/fertilizers', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        crop_name = str(request.form['crop'])
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorous'])
        K = int(request.form['potassium'])
        # ph = float(request.form['ph'])

        df = pd.read_csv(r"E:\Projects\Smart_Harvest\fertilizer.csv")

        nr = df[df['Crop'] == crop_name]['N'].iloc[0]
        pr = df[df['Crop'] == crop_name]['P'].iloc[0]
        kr = df[df['Crop'] == crop_name]['K'].iloc[0]

        n = nr - N
        p = pr - P
        k = kr - K
        temp = {abs(n): "N", abs(p): "P", abs(k): "K"}
        max_value = temp[max(temp.keys())]
        if max_value == "N":
            if n < 0:
                key = 'NHigh'
            else:
                key = "Nlow"
        elif max_value == "P":
            if p < 0:
                key = 'PHigh'
            else:
                key = "Plow"
        else:
            if k < 0:
                key = 'KHigh'
            else:
                key = "Klow"

        response = Markup(str(fertilizer_dic[key]))
        return render_template('Fertilizer_result.html', response = response)
    return render_template('Fertilizer_details.html')

# Weather
@app.route('/weather', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        print("Entered....")
        zip_code = str(request.form['zip'])
        # state = str(request.form['state'])
        api_key = "56765cc0691fe16b12cf69c42ce61c10"

        headers = {
            "apikey": "90c125c0-e455-11ee-aee3-13a3b378e2b5"}

        params = (
            ("codes", zip_code),
            ("country","in"),
        )

        response = requests.get('https://app.zipcodebase.com/api/v1/search', headers=headers, params=params);

        response = json.loads(response.text)
        results = response['results'][zip_code]
        latitude = results[0]['latitude']
        longitude = results[0]['longitude']

        # using Latitude and Longitude
        resp = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}")


        data = json.loads(resp.text)

        # Extract temperature, humidity, longitude, and latitude
        temperature = round(data['main']['temp']-273.15, 2)
        humidity = data['main']['humidity']
        # longitude = data['coord']['lon']
        # latitude = data['coord']['lat']
        state = "".join(results[0]['state'].lower().split())
        province = results[0]['province']
        print(state)
        print(province)
        print(data['main']['temp']-273.15)
        return render_template('Details.html', temperature = str(temperature), humidity= str(humidity), state=state)
    return render_template('Details.html', temperature = '', humidity= '', state='')

@app.route('/crop_info')
def crop_info():
    return render_template('Crop_info.html')

@app.route("/goback")
def goback():
    return render_template('Choose.html')


if __name__ == '__main__':
    app.run(debug=True)