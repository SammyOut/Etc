const body = document.querySelector("body");

const IMG_NUMBER = 6;

function handleImgLoad(event){
}

function paintImage(imgNumber){
    const image = new Image();
    image.src = `./images/${imgNumber}.jpg`;
    image.classList.add("bgImage"); 
    body.prepend(image);
}

function genRandom(){
    const number = Math.random() * IMG_NUMBER;
    return Math.floor(number) + 1;
}

function init(){
    const randomNumber = genRandom();
    paintImage(randomNumber)
}

init();