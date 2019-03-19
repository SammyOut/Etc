const clockContainer = document.querySelector(".js-clock");
const clockTitle = clockContainer.querySelector("h1");


function setClockTime(){
    const date = new Date();
    const hours = date.getHours();
    const minutes = date.getMinutes();
    const seconds = date.getSeconds();
    clockTitle.innerText = `${
        hours < 10 ? `0${hours}` : hours
    }:${
        minutes < 10 ? `0${minutes}` : minutes
    }:${
        seconds < 10 ? `0${seconds}` : seconds
    }`;
}

function init(){
    setInterval(setClockTime, 1000);
}

init()