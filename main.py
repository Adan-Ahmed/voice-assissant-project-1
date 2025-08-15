import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from gtts import gTTS
import pygame
import os
from openai import OpenAI
from dotenv import load_dotenv
import os

# recoginze use to take speech recognizing functionality
recognizer = sr.Recognizer() 

# initialize the pyttsx
engine = pyttsx3.init()

newsapi = "83eec22bb078402d826b380e22637b3d"

load_dotenv()  # loads .env from the current working directory
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY not found. Is your .env in the project root?")
def aiprocess(command):
    client = OpenAI(api_key=api_key)
    resp = client.chat.completions.create(

    model="gpt-5",  # you can change this later
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Google skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
)
    return resp.choices[0].message.content

def speak_old(text):
    engine.say(text)
    engine.runAndWait()
    
def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 


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
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            for article in articles:
                speak(article["title"])
                
    else:
        output = aiprocess(c)
        speak(output)

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