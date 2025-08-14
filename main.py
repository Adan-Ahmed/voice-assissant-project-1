import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary

# recoginze use to take speech recognizing functionality
recognizer = sr.Recognizer() 

# initialize the pyttsx
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcomand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open lindin" in c.lower():
        webbrowser.open("https://lindin.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    else:
        print("error")

if __name__ == "__main__":
    speak("Initializing google....")

    while True:
        # Listen for the wake word "google"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "google"):
                speak("Yes")
                with sr.Microphone() as source:
                    print("google Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processcomand(command)


        except Exception as e:
            print("Error; {0}".format(e))