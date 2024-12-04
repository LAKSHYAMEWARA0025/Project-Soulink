skip = "inactive";
const output = document.getElementById("output");
const startBtn = document.getElementById("start");
const endBtn = document.getElementById("end");
const clearBtn = document.getElementById("clear");
let recognition;

function startRecognition() {
  startBtn.style.display = "none";
  endBtn.style.display = "block";
  clearBtn.style.display = "block";
  recognition = new webkitSpeechRecognition() || new SpeechRecognition();
  recognition.lang = "en-IN"; // Set the language for speech recognition
  recognition.continuous = true; // Enable continuous listening


  recognition.onresult = function (event) {
    const transcript = event.results[event.results.length - 1][0].transcript;    
    output.textContent = transcript;
  };

  recognition.onend = function () {
    recognition.start(); // Restart the recognition when it stops
    output.innerHTML = "";
  };

  recognition.start();
}

function stopRecognition() {
  recognition.stop();
  // Stop the continuous recognition
  output.innerHTML = "";
}

function clearText() {
  output.innerHTML = "";
}
