import speech_recognition as sr
import webbrowser as webbr
import pyttsx3
import music_library
from dotenv import load_dotenv
import os
import requests


load_dotenv('.env.local')

recognizer = sr.Recognizer()
engine = pyttsx3.init()
news_api_key = os.getenv('NEWS_API_KEY')

def speak(text):
   engine.say(text)
   engine.runAndWait()

def processCommand(c):
   if "open google" in c.lower():
      webbr.open("https://www.google.com")
   elif "open instagram" in c.lower():
      webbr.open("https://www.instagram.com")
   elif "open github" in c.lower():
      webbr.open("https://www.github.com")
   elif "open linkedin" in c.lower():
      webbr.open("https://www.linkedin.com")
   elif "open youtube" in c.lower():
      webbr.open("https://www.youtube.com")
   elif c.lower().startswith("play"):
      song = c.lower().split(" ")[1]
      link = music_library.music[song]
      webbr.open(link)

   elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={news_api_key}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])


if __name__ == "__main__":
   speak("Initializing Jarvis....")
   # Liten for the wake word jarvis
   # obtain audio from the microphone
   while True:
      r = sr.Recognizer()

      # recognize speech using Sphinx
      try:
         with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout=2, phrase_time_limit=1)
         word = r.recognize_google(audio)
         if (word.lower() == "jarvis"):
            speak("Yes")
            with sr.Microphone() as source:
               print("Jarvis is Listning")
               audio = r.listen(source)
               command = r.recognize_google(audio)

               processCommand(command)
            #Listen for Command
      except Exception as e:
         print("Error; {0}".format(e))