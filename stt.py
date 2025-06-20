import speech_recognition as sr

r= sr.Recognizer()

with sr.Microphone() as source:
    print("🎙️ Calibrating... Please wait.")
    r.adjust_for_ambient_noise(source, duration=1)
    print("say something")
    audio =r.listen(source)

try:
    print("you said:"+ r.recognize_google(audio))

except sr.UnknownValueError:
    print("could not understand")
except sr.RequestError:
    print("check your internet") 