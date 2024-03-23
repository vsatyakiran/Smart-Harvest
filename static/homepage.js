

var scrolle = document.querySelector(".scroll");
var img_cont = document.querySelector(".img_content");
var head = document.querySelector(".head");
var right = document.querySelector('.fa-chevron-right');
var left = document.querySelector('.fa-chevron-left');
var why = document.querySelector(".why");
// document.querySelector(".learn").addEventListener('click', focus_1());

var index = 0;

var img_arr = ["static/images/Scroll_1.jpg","static/images/Scroll_2.jpg","static/images/Scroll_3.jpg","static/images/Scroll_4.jpg","static/images/Scroll_5.jpg"];
var content_arr = ['Smart Harvest utilizes advanced algorithms and data analytics to analyze various factors such as soil condition, weather patterns, and geographical location. This ensures that farmers receive precise recommendations tailored to their specific agricultural environment, maximizing crop yield and profitability.','By leveraging cutting-edge technology, Smart Harvest empowers farmers to make informed decisions about crop selection. This leads to increased productivity as farmers can choose crops that are most suitable for their land and climate, reducing the risk of crop failure and improving overall efficiency.','Smart Harvest promotes sustainable agriculture by recommending crops that require optimal resources such as water, fertilizers, and pesticides. By aligning crop selection with resource availability and environmental factors, the system helps farmers minimize waste and conserve natural resources, contributing to long-term ecological balance.','Agriculture is inherently vulnerable to various risks, including unpredictable weather patterns, pests, and diseases. Smart Harvest mitigates these risks by offering diversified crop recommendations based on comprehensive data analysis. By spreading the risk across different crops, farmers can safeguard their livelihoods and maintain stability even in the face of adversity.','Smart Harvest empowers farmers with valuable insights and knowledge, enabling them to make informed decisions independently. By providing access to cutting-edge technology and personalized recommendations, the platform strengthens farmers capabilities, fosters innovation, and promotes self-sufficiency in agricultural practices.']
var head_arr = ['Optimized Crop Selection','Enhanced Productivity','Resource Conservation','Risk Mitigation','Empowering Farmers']
left.style.color = "rgb(24, 24, 24)";
left.style.cursor = "default";

function increment()
{ 
    if(index!=4)
    {
        index +=1;
        scrolle.setAttribute("src", img_arr[index]);
        img_cont.innerText = content_arr[index];
        head.innerText = head_arr[index];
        left.style.color = "white";
        left.style.cursor = "pointer";
        
    }
    if(index==4)
    {
        right.style.color = "rgb(24, 24, 24)";
        right.style.cursor = "default";
    }
}

function decrement()
{ 
    if(index!=0)
    {
        index -=1;
        scrolle.setAttribute("src", img_arr[index]);
        img_cont.innerText = content_arr[index];
        head.innerText = head_arr[index];
        right.style.color = "white";
        right.style.cursor = "pointer";
    }
    if(index==0)
    {
        left.style.color = "rgb(24, 24, 24)";
        left.style.cursor = "default";
    }
}


function focus_1()
{
    why.scrollIntoView({behavior: 'smooth'});
    
}
