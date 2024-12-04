# from openai_unofficial import OpenAIUnofficial

# client = OpenAIUnofficial()
# audio_data = client.audio.create(
#     input_text="This is a test of the TTS capabilities!",
#     model="tts-1-hd",
#     voice="nova"
# )
# with open("tts_output.mp3", "wb") as f:
#     f.write(audio_data)
# print("TTS Audio saved as tts_output.mp3")

import requests

def download_audio_speech():
    url = "https://openai-devsdocode.up.railway.app"
    payload = {
        "model": "tts-1-hd-1106",
        "voice": "nova",
        "input": "I love you & I can't wait to spend time together!"
    }
    response = requests.post(url, json=payload, stream=True)
    with open("speech.mp3", "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    print("Audio saved as speech.mp3")

# download_audio_speech()