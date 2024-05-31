import pyttsx3

# Initialize the Speech Engine
engine = pyttsx3.init()

# Set the speech rate
engine.setProperty('rate', 120)

# Specify the voice ID for a male voice (you should replace this with the desired male voice ID)
male_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'

# Set the voice to the male voice
engine.setProperty('voice', male_voice_id)

# Text to be converted to speech
text = "Hello,, My project is all about to analyze human behaviour and emotion and interact with them. So I have to build a model to understand the human behaviour. I am getting started. Let us see how far I have gone till now! my project has got three major point,, voice assistant, chatbot, behaviour analysis. But behaviour analysis is a vast machine learning approach to be done. I am working on it but till now i have built some functionality of chatbot and voice assistant. lets see what its transpire"

# Convert text to speech
engine.say(text)
engine.runAndWait()
