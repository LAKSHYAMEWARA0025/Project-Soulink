let hide_img = document.querySelector(".hide");
let anchor = document.querySelector(".tags a");
let input_boxs = document.querySelectorAll(".input.wrapper");
let hidden = true;

hide_img.addEventListener("click", () => {
    if (hidden) {
        hidden = false;
        hide_img.src = "/static/images/login page/unhide.png";
    }
    else {
        hidden = true;
        hide_img.src = "/static/images/login page/hide.png";
    }
});

anchor.addEventListener("click", () => {
    
    input_boxs[0].style.transform = "translateY(0%)";
    input_boxs[1].style.transform = "translateX(0%)";
    input_boxs[2].style.transform = "translateY(0%)";
    input_boxs[1].style.opacity = "1";
})


// input_boxs[0].style.transform = "translateY(5%)";
// input_boxs[1].style.opacity = "0";
// input_boxs[1].style.transform = "translateX(150%)";
// input_boxs[2].style.transform = "translateY(-50%)";