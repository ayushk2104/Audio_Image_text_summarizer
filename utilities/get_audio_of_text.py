from gtts import gTTS
import os

def get_audio_from_text(text):
    audio = gTTS(text=text, lang="en")
    
    audio.save("Audio_Generated.mp3") 
        
    # Playing the converted file 
    os.system("Audio_Generated.mp3")
