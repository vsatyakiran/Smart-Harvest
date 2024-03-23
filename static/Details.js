
// window.addEventListener('beforeunload', function (e) {
//     // Clear form 1
//     document.querySelector('#temperature').setAttribute('value','')
//     // Clear form 2
//     document.querySelector('#humidity').setAttribute('value','');
// });


function clear()
{
    FormData.clear
}

function updateInput()
{    
    var selectedCrop = document.getElementById("cropSelect").value;

    console.log(selectedCrop);
}

function moveToNext(event, nextFieldId) {
    if (event.key === 'Enter') { 
        event.preventDefault(); 
        document.getElementById(nextFieldId).focus(); 
    }
}

function hide()
{
    // document.querySelector(".location").style.display = 'none';
}