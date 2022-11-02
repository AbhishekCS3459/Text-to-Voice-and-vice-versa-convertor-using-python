from email.mime import audio
import speech_recognition
import pyttsx3
def SpeakText(command):
	
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()

recogniser= speech_recognition.Recognizer() # this will recognise the speech into recogniser
with speech_recognition.Microphone() as source: # this is opening the microphone 
    print("say something: ")
    audio=recogniser.listen(source) # this line listen form my pc microphone and stores to the vairable called audio

#print("You said:")
#this line sends audio file to google and return the text what it got from google
#print(recogniser.recognize_google(audio))

if "hello " in audio:
    text="Hi"
    SpeakText(text)
elif "how are you" in audio:
    SpeakText("I am well,thanks")
else:
    SpeakText("Huh?")
    