from asyncio import run
from edge_tts import Communicate
from os import remove
from os.path import exists


class TTS:
    def __init__(self, voice: str = 'ta-IN-PallaviNeural'):
        self.__voice: str = voice
        self.__voices: list[str] = ['hi-IN-SwaraNeural',
                    'hi-IN-MadhurNeural',
                    'ta-IN-PallaviNeural',
                    'te-IN-ShrutiNeural',
                    'en-IN-NeerjaNeural',
                    'ta-MY-KaniNeural',
                    'en-GB-LibbyNeural']
        self.__path: str = "static/audios/voice.mp3"
        self.__speech_rate: int = 1
    
    def remove_special_chars(self, text) -> str:
        allowed_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 :,.?!"
        newtxt=""
        for i in text:
            if i in allowed_characters:
                newtxt+=i
        return newtxt
    
    async def amain(self, text: str) -> None:
        """Main function"""

        if exists(self.__path):
            remove(self.__path)

        communicate = Communicate(text,self.__voice, rate= f'+{self.__speech_rate}%')
        await communicate.save(self.__path)
    
    def generate_audio(self, text: str) -> None:

        text = self.remove_special_chars(text)
        try:
            run(self.amain(text))
        except Exception as e:
            print(f"Error: {e}")
    
    def change_voice(self, voiceId: int) -> None:
        """
        Available voices:
        0: Swara - Hindi
        1: Madhur - Hindi
        2: Pallavi - Tamil + Hindi + English
        3: Shruti - Telugu + Hindi + English
        """
        self.__voice = self.__voices[voiceId]

    def change_speech_rate(self, speech_rate: int) -> None:
        self.__speech_rate = speech_rate
    


if __name__ == "__main__":
    tts = TTS('ta-IN-PallaviNeural')
    tts.generate_audio("So what? Don't worry I am here to listen you.") 