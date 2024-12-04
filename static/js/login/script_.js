let image = []
let spacing = []


let toggle_psswrd = function (e) {
  if (this.getAttribute("data-visibility") === "hidden") {
    this.src = "/static/images/login page/unhide.png";
    this.setAttribute("data-visibility", "visible");

    document.querySelectorAll(".wrap_field input")[2].type = "text";
  } else {
    this.src = "/static/images/login page/hide.png";
    this.setAttribute("data-visibility", "hidden");

    document.querySelectorAll(".wrap_field input")[2].type = "password";
  }
};

let switch_2_signup = function () {
  cont.style.backgroundImage = image[1];

  input_boxs[1].style.opacity = "1";
  input_boxs[1].style.transform = "translateX(0%)";

  heading.innerHTML = "SIGN UP";
  heading.style.letterSpacing = spacing[0];

  btn.innerHTML = "SIGN UP";
  btn.style.color = "#000000cc";

  tags.querySelector("span").innerHTML = "Already have an account ?";
  tags.querySelector("a").innerHTML = "LOGIN";
  tags.style.opacity = "1";
};

let switch_2_login = function () {
  cont.style.backgroundImage = image[0];

  input_boxs[0].style.transform = "translateY(40%)";
  input_boxs[2].style.transform = "translateY(-40%)";

  heading.innerHTML = "LOGIN";
  heading.style.letterSpacing = spacing[0];

  btn.innerHTML = "LOGIN";
  btn.style.color = "#000000cc";

  tags.querySelector("span").innerHTML = "Don't have an account yet ?";
  tags.querySelector("a").innerHTML = "SIGN UP";
  tags.style.opacity = "1";
};

let toggle_page = function (e) {

  errors.forEach((error) => {
    error.style.display = "none";
    error.innerHTML = "";
  });

  heading.style.letterSpacing = spacing[1];
  btn.style.color = "#e7e7e7";
  tags.style.opacity = "0";

  if (form_type.value === "login") {
    form_type.value = "singup";

    input_boxs[0].style.transform = "translateY(0%)";
    input_boxs[2].style.transform = "translateY(0%)";

    setTimeout(switch_2_signup, 500);
  } else {
    form_type.value = "login";
    input_boxs[1].style.opacity = "0";
    input_boxs[1].style.transform = "translateX(50%)";

    setTimeout(switch_2_login, 500);
  }
};

let live_validation = function (e) {
  if (this.type === "text") {
    if (!this.value.match(regex[0])) {
      this.value = this.value.slice(0, -1);
    }
  } else if (this.type === "password") {
    if (!this.value.match(regex[2])) {
      this.value = this.value.slice(0, -1);
    }
  }
};


let validate = function (e) {
  let input_fields = document.querySelectorAll(".wrap_field input");
  let validation = true;

  input_fields.forEach((field, index) => {

    if (index == 1 && form_type.value === "login") {
        return;
    }

    if (field.value.length < charLength[index]) {
      errors[index].innerHTML = errorMessages[index];
      errors[index].style.display = "block";
      validation = false;
    } else if (!field.value.match(regex[index])) {
      errors[index].innerHTML = errorMessages[index];
      errors[index].style.display = "block";
      validation = false;
    }
    else {
      errors[index].style.display = "none";
      errors[index].innerHTML = "";
    }
  });

  if (!validation) {
    e.preventDefault();
    return; }
  
  if (form_type.value === "login") {   
    input_fields[1].value = "";
  }

  errors.forEach((error) => {
    error.style.display = "none";
    error.innerHTML = "";
  });

  console.log("Validation Successfull");
};


let set_values = function () {
  let win_images = [
    "url('/static/images/login page/background_abstract.png')",
    "url('/static/images/login page/background_fluid.png')",
  ];

  let android_images = [
    "url('/static/images/login page/android_background.png')",
    "url('/static/images/login page/android_background2.png')",
  ];

  let win_spacing = [".5vw", "-1.5vw"];
  let android_spacing = ["2.5vw", "-5.5vw"];

  if (window.innerWidth < 560) {
    image = android_images;
    spacing = android_spacing;
  } else {
    image = win_images;
    spacing = win_spacing;
  }
  

  if (form_type.value === "signup") {
    input_boxs[0].style.transform = "translateY(0%)";
    input_boxs[2].style.transform = "translateY(0%)";
    switch_2_signup();
  }
};


let cont = document.querySelector(".container");
let input_boxs = document.querySelectorAll(".input");
let heading = document.querySelector(".form > h1");
let btn = document.querySelector(".btn");
let tags = document.querySelector(".anchor");
let errors = document.querySelectorAll(".errors");
let form_type = tags.querySelector("input");

window.onload = set_values;

let regex = [
  "^[a-zA-Z0-9_]+$",
  "^[a-z0-9.%]+@[a-z]{2,}\.[a-z]{2,}$", // mail
  "^[a-zA-Z0-9_.@]+$"
];

let errorMessages = [
  "Username too short !",
  "Invalid Mail !",
  "Password too short !",
];

let charLength = [3, 1, 8];

document
  .querySelector(".icons.psswrd")
  .addEventListener("click", toggle_psswrd);
document.querySelector(".anchor a").addEventListener("click", toggle_page);
document
  .querySelectorAll(".wrap_field input")
  .forEach((input) => input.addEventListener("input", live_validation));
btn.addEventListener("click", validate);
