import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit
import webbrowser
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 180)  # Speed of speaking

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def wish_user():
    hour = datetime.datetime.now().hour
    name = "Ansh"

    if 0 <= hour < 12:
        greet = "Good Morning"
    elif 12 <= hour < 18:
        greet = "Good Afternoon"
    else:
        greet = "Good Evening"

    speak(f"{greet}, {name}!")
    speak("I am your desktop assistant. How can I help you today?")

def take_command():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that. Please try again.")
        return "none"
    except sr.RequestError:
        speak("Speech service is down. Please check your internet.")
        return "none"
    except Exception as e:
        speak("There was a problem with the microphone.")
        print(f"Error: {e}")
        return "none"

def run_ai_desktop():
    wish_user()

    while True:
        query = take_command()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            try:
                result = wikipedia.summary(query.replace("wikipedia", ""), sentences=2)
                speak(result)
            except:
                speak("Sorry, I couldn't find anything on Wikipedia.")

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube.")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            speak("Opening Google.")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open notepad' in query:
            os.system("notepad")

        elif 'open chrome' in query:
            path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Update if needed
            if os.path.exists(path):
                os.startfile(path)
            else:
                speak("Chrome path not found. Please check the installation.")

        elif 'play' in query:
            song = query.replace('play', '')
            pywhatkit.playonyt(song)
            speak(f"Playing {song} on YouTube.")

        elif 'search' in query:
            search_query = query.replace('search', '')
            pywhatkit.search(search_query)
            speak(f"Searching for {search_query}.")

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye Ansh, have a great day!")
            break

        else:
            speak("Sorry, I don't understand that command.")

# Start the assistant
if __name__ == "__main__":
    run_ai_desktop()
