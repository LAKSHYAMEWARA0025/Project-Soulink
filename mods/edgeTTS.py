from pygame import mixer,time
import random
import asyncio
import edge_tts
import sys
import os
from time import sleep


allow="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 :,.?!"

mixer.init()
'''
hi-IN-SwaraNeural
hi-IN-MadhurNeural
ta-IN-PallaviNeural
te-IN-ShrutiNeural
'''
voices = ['hi-IN-SwaraNeural',
        'hi-IN-MadhurNeural',
        'ta-IN-PallaviNeural',
        'te-IN-ShrutiNeural']
'''
,pitch='+5Hz'
'''

def remove_special_chars(text):
    newtxt=""
    for i in text:
        if i in allow:
            newtxt+=i
    return newtxt

def fnsample(r=None):
    return True

async def amain(text) -> None:
    """Main function"""
    file_path = "static/audios/voice.mp3"

    if os.path.exists(file_path):
        os.remove(file_path)
    communicate = edge_tts.Communicate(text,voices[2], rate='+16%')
    await communicate.save(file_path)

def TextToSpeech(Text):
    file_path = "static/audios/voice.mp3"
    def Speak(*args,fn=fnsample,**kwargs):
        r=[str(i) for i in args]
        data=" ".join(r)
        data=remove_special_chars(data)
        while 1:
       
            try:
                asyncio.run(amain(data))
                mixer.init()
                mixer.music.load(file_path)
                mixer.music.play()
                print(f"Vani: {Text}")
                while mixer.music.get_busy():
                        if fn()==False:
                            break
                        time.Clock().tick(10)
                
                
            except Exception as e:
                print(f"Error:{e}")

            finally:
                fn(False)
                mixer.music.stop()
                mixer.quit()
                sleep(3)
                os.remove(file_path)                
                return
            

    Data = str(Text).split(".")
    responses = [
    "The text has been successfully printed on the chat screen, awaiting for your review.",
    "Your requested text has been printed on the chat screen for your convenience, sir.",
    "Sir, the printed text is now visible on the chat screen, please take a look.",
    "The text has been rendered on the chat screen as per your instruction, sir.",
    "You'll find the text printed on the chat screen, ready for your inspection, sir.",
    "The chat screen now displays the printed text, sir, awaiting your feedback.",
    "The printed text is now visible on the chat screen for your perusal, sir.",
    "Sir, the text has been successfully printed on the chat screen for your review.",
    "The chat screen now showcases the printed text, sir, please have a look.",
    "You'll find the result displayed on the chat screen, sir, ready for your assessment."
    ]

    if len(Data)>8:
        if len(Text)>=350:
                Speak(random.choice(responses))

        else:
                Speak(Text)

    else:
        Speak(Text)
    
    

if __name__ == "__main__":
    #print(TextToSpeech("Hi Sita, mai tumhari kaise madad kar sakti hun"))
    # TextToSpeech("Namaste, Myself Vaani. I am an A I assistant, designed to make your digital experience more efficient and enjoyable.\
    #             I can provide information, answer questions, and assist with a variety of tasks by interpreting and understanding voice commands.\
    #             However, I must clarify that I do not have personal experiences or emotions.\
    #             My goal is to provide reliable assistance while ensuring a positive and engaging user experiences.\
    #             How may I assist you today?")
    TextToSpeech("Hi !, how can i help you today ?")

'''नमस्ते पीटर, मैं आपकी कैसे मदद कर सकता हूँ?'''