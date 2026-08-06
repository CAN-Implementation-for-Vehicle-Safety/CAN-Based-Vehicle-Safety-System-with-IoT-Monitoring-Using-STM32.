setInterval(function(){

    const d = new Date();

    const time =
        d.toLocaleDateString() +
        " " +
        d.toLocaleTimeString();

    const clock = document.getElementById("clock");

    if(clock){
        clock.innerHTML = time;
    }

},1000);
