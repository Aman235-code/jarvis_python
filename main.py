import speech_recognition as sr
import webbrowser
import pyttsx3
import music

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    print(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif c.lower().startswith("play"):
        print("here")
        song = c.lower().split(" ")[1]
        link = music.musics[song]
        webbrowser.open(link)

    else:
        # Let openai handle the req
        pass

    
if __name__ == "__main__":
    speak("Initializing Jarvis......")
    while True:
        # Listen for the wake word Jarvis
        r = sr.Recognizer()
        # recognize speech using Sphinx
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening........")
                audio = r.listen(source,timeout=10, phrase_time_limit=7)
            word = r.recognize_google(audio)
            print(word)
            if word.lower() == "jarvis":
                speak("Yes Aman")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        
        except Exception as e:
            print("Error {0}".format(e))
    

   

    