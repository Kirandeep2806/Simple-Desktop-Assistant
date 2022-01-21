# Install pyaudio using the after executing requirements file, using "pywin install pyaudio"

"""

Q1. What is this code about ?
Ans : This code acts like a chatbot which can perform certain operations which user asks...

Q2. What can this chatbot do ?
Ans : This chatbot can perform several operation until you say "stop". The list of operations are given below...

        1. Set alarm
        2. Set reminder
        3. Play music
        4. Play movies
        5. Searches on  Wikipedia
        6. Opening Google
        7. Opening Yahoo
        8. Opening Bing
        9. Opening Youtube
        10. Say Current time
        11. Say Current date
        12. Say the weather report
                a. Temperature
                b. Windspeed
                c. Dewpoint
                d. Humidity
                e. Conditions
        [ Remember that we can't say surely that we obtain all of these for any place which is considered ].
        13. Make any other Searches...
        14. Answer few else questions regarding it, like...
                a. What is your age
                b. Who created you
                c. Where are you from
                d. Tell me about you
                e. What you can do
                f. Sing a song
                g. Tell a poem
                h. I love you
                i. Thank you
                j. Are you better than alexa, google assistant and siri
                k. Who are your friends
                l. Are you married
                m. What is your gender
                n. I miss you
                o. What is your name
                p. Favourite actor
                q. Favourite actress
                r. Favourite place
                s. Favourite food
                t. Favourite anchor
                u. Favourite singer
                v. Favourite colour
                w. Favourite movie
                x. Favourite musician
                y. Favourite song
                z. Your Inspiration or hero
                za. What is my age
                zb. Do you like anyone
                zc. Whom do you like
                zd. What is your speciality
        15. Display the alarms that you have set
        16. Also display the reminders that you have set

3. How to search in wikipedia ?
A.  It is very pretty simple simply say
          -----------------------------------------
         |   Syntax :  <which wikipedia> wikipedia   |
           ----------------------------------------

        Example : 1. Sachin Tendulkar wikipedia
                      2.  Mahesh babu Wikipedia , etc.,

---> When you want to play a music/play a video, all these will be played randomly...

"""

import os
import pyttsx3
import datetime
from wolframalpha import Client
from re import sub
import speech_recognition as sr
import webbrowser
from random import randint
import wikipedia
from pygame import mixer
import time

