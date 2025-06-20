import pyttsx3

engine = pyttsx3.init()

text = input("enter text:")

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

engine.say(text)

engine.runAndWait()
