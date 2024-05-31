import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes
import PySimpleGUI as sg
import weather as weather
import youtube as youtube


engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time(x):
    Time = datetime.datetime.now().strftime("%I: %M: %S")
    if x==0:
        speak("The current time is")
        speak(Time)
    else:
        query = 'The current time is: {}'.format(Time)
        return query

def date(x):
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    if x==0:
        speak("The current Date is")
        speak(day)
        speak(month)
        speak(year)
    else:
        query = 'The current Date is: {}/{}/{}'.format(day, month, year)
        return query

def age(x):
    creation_date = datetime.datetime(2023, 9, 22)
    current_date = datetime.datetime.now()
    diff = current_date - creation_date
    years = diff.days // 365
    months = (diff.days % 365) // 30
    days = (diff.days % 365) % 30
    answer = f"My age is {years} years, {months} months, and {days} days."
    if years==0:
        answer = answer.replace(" 0 years, ", "")
        if months==0:
            answer = answer.replace("0 months, and", "")
    if x==0:
        speak(answer)
    else:
        return answer

def wishMe():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good morning sir!")
    elif hour>=12 and hour<18:
        speak("Good afternoon sir!")
    else:
        speak("Good evening sir!")
    speak("Amigo at your service. Please tell me how can i help you?")

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening.....")
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = r.listen(source, timeout=5, phrase_time_limit=10)  # Listen for up to 5 seconds with a 5-second phrase time limit

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except sr.WaitTimeoutError:
        print("Listening timed out, no speech detected.")
        return "none"

    except Exception as e:
        print(e)
        speak("Say that again, please...")
        return "none"

    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.ehlo()
    server.starttls()
    server.login('testproject488@gmail.com','1q!@#$%^')
    server.sendmail('testproject488@gmail.com', to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:/Users/tusha/Amigo/ss.png")

def cpu(x):
    usage = str(psutil.cpu_percent())
    battery =psutil.sensors_battery()
    if x==0:
        speak('CPU is at'+ usage)
        speak("battery is at")
        speak(battery)
    else:
        answer = 'CPU is at: {}\nbattery is at: {}'.format(usage, battery)
        return answer

def jokes(x):
    if x==0:
        speak(pyjokes.get_joke())
    else:
        answer = pyjokes.get_joke()
        return answer

def command(query, x):
    if 'time' in query:
        time(x)
    elif 'date' in query:
        date(x)
    elif 'hello' in query:
        wishMe()
    elif 'wikipedia' in query:
        speak("searching...")
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        print(result)
        speak(result)
    elif 'song' in query:
        query = query.replace("song", "")
        youtube.youtubesearch(query)
    elif 'music' in query:
        query = query.replace("song", "")
        youtube.youtubesearch(query)
    elif 'video' in query:
        query = query.replace("song", "")
        youtube.youtubesearch(query)
    elif 'youtube' in query:
        query = query.replace("song", "")
        youtube.youtubesearch(query)
    elif 'play' in query:
        query = query.replace("song", "")
        youtube.youtubesearch(query)
    elif 'send email' in query:
        try:
            speak("What should i say?")
            content = takeCommand()
            to = 'hakirmubarmaj@gmail.com'
            sendEmail(to, content)
            speak("Email has been sent Successfully!")
        except Exception as e:
            print(e)
            speak("unable to send mail")
    elif 'search in chrome' in query:
        speak("What should i search?")
        chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        search = takeCommand().lower()
        wb.get(chromepath).open_new_tab(search+ '.com')
    elif 'play song' in query:
        songsdir = 'D:\samsung j7\Voice Recorder'
        songs = os.listdir(songsdir)
        os.startfile(os.path.join(songsdir, songs[0]))
    elif 'screenshot' in query:
        screenshot()
        speak("Done")
    elif 'remember that' in query:
        speak("What should i remember")
        data = takeCommand()
        remember = open('data.txt', 'a')
        remember.write(data)
        remember.close()
    elif 'do you know anything' in query:
        remember = open('data.txt', 'r')
        speak(remember.read())
    elif 'cpu' in query:
        cpu(x)
    elif 'joke' in query:
        jokes(x)
    elif 'your name' in query:
        name = open('Amigo.txt', 'r')
        nameread = f'My name is {name.read()}.'
        speak(nameread)
    elif 'old are you' in query:
        age(x)
    elif 'weather' in query:
        speak(weather.weather_info)
    elif 'offline' in query:
        speak("Going offline..")
        quit()
    elif 'chat' in query:
        responseA(query, 1)    
    else:
        try:
            speak(wikipedia.summary(query, sentences=2))
        except Exception as e:
            print(e)
            speak("Please say that again")

def responseA(query, x):
    if 'time' in query:
        answer = time(x)
    elif 'date' in query:
        answer = date(x)
    elif 'send email' in query:
        try:
            speak("What should i say?")
            content = takeCommand()
            to = 'hakirmubarmaj@gmail.com'
            sendEmail(to, content)
            speak("Email has been sent Successfully!")
        except Exception as e:
            print(e)
            speak("unable to send mail")
    elif 'remember that' in query:
        query = query.replace("remember that", "")
        remember = open('data.txt', 'w')
        remember.write(query)
        remember.close()
        answer = 'Done!'
    elif 'recall' in query:
        remember = open('data.txt', 'r')
        answer = remember.read()
    elif 'cpu' in query:
        answer = cpu(x)
    elif 'joke' in query:
        answer = jokes(x)
    elif 'your name' in query:
        name = open('Amigo.txt', 'r')
        answer = f'My name is {name.read()}.'
    elif 'old are you' in query:
        answer = age(x)
    elif 'weather' in query:
        answer = weather.weather_info
    elif 'offline' in query:
        quit()
    else:
        try:
            answer = wikipedia.summary(query, sentences=2)
        except Exception as e:
            print(e)
            answer = 'Enter text correctly...'
    return answer

def appFunction():
    query = takeCommand().lower()
    command(query, 0)

if __name__ == "__main__":
   
    while True:
        query = takeCommand().lower()
        if 'chat' in query:
            layout = [
            [sg.Multiline("", size=(60, 55), key="output", disabled=True)],
            [sg.InputText("", size=(60, 1), key="input"), sg.Button("Send")]
            ]

            window = sg.Window("Amigo", layout)
            chat_history = ""

            while True:
                event, values = window.read()

                if event == sg.WIN_CLOSED:
                    break

                user_input = values["input"]
                chat_history += f"You: {user_input}\n"
                window["output"].update(chat_history)

                answer = responseA(user_input, 1)
                chat_history += f"Amigo: {answer}\n\n"
                window["output"].update(chat_history)

            window.close()
        else:
            command(query, 0)