try:
    i =j=count_a=count_r= 0
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice",voices[1].id)
    engine.setProperty("rate", 150)

    def speak(data):

        engine.say(data)

        engine.runAndWait()

    def wish(name):

        hour = int(datetime.datetime.now().hour)

        if hour>=00 and hour<12:
            speak(f"Good Morning {name}!")
        elif hour>=12 and hour<18:
            speak(f"Good Afternoon {name}!")
        else:
            speak(f"Good Evening {name}!")

        speak(f"Say something ...!")

    def sinput():

        r = sr.Recognizer()
        r.energy_threshold = 3000
        r.pause_threshold = 1
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language = "en-in")
            print(f"{query}")
        except:
            print("Failed !")
            return "None"
        return query.lower()

    def voice(to_be_said):
        print(to_be_said)
        speak(to_be_said)

    def weather():
        try:
            voice("Wait until the information is being fetched. It takes a while...!")
            ind = sign = 0
            client = Client("UGU68L-8Q9H2PAUJA")
            search = client.query(data)
            first_one = next(search.results).text
            check = first_one.split("(")
            for i in check:
                if "minutes" in i or "hours" in i or "seconds" in i or "minute" in i or "hour" in i or "second" in i:
                    sign = 1
                    break
                ind += 1
            if sign == 1:
                for j in range(ind, len(check)):
                    try:
                        check.pop(ind)
                    except IndexError:
                        break
            first_one = ", ".join(check)
            first_one = sub("\)", "", first_one)
            first_one = sub("m/s", "metres per second", first_one)
            first_one = sub("\|", "is", first_one)
            first_one = sub(":", " is", first_one)
            return first_one
        except:
            voice("Sorry for inconvenience ! An error occurred while fetching the information. Make sure that you said is a valid query...")

    def respond(data):

        if "tell me about you" in data or "say me about you" in data or "say about you" in data or "tell about you" in data or "your intro" in data or "your introduction" in data:
            print("This is Zira, I am a chatbot created by the mentors of Government Polytechnic college which is located in the Masab Tank of the Hyderabad. I was born on the auspicious occassion of 'Gandhi Jayanti' which is 2nd October. My year of birth is 2019. I can fulfill your requirements based on the things or requests that I have acquired from my mentors. Irrespective of the functionalities of other chatbots I am a bit different")
            speak("This is Zira, I am a chatbot created by the mentors of Government Polytechnic college which is located in the Masab Tank of the Hyderabad. I was born on the auspicious occassion of 'Gandhi Jayanti' which is 2nd October. My year of birth is 2019. I can fulfill your requirements based on the things or requests that I have acquired from my mentors. Irrespective of the functionalities of other chatbots I am a bit different")

        elif "what you can do" in data or "what can you do" in data:
            print("""1. Set alarm
    2. Set reminder
    3. Play music
    4. Play movies
    5. Searches on  Wikipedia
    6. Opening Google
    7. Opening Yahoo
    8. Opening Bing
    9. Opening Youtube
    10. Say Current time
    11. Say Current date
    12. Answer few else questions...""")
            speak("I can make set alarms, set reminder, play music, play movies, show searches on wikipedia. I can open google, bing, yahoo, youtube. I can tell the current time and current date. Also I can answer to some of my information")

        elif "sing a song" in data or "poem" in data or "sing song" in data:
            if "poem" in data:
                voice(f"{name}! You will be screaming if I say poem. I am not interested to make my owner to get annoyed. So, I can't make your wish possible!")
            else:
                voice(f"{name}! You will be screaming if I sing song. I am not interested to make my owner to get annoyed. So, I can't make your wish possible but I can play a music for you. Shall I ?")
                option = sinput()
                if "yes" in option or "yeah" in option or "ya" in option or "yah" in option or "obviously" in option or "surely" in option:
                    respond("music")

        elif "special about you" in data or "your speciality" in data:
            speak("You aren't matured enough to know my speciality !")

        elif "i love you" in data:
            speak("I love you too...")

        elif "google assistant" in data or "siri" in data or "alexa" in data:
            speak(f", Yeew ! Hey {name}, please don't compare me with those kind of assistants or chatbots...")

        elif "your friends" in data:
            speak(f"{name},I am lonely! Do you wanna be my friend ?")
            option = sinput()
            if "yes" in option or "yeah" in option or "ya" in option or "yah" in option or "obviously" in option or "surely" in option or "for sure" in option:
                speak(f"Thanks {name}, for being one of my friend. Sorry ! It's one and only friend.")

        elif "married" in data:
            speak("Nope! Not anymore, I am an eternal child chatbot. So, I can't get married")

        elif "i miss you" in data:
            speak(f"{name}, I am with you ever and forever !")

        elif "your gender" in data:
            speak(f"{name}, guess my gender ?")
            k=0
            while k != 1:
                option = sinput()
                if "female" in option:
                    speak(f"Oh {name}! you've done a pretty good job by guessing my gender correctly.")
                    break
                elif "male" in option or "mail" in option:
                    speak(f"So close, but not appropriate...Try again {name}")
                else:
                    speak("What you said is not a gender. Please try again!")

        elif 'time' in data:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            voice(f"The time is {time}")

        elif 'date' in data:
            date = datetime.datetime.now().strftime("%m-%d-%y")
            voice(f"The date is {date}")

        elif "do you like anyone" in data or "did you fell in love" in data or "did you like anyone" in data:
            voice("I was not supposed to say! But, Yeah...")

        elif "who is that" in data or "your favourite person" in data or "whom do you like" in data or "who do you like" in data or "crush" in data:
            voice("I feel shy! But, coming to the truth, It's my creator 'Govardhan Reddy'")

        elif "your favourite actor" in data or "actor do you like" in data or "actor is your favourite" in data:
            voice("I actually want to make it a bit confidential, but as your my user I need to look after all your requirements. So, coming to my favourite actor, I love 'Chris Hemsworth'")

        elif "your favourite actress" in data or "actress do you like" in data or "actress is your favourite" in data:
            voice("I actually want to make it a bit confidential, but as your my user I need to look after all your requirements. So, coming to my favourite actress I like 'Scarlett Johannson'")

        elif "your inspiration" in data or "your hero" in data:
            voice(f"You are my one and only inspiration {name}!")

        elif "your favourite song" in data or "song do you like" in data or "song is your favourite" in data:
            voice(f"{name}, I like the song 'Faded' which is an album from the world's best music artiste 'Alan Walker'")

        elif "your favourite movie" in data or "movie do you like" in data or "movie is your favourite" in data or "your favourite film" in data or "film do you like" in data or "film is your favourite" in data:
            voice("I like the movie 'Avenger's Endgame', but I feel very sorrow for the death of Iron man!")

        elif ("your favourite" in data or "do you like" in data or "is your favourite" in data) and ("place" in data or "location" in data or "destination" in data or "spot" in data):
            voice("It's hard to say one place as a favourite destination. But most of all I like 'India' which has one of the richest and vivid histories and heritage")

        elif "your favourite singer" in data or "singer do you like" in data or "singer is your favourite" in data:
            voice("It may be a controversial question, but coming to the fact I love 'Justin Bieber'")

        elif ("your favourite" in data or "do you like" in data or "is your favourite" in data) and ("musician" in data or "music director" in data):
            voice("Oops ! Such a tough question ? But I am with my answer and it is the 'A.R.Rahman'")

        elif ("your favourite" in data or "do you like" in data or "is your favourite" in data) and ("anchor" in data or "host" in data):
            voice("It could be a fine good question ! But the answer made very simple and it is 'Salman Khan', who can be a best anchor, cum host, cum actor")

        elif ("your favourite" in data or "do you like" in data or "is your favourite" in data) and ("colour" in data or "color" in data):
            voice("Black could be my favourite, because every one in world can see it including the blind !")

        elif ("your favourite" in data or "do you like" in data or "is your favourite" in data) and ("dish" in data or "food" in data or "recipe" in data or "item" in data):
            voice("I love to eat a pizza with extra cheese and extra sauce")

        elif 'your age' in data:
            born = datetime.datetime(2019, 10, 2, 18, 33, 46, 570551)
            age = str(datetime.datetime.now() - born)
            seconds = "".join(list(reversed(age[-8:-10:-1])))
            minutes = "".join(list(reversed(age[-11:-13:-1])))
            hours = "".join(list(reversed(age[-14:-16:-1])))
            days = age[0:age.index("d") - 1]
            voice(f"My age is {days} days, {hours} hours, {minutes} minutes and {seconds} seconds")

        elif "your name" in data or "who are you" in data:
            speak("Zira, what my friends call me")

        elif "created you" in data:
            speak("I was created by mentors of GPT Masab Tank")

        elif "your address" in data or "you from" in data:
            speak("I am from top 1 Polytechnic college of Telangana")

        elif "my age" in data:
            speak("Your fitness is saying your age")

        elif "music" in data or "refresh" in data or "songs" in data:
            speak("Obviously !")
            music_dir = r"D:\Music"
            songs = os.listdir(music_dir)
            a = randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir, songs[a]))

        elif "movie" in data or "video" in data:
            speak("For sure !")
            videos_dir = r"D:\VIDEOS"
            videos = os.listdir(videos_dir)
            a = randint(0, len(videos)-1)
            os.startfile(os.path.join(videos_dir, videos[a]))

        elif ("alarm" in data or "reminder" in data) and ("show" in data or "display" in data):
            if "alarm" in data:
                if count_a == 1:
                    print(f"The alarm is set for {n_a}")
                    speak(f"The alarm is set for {n_a}")
                else:
                    voice("No alarm has been set. To set an alarm just simply say, ' Set alarm'...")
            else:
               if count_r == 1:
                    voice(f"You've set the reminder saying that, '{rem}'")
                    speak("Do you want to know when the reminder has to be reminded ?")
                    option = sinput()
                    if "yes" in option or "yeah" in option or "ya" in option or "yah" in option or "obviously" in option or "surely" in option or "for sure" in option:
                        print(f"The reminder is set for {n_r}")
                        speak(f"The reminder is set for {n_r}")
               else:
                   voice("No reminder has been set. To set a reminder just simply say, ' Set reminder'...")

        elif ("alarm" in data or "reminder" in data) and ("set" in data or "put" in data or "keep" in data):
            if "alarm" in data:
                opt = "alarm"
            if "reminder" in data:
                opt = "reminder"
            def  set_alarm():
                voice("Say the time in 24 hours format...")
                j=i=1
                while j!=0:
                    while i!=0:
                        try:
                            speak(f"Say the hour of the {opt}...")
                            a = sinput()
                            hour = int(check_hour(a))
                            break
                        except:
                            speak("What you said isn't a hour. Please say a hour which is a number")
                    while i != 0:
                        try:
                            speak(f"Say the minutes of the {opt}...")
                            b = sinput()
                            min = int(check_minute(b))
                            break
                        except:
                            speak("What you said isn't a minute. Please say a minute which is a number")
                    try:
                        alarm_time = datetime.datetime.combine(datetime.datetime.now().date(),datetime.time(hour,min))
                        say = alarm_time.strftime("%H:%M:%S")
                        voice(f"The {opt} is set for {say}")
                        break
                    except:
                        voice(f"{name}! Either the hour or the minute you said was exceeding their range...So please say again !")
                return say
            n = set_alarm()
            return n

        elif "google" in data or "chrome" in data:
            if "google" in data:
                s = "google"
            else:
                s = "chrome"
            speak(f"Opening {s}...")
            webbrowser.open_new_tab("https://www.google.com")

        elif "youtube" in data:
            speak("Opening youtube...")
            webbrowser.open_new_tab("https://www.youtube.com")

        elif "yahoo" in data:
            speak("Opening yahoo...")
            webbrowser.open_new_tab("https://www.yahoo.com")

        elif "bing" in data:
            speak("Opening bing...")
            webbrowser.open_new_tab("https://www.bing.com")

        elif "wikipedia" in data:
            try:
                speak("Searching Wikipedia...")
                data = data.replace("wikipedia","")
                result = wikipedia.summary(data, sentences=2)
                speak(f"According to wikipedia...")
                print(result)
                speak(result)
            except wikipedia.PageError:
                voice("Data not found in Wikipedia")
            except:
                voice("Oops! An unexpected error occured due to either the Internet issues or the Server issues...")

        elif "thank you" in data or "thanks" in data or "thankyou" in data:
            voice(f"It's my pleasure and duty {name}")

        elif "weather" in data:
            if "my" in data or "current" in data or "this" in data:
                voice(f"Oops! Unable to fetch the location. Sorry {name}, try with the name of your city.")
            else:
                a = weather()
                print("-" * 20, "The weather is : ", "-" * 20, sep="\n")
                speak("Here is the weather report !")
                print(a)
                speak(a)

        elif "temperature in" in data or "dew point in" in data or "dewpoint in" in data or "conditions in" in data or "condition in" in data or "humidity in" in data or "wind speed in" in data or "windspeed in" in data:
            try:
                data = sub("wind speed", "windspeed", data)
                data = sub("dew point", "dewpoint", data)
                count = 0
                ind = sign = 0
                o = ["temperature", "humidity", "dewpoint", "conditions", "condition", "windspeed"]
                client = Client("UGU68L-8Q9H2PAUJA")
                a = data.split()
                for i in o:
                    if i in a:
                        a.remove(i)
                        query = i
                if "in" in a:
                    a.remove("in")
                if "at" in a:
                    a.remove("at")
                if "what" in a:
                    a.remove("what")
                if "is" in a:
                    a.remove("is")
                if "the" in a:
                    a.remove("the")
                a = ','.join(a)
                voice("Wait until the information is being fetched. It takes a while...!")
                search = client.query("weather in " + a)
                first_one = next(search.results).text
                first_one = sub("wind speed", "windspeed", first_one)
                first_one = sub("dew point", "dewpoint", first_one)
                check = first_one.split("(")
                for i in check:
                    if "minutes" in i or "hours" in i or "seconds" in i or "minute" in i or "hour" in i or "second" in i:
                        sign = 1
                        break
                    ind += 1
                if sign == 1:
                    for j in range(ind, len(check)):
                        try:
                            check.pop(ind)
                        except IndexError:
                            break
                first_one = ", ".join(check)
                first_one = sub("\)", "", first_one)
                first_one = sub("m/s", "metres per second", first_one)
                first_one = sub("\|", "is", first_one)
                first_one = sub(":", " is", first_one)
                a = first_one.split("\n")
                for i in range(0, len(a)):
                    l = a[0].split(",")
                    for j in range(0, len(l)):
                        a.append(l[j])
                    a.remove(a[0])
                    count += 1
                a.pop()
                count = 0
                for i in a:
                    if query in i:
                        print(i)
                        speak(i)
                        count = 1
                if count == 0:
                    voice("Oops! Data not found!")
            except:
                print(f"{name},either there was an error when finding the place you are searching for, or, the place you are searching for is not found...")

        elif "tell about" in data or "tell me" in data or "say me" in data or "say about" in data or "what" in data or "who" in data or "acknowledge" in data:
            a = ["tell about", "tell me", "say me", "say about", "what", "who", "acknowledge"]
            for i in a:
                if i in data:
                    temp = i
                    break
            temp = data.replace(temp,"")
            try:
                result = wikipedia.summary(temp, sentences=2)
                speak(f"I have found the following results for you {name}!")
                print(result)
                speak(result)
            except:
                try:
                    a = weather()
                    voice(f"{name}, I have some results, do you want me read it ?")
                    option = sinput()
                    if "yes" in option or "yeah" in option or "ya" in option or "yah" in option or "obviously" in option or "surely" in option:
                        print(a)
                        speak(a)
                except:
                    webbrowser.open_new_tab("https://www.google.com")
        else:
            try:
                a = weather()
                speak(f"{name}, I have found the following information...")
                voice(a)
            except:
                voice("The data not found, or there may be issues with the internet...")

    def sound():

        mixer.init()
        mixer.music.load(os.path.join(__file__, "..", "alarm_3 ringtone.mp3"))
        n = 5
        while n>0:
            mixer.music.play()
            time.sleep(4)
            n = n-1

    def check_hour(a):

        if a=="zero":
            return 0
        elif a=="Tu" or a=="tu" or a=="tube":
            return 2
        elif a=="tree" or a=="free":
            return 3
        elif a=="sex":
            return 6
        elif a=="n":
            return 10
        elif a=="well" or a=="tubewell":
            return 12
        elif a=="xx":
            return 20
        else:
            return a

    def check_minute(a):

        if a=="zero":
            return 0
        elif a=="Tu" or a=="tu":
            return 2
        elif a=="tree" or a=="free":
            return 3
        elif a=="sex":
            return 6
        elif a=="n":
            return 10
        elif a=="well":
            return 12
        elif a=="xx":
            return 20
        elif a=="x**" or a=="tatti":
            return 30
        elif a[0]==8 and len(a)==2:
            return a-50
        else:
            return a

    while j!=1:
        speak("This is Zira, Say your name in single word?")
        name = sinput()
        if name=="None":
            j=0
        else:
            break

    wish(name)
    while i !=1:
        if count_a==1:
            def alarm():
                while True:
                        print("Alarm")
                        break
                sound()
                return 0
            if time.localtime().tm_hour >= hour_a and time.localtime().tm_min >= min_a:
                count_a = alarm()

        if count_r==1:
            if time.localtime().tm_hour >= hour_r and time.localtime().tm_min >= min_r:
                voice(f"{name}! Did you forget that you've set a reminder...?")
                option = sinput()

                if "yes" in option or "yeah" in option or "ya" in option or "yah" in option or "obviously" in option or "nope" in option or "no" in option:
                    print(f"{rem}")
                    speak(f"You've set the reminder saying that, '{rem}'")
                    count_r = 0

        data = sinput()
        if "alarm" in data and ("set" in data or "put" in data or "keep" in data):
                n_a = respond(data)
                count_a = 1
                hour_a=int("".join(n_a[0:2]))
                min_a=int("".join(n_a[3:5]))

        elif "reminder" in data and ("set" in data or "put" in data or "keep" in data):
            voice("What do you want to be reminded ?")
            rem = sinput()
            n_r = respond(data)
            count_r = 1
            hour_r = int("".join(n_r[0:2]))
            min_r = int("".join(n_r[3:5]))

        else:
            if "stop" in data or "bye" in data or "meet you again" in data or "leave" in data:
                speak(f"This is Zira, Signing off bye bye...")
                break
            else:
                respond(data)
except Exception as a:
    print("Sorry! An unexpected error occured...")
    print(a)
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice",voices[1].id)
    engine.setProperty("rate", 150)
    engine.say("Sorry! An unexpected error occured...")
    engine.runAndWait()
