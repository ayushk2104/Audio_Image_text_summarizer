import speech_recognition as sr

def get_text_from_audio(file_path):
    r = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
        except:
            text = "Unable to recognize audio." + "\n" + "Please try again."
    return text