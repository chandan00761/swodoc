const labels = document.getElementsByClassName("signup-label");
let active = labels[0].classList.contains('active') ? labels[0] : labels[1];
const forms = document.getElementsByTagName("form");

labels[0].addEventListener("click", function (){
    if(active !== this) {
        this.classList.add("active");
        forms[0].classList.remove("hidden");
        labels[1].classList.remove("active");
        forms[1].classList.add("hidden");
        active = this;
    }
});


labels[1].addEventListener("click", function (){
    if(active !== this) {
        this.classList.add("active");
        forms[1].classList.remove("hidden");
        labels[0].classList.remove("active");
        forms[0].classList.add("hidden");
        active = this;
    }
})