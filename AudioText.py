from utilities.audio_to_text import get_text_from_audio
from utilities.display import display_text

text = get_text_from_audio("male.wav")
display_text(text)