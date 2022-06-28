/* NAV */
const activePage = window.location.pathname;
const navLinks = document.querySelectorAll('nav a').forEach(link => {
    if (link.href.includes(`${activePage}`)) {
        link.classList.add('active');
        console.log(link);
    }
})


/* Typing Effect */
var i = 0;
var txt = 'This is the best office website you will ever visit, Welcome !! ;)';
var speed = 50;

function typeWriter() {
    if (i < txt.length) {
        document.getElementById("demo").innerHTML += txt.charAt(i);
        i++;
        setTimeout(typeWriter, speed);
    }
}

/*FAQ*/

var acc = document.getElementsByClassName("questions");
var i;

for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function () {
        /* Toggle between adding and removing the "active" class,
        to highlight the button that controls the panel */
        this.classList.toggle("active");

        /* Toggle between hiding and showing the active panel */
        var panel = this.nextElementSibling;
        if (panel.style.display === "block") {
            panel.style.display = "none";
        } else {
            panel.style.display = "block";
        }
    });
}
var acc = document.getElementsByClassName("questions");
var i;

for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function () {
        this.classList.toggle("active");
        var panel = this.nextElementSibling;
        if (panel.style.maxHeight) {
            panel.style.maxHeight = null;
        } else {
            panel.style.maxHeight = panel.scrollHeight + "px";
        }
    });
}

function myFunction() {
    document.querySelector('#front')?.addEventListener('submit', (e) => {
        e.preventDefault()
        const id = e.target.id.value
        fetch('https://reqres.in/api/users/' + id).then(
            results => results.json())
            .then(json => {
                const image = document.getElementById("image")
                const email = document.getElementById("email")
                image.classList.remove('invisible')
                email.classList.remove('invisible')
                image.src = json.data.avatar
                email.innerHTML = 'email: ' + json.data.email
            })
            .catch((e) => {
            })
    })
}

const getUser = () => {
    const formInputValue = document.getElementById("frontend-request").user_number.value;
    fetch(` https://reqres.in/api/users/${formInputValue}`)
        .then((response) => response.json())
        .then((object) => {
            const data = object?.data;
            document.getElementById("place_holder_for_response").innerHTML =
                `
                    <br>
                    <h3>${data?.first_name} ${data?.lastname}</h3>
                    <h4>${data?.email}</h4>
                    <img src="${data?.avatar}" alt="Profile Picture"/>
                `
        })
        .catch((err) => console.log(err));
}