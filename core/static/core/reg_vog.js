document.getElementById('item_').addEventListener('click', function() {
    window.location.href = '/';
});
 
document.getElementById('press-1').addEventListener("click", addPage);
document.getElementById('press-2').addEventListener("click", deletePage);
const container = document.getElementById('add-container_2');
let removeBtn = document.getElementById('press-2');
var count = 1;
function addPage() {
    count++;
    container.innerHTML += `
    <div class="leader">
            <div class="leader-text">
                <div class="finally"><div class="hax">Members ${count} Details
                </div></div>
                <p class="txt-2 padding">All feilds marked with&nbsp;<a>*</a>&nbsp;are mandatory</p>
            </div>
    </div>   
    <div class="form-container">         
    <div action="" class="form-box-1 mem">
    <div>
        <p>Name&nbsp;<a>*</a></p><input class="input-box" type="text" name="name">
    </div>
    <div class="align-right">
        <p>Gender&nbsp;<a>*</a></p>
        <select name="gender" id="select" class="input-box">
                    <option value="m">Male</option>
                    <option value="f">Female</option>
                    <option value="o">Others</option>
                </select>
                <img class="img-set" src="{% static "core/Vector 6.png" %}" alt="">
    </div>
    <div>
        <p>Contact Number&nbsp;<a>*</a></p><input id="phone-${count}" class="input-box phone1" type="tel" name="Phone_Number">
    </div>
    <div class="align-right">
        <p>Email ID&nbsp;<a>*</a></p><input class="input-box" type="email" name="Email">
    </div>
    <div>
        <p>Role&nbsp;<a>*</a></p>
        <select  id="select" class="input-box" name="role">
            {% for role in roles %}
            <option value="{{ role.id }}">{{ role.name_of_role}}</option>
            {% endfor %}
        </select>
        <img class="img-set-2" src="{% static "core/Vector 6.png" %}" alt="">
    </div>
</div>
</div>
</div>`;

    if (count == 2) {
        removeBtn.style.display = "inline-block";
    }

    const input = document.querySelector(`#phone-${count}`);
    window.intlTelInput(input, {
      utilsScript: "https://cdn.jsdelivr.net/npm/intl-tel-input@18.2.1/build/js/utils.js",
      initialCountry: "in",
      separateDialCode: true,
    });
}

function deletePage() {
    count--;
    let elm = container.lastElementChild;
    let elm2 = container.lastElementChild.previousElementSibling;
    container.removeChild(elm);
    container.removeChild(elm2);

    if (count == 1) {
        removeBtn.style.display = "none";
    }
}

const linkPage = window.location.pathname;
const com1 = document.getElementById("com1");
const com2 = document.getElementById("com2");
const com3 = document.getElementById("com3");

function addClassOnClick(element1, element2, element3) {
    element1.classList.add("comm");
    element2.classList.remove("comm");
    element3.classList.remove("comm");

};
if (linkPage == com1.firstElementChild.pathname) {
addClassOnClick(com1, com2, com3);
}
if (linkPage == com2.firstElementChild.pathname) {
    addClassOnClick(com2, com1, com3);
}
if (linkPage== com3.firstElementChild.pathname) {
    addClassOnClick(com3, com1, com2);
}
const popup = document.querySelectorAll('.black')[0]
popup.addEventListener("click", function(){
    popup.style.display="none";
});

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