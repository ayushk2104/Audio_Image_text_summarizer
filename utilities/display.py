from utilities.process_text import text_summarizer
from utilities.process_text import reading_time
from utilities.get_audio_of_text import get_audio_from_text

def display_text(text):
    text_stat = text_summarizer(text)
    print("Here's the summary \n")
    print(text_stat[2])
    print("\nThe length of the summary is " + str(text_stat[3]))
    print("\nReading time of the summary is " + reading_time(text_stat[2]))
    print("The following is the audio of the same")
    get_audio_from_text(text_stat[2])