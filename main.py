import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(c):
    if "open google" in c.lower():
        webbrowser.open("http://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("http://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("http://facebook.com")
    else:
        print("Error to process command]")


if __name__ == "__main__" :
    speak("Initializing Google......")
    while True:
    #  listen for the wake word jarvis 
        # obtain audio from microphone
        r = sr.Recognizer()
        
        print("recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout = 2, phrase_time_limit = 1)
            word = r.recognize_google(audio)
            if(word.lower() == "google"):
                speak("yes sir")
                # listen for word
                with sr.Microphone() as source:
                    print("google active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    process_command(command)

        except Exception as e:
            print("Error; {0}".format(e))