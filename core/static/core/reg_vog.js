document.forms['reg-form'].onsubmit= function(event){
    let nameInputs = document.querySelectorAll('input');
    for (var i = 0; i < nameInputs.length; i++) {
        if (nameInputs[i].value.trim() === "") {
            document.querySelector(".dis").innerHTML = "Enter All necessary details Properly";
            document.querySelector(".black").style.display = "block";
            event.preventDefault();
            return false;
        }
    }
    var numInputs = document.querySelectorAll('input[type="tel"]');
    for (var i = 0; i < numInputs.length; i++) {
        if (isNaN(numInputs[i].value.trim())) {
            document.querySelector(".dis").innerHTML = "Enter All necessary details Properly";
            document.querySelector(".black").style.display = "block";
            event.preventDefault();
            return false;
        }
    }
}