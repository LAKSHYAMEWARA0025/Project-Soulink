const output = document.getElementById("text");
const mic = document.getElementById("mic");
let transcriptOn = false;

let updateTranscript = function(event) {
    const transcript = event.results[event.results.length - 1][0].transcript;
    output.value = transcript;
}

let resumeTranscription = function() {
    recognition.start();
    console.log("resuming...");
}

let stopTranscription = function() {
    recognition.stop();
}

let clearTranscript = function() {
    output.textContent = "";
}

let startTranscription = function() {
    recognition = new webkitSpeechRecognition() || new SpeechRecognition();
    recognition.lang = "en-IN"; // Set the language for speech recognition
    recognition.continuous = true; // Enable continuous listening
    recognition.interimResults = true; // Strem Output

    recognition.start();
    recognition.onresult = updateTranscript;
    recognition.onend = resumeTranscription;
    // recognition.onend = stopTranscription;
    
}

mic.addEventListener("click", function() {
    console.log(transcriptOn);
    if (!transcriptOn) {
        console.log("working !");
        startTranscription();
        transcriptOn = true;
    }
    else {
        stopTranscription();
        transcriptOn = false;
    }
})