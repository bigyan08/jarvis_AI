import os
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib

def speak(audio):
    os.system(f"espeak '{audio}'")

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am Jarvis Sir. Please tell me how may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said: {query}\n")
    
    except Exception:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    # Implement your email sending logic here
    pass

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
        
        elif 'play music' in query:
            # Provide the correct location of your music directory
            music_dir = '/path/to/your/music'
            songs = os.listdir(music_dir)
            print(songs)
            os.system(f"xdg-open {os.path.join(music_dir, songs[0])}")
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            # Provide the correct location of your code editor (e.g., VSCode)
            code_path = '/path/to/your/code/editor'
            os.system(f"{code_path} &")
        
        elif 'close' in query:
            speak("Closing the program. Goodbye!")
            break
