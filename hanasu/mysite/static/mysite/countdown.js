// definie une temps à décompter
let timeSecond = 30;
// defini la balise à selectionner
const timeH = document.querySelector("h1");
displayTime(timeSecond);

const countDown = setInterval(() => {
  timeSecond--;
  displayTime(timeSecond);
  if (timeSecond == 0 || timeSecond < 1) {
    
    // document.getElementById('image').style.display = "block";   
    clearInterval(countDown);
    endCount(); 
    show();
    setTimeout(() => {
      // change l'url mais en lui donnant la même que celle utilisé.
      window.location = window.location.href
      }, 5000)
        
    
  }
}, 1000);

function displayTime(second) {
  const min = Math.floor(second / 60);
  const sec = Math.floor(second % 60);
//   ternaire : si minute < 10 alors = 0 sinon egale à null
  timeH.innerHTML = `  ${min < 10 ? "0" : ""}${min}:${sec < 10 ? "0" : ""}${sec}`
}

function endCount() {
  timeH.innerHTML = "Time out";
}

function show() {
 
    /* change le style de l'image à block*/
    document.getElementById('image')
            .style.display = "block";




}