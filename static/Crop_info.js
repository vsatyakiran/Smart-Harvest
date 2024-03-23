

var myVariable = localStorage.getItem('myVariable');
console.log(myVariable); // Outputs: Hello





var imi = document.querySelector("img");
var head = document.querySelector(".head");
var duration_h = document.querySelector(".dur_p");
var rain_h = document.querySelector(".rainfall");
var temp_h = document.querySelector(".temp");
var humid_h = document.querySelector(".humid");

var nitro_h = document.querySelector(".nitro");
var pho = document.querySelector(".pho");
var po = document.querySelector(".po");
var Ph = document.querySelector(".ph");
var culti = document.querySelector(".cultiv");

function execute(index)
{
    fetch('static/allcrop.json')
    .then(response => response.json())
    .then(data => {
        const jsonData = data;
        var crops = Object.keys(jsonData);
        console.log(crops);

        var duration = jsonData[crops[index]]['Duration'];

        var environment = jsonData[crops[index]]['Environment'];
        var rainfall = environment['Rainfall'];
        var temperature = environment['Temperatue'];
        var humidity = environment["Humidity"];

        var soil = jsonData[crops[index]]["Soil"];
        var nitrogen = soil["Nitrogen"];
        var phosphorous = soil["Phoshorous"];
        var potassium = soil["Potassiun"];
        var ph = soil["ph"];

       
        
        var cultivate = jsonData[crops[index]]["Cultivate"];
        var cul_keys = Object.keys(cultivate);
        console.log(cul_keys[0]);

        for (var i = 0; i < cul_keys.length; i++) 
        {
            var class1 = "x"+ i.toString();
            var key = cul_keys[i];
            console.log(key);
            culti.innerHTML = culti.innerHTML + `<div><h3>${key}</h3><p class="${class1}"></p></div>`;
            
            // console.log(cultivate[key]);
            document.querySelector("."+class1).innerText = cultivate[key];
        }

        var images = ["static/images/apple_1.jpg", "static/images/banana.jpeg", "static/images/black_gram.jpg","static/images/chickpeas.jpg", "static/images/coconut.jpg", "static/images/coffee.jpg", "static/images/cotton.jpg","static/images/grapes.jpg", "static/images/jute.jpg", "static/images/kidneybeans.jpg", "static/images/lentil.jpg", "static/images/maize.jpg", "static/images/mango.jpg", "static/images/mothbeans.jpg", "static/images/mungbeans.jpg", "static/images/muskmelon.jpg", "static/images/orange1.jpg", "static/images/papaya.jpeg", "static/images/pigeonpeas.jpg","static/images/pomegranate.jpg","static/images/rice.jpg", "static/images/watermelon.jpg"]
        imi.setAttribute("src",images[index])
        
       
        head.innerText = crops[index];
        duration_h.innerText = duration;
        rain_h.innerText = rainfall;
        temp_h.innerText = temperature;
        humid_h.innerText = humidity;
        nitro_h.innerText = nitrogen;
        pho.innerText = phosphorous;
        po.innerText = potassium;
        Ph.innerText = ph;





        
    })
    .catch(error => console.error('Error fetching JSON:', error));
}




execute(myVariable)

