const labels = document.getElementsByClassName("signup-label");
const forms = document.getElementsByTagName("form");

labels[0].addEventListener("click", function (){
    this.classList.add("active");
    forms[0].classList.remove("hidden");
    labels[1].classList.remove("active");
    forms[1].classList.add("hidden");
});


labels[1].addEventListener("click", function (){
    this.classList.add("active");
    forms[1].classList.remove("hidden");
    labels[0].classList.remove("active");
    forms[0].classList.add("hidden");
})