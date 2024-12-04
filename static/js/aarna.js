const textarea = document.getElementById("text");
const clear = document.getElementById("clear");
const chatbox = document.querySelector(".container.ai");

let prev_prompt = "";
let aarna_chat = null;
let scroll_height = textarea.scrollHeight;


let notify = function () {

  // Create a new AudioContext
  const audioContext = new AudioContext();

  // Create a new AudioBufferSourceNode
  const source = audioContext.createBufferSource();

  // Load the audio file
  fetch("/static/audios/pop notification2.mp3")
    .then((response) => response.arrayBuffer())
    .then((arrayBuffer) => audioContext.decodeAudioData(arrayBuffer))
    .then((audioBuffer) => {
      // Set the audio buffer
      source.buffer = audioBuffer;

      // Connect the source to the destination
      source.connect(audioContext.destination);

      // Start playing the audio
      source.start();
    });
};

let play_audio = function() {
  // Create a new AudioContext
  const audioContext = new AudioContext();

  // Create a new AudioBufferSourceNode
  const source = audioContext.createBufferSource();

  // Load the audio file
  try{
    fetch("/static/audios/voice.mp3")
    .then((response) => response.arrayBuffer())
    .then((arrayBuffer) => audioContext.decodeAudioData(arrayBuffer))
    .then((audioBuffer) => {
      // Set the audio buffer
      source.buffer = audioBuffer;

      // Connect the source to the destination
      source.connect(audioContext.destination);

      // Start playing the audio
      source.start();
    });
  }
  catch(error) {
    console.log("Error playing voice !")
  }
  
}

let create_userResponse = function(user_prompt) {
    let responseBox = document.createElement("div");
    responseBox.innerHTML = `<img src="/static/images/user.png" alt="user.png" class = "userIcon">
                            <div class = "chatLabel">
                                ${user_prompt}
                            </div>`;
    responseBox.classList.add("responseBox", "User");
    chatbox.appendChild(responseBox);
    responseBox.scrollIntoView({ behavior: "smooth" });
    responseBox.querySelector(".chatLabel").classList.add("anime");

    setTimeout(() => {
        responseBox.querySelector(".chatLabel").classList.remove("anime");
    }, 750);
}

let create_aarnaResponse = function() {
    let responseBox = document.createElement("div");
    responseBox.innerHTML = `<img src="/static/images/aarna2_crop.jpeg" alt="aarna.png" class = "aarnaIcon">
                            <div class = "chatLabel">
                                typing...
                            </div>`;
    responseBox.classList.add("responseBox", "Aarna");
    chatbox.appendChild(responseBox);
    responseBox.scrollIntoView({ behavior: "smooth" });
    responseBox.querySelector(".chatLabel").classList.add("anime");

    setTimeout(() => {
        responseBox.querySelector(".chatLabel").classList.remove("anime");
    }, 750);

    aarna_chat = responseBox.querySelector(".chatLabel");
}

let update_response = async function(server_response) {
    let counter = 0;
    while (aarna_chat === null) {
        await new Promise(resolve => setTimeout(resolve, 100));
        counter += .1;
    }

    if (counter < 3){
        counter = 0;
        while (counter < 3) {
          await new Promise((resolve) => setTimeout(resolve, 1000));
          counter++;
          // console.log(counter);
        }
    }    

    notify();
    console.log(`Voice Output Status: ${server_response.voice_output}`);
    if (server_response.voice_output) {
      play_audio();
    }
    aarna_chat.innerHTML = server_response.bot_reply;
    aarna_chat = null;
}

let sendRequest = function() {
    let user_prompt = textarea.value.trim();
    if (user_prompt === "" || user_prompt === prev_prompt) {
        return;
    }

    create_userResponse(user_prompt);
    setTimeout(create_aarnaResponse, 3000);

    const user_data = {
        user_prompt: user_prompt,
    };
    let status_code = 0;

    // Send Data to server
    fetch("bot-api", {
        method: "POST",
        headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
        },
        body: JSON.stringify(user_data),
    })

    // Recieve Data from server
    .then((response) => {
      status_code = response.status;
      console.log(response.status);
      return response.json();
    })
    .then((data) => {
      console.log("Success:", data.message);
      if (status_code !== 404) {
        update_response(data);
      }
    })
    .catch((error) => {
            console.error("Error:", error);
    });

    // let aarna_response = "Hello, I'm Aarna. How may I help you today?";
    // setTimeout(update_response, 6000, aarna_response);

    prev_prompt = user_prompt;
}


textarea.addEventListener("input", function () {
  if (this.scrollHeight > scroll_height && +this.getAttribute("rows") < 4) {
    this.setAttribute("rows", `${+this.getAttribute("rows") + 1}`);
    scroll_height = this.scrollHeight;
  }
  else if (this.value === "") {
    this.setAttribute("rows", "1");
    scroll_height = this.scrollHeight;
  }
});

clear.addEventListener("click", function () {
  textarea.value = "";
  textarea.setAttribute("rows", "1");
  scroll_height = textarea.scrollHeight;
});

window.addEventListener("keypress", function (e) {
  if (e.key === "Enter") {
    e.preventDefault();
    sendRequest();
  }
});