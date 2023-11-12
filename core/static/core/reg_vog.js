document.getElementById('press-1').addEventListener("click", addPage);
document.getElementById('press-2').addEventListener("click", deletePage);
const container = document.getElementById('add-container');
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
    <form action="" class="form-box mem">
    <div>
        <p>Name&nbsp;<a>*</a></p><input class="input-box" type="text" name="name">
    </div>
    <div class="align-right">
        <p>Gender&nbsp;<a>*</a></p>
        <select name="gender" id="select" class="input-box">
                    <option value="male">Male</option>
                    <option value="female">Female</option>
                    <option value="others">Others</option>
                </select>
                <img class="img-set" src="Vector 6.png" alt="">
    </div>
    <div>
        <p>Contact Number&nbsp;<a>*</a></p><input id="phone-${count}" class="input-box" type="tel" name="phone_number">
    </div>
    <div class="align-right">
        <p>Email ID&nbsp;<a>*</a></p><input class="input-box" type="email" name="email">
    </div>
    <div>
        <p>Role&nbsp;<a>*</a></p>
        <select name="" id="select" class="input-box" name="role">
            {% for role in roles %}
                <option value="{{ role.id }}">{{ role.name_of_role}}</option>
            {% endfor %}
                </select>
                <img  class="img-set-2" src="Vector 6.png" alt="">
    </div>
</form>
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

const activLinks = document.querySelectorAll('.competiton');
const linkPage = window.location.pathname;
activLinks.forEach(link => {
    if (linkPage.href.include(`${linkPage}`)) {
        link.classList.add('active');
    }
})