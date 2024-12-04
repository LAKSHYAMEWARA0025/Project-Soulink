from os import remove
import edge_tts
import asyncio

voices = ['hi-IN-SwaraNeural',
        'hi-IN-MadhurNeural',
        'ta-IN-PallaviNeural',
        'te-IN-ShrutiNeural']

text = "hi, this is a test"

communicate = edge_tts.Communicate(text,voices[2], rate='+16%')

async def save_audio():
    await communicate.save("mods/test.mp3")

asyncio.run(save_audio())