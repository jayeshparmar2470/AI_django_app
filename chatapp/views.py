# # # from django.shortcuts import render

# # # # Create your views here.
# # # chatapp/views.py

# # from django.shortcuts import render
# # import pyttsx3
# # import speech_recognition as sr
# # import datetime
# # import wikipedia
# # import webbrowser
# # import os
# # import smtplib

# # engine = pyttsx3.init('sapi5')
# # voices = engine.getProperty('voices')
# # engine.setProperty('voice', voices[0].id)

# # def speak(audio):
# #     engine.say(audio)
# #     engine.runAndWait()

# # def takeCommand():
# #     r = sr.Recognizer()
# #     with sr.Microphone() as source:
# #         print("Listening...")
# #         r.pause_threshold = 1
# #         audio = r.listen(source)

# #     try:
# #         print("Recognizing...")
# #         query = r.recognize_google(audio, language='en-in')
# #         print(f"User said: {query}\n")
# #     except Exception as e:
# #         print("Say that again please...")
# #         return "None"
# #     return query

# # def chat(request):
# #     # Check if the form is submitted
# #     if request.method == 'POST':
# #         query = request.POST['user_input'].lower()

# #         # Logic for executing tasks based on query
# #         if 'wikipedia' in query:
# #             speak('Searching Wikipedia...')
# #             query = query.replace("wikipedia", "")
# #             results = wikipedia.summary(query, sentences=2)
# #             speak("According to Wikipedia")
# #             return render(request, 'chatapp/home.html', {'result': results})
        
# #         # Add other chat logic here for other commands

# #     return render(request, 'home.html')
# # chatapp/views.py

# from django.shortcuts import render
# import wikipedia
# import webbrowser



# import pyttsx3 #pip install pyttsx3
# import speech_recognition as sr #pip install speechRecognition
# import datetime
# import wikipedia #pip install wikipedia
# import webbrowser
# import os
# import smtplib

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# # print(voices[1].id)
# engine.setProperty('voice', voices[0].id)


# def speak(audio):
#     engine.say(audio)
#     # engine.runAndWait()
#     # return 1


# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     if hour>=0 and hour<12:
#         speak("Good Morning!")

#     elif hour>=12 and hour<18:
#         speak("Good Afternoon!")   

#     else:
#         speak("Good Evening!")  

#     speak("I am Jarvis Sir. Please tell me how may I help you")   
#     # return 1    

# def takeCommand():
#     #It takes microphone input from the user and returns string output

#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)

#     try:
#         print("Recognizing...")    
#         query = r.recognize_google(audio, language='en-in')
#         print(f"User said: {query}\n")

#     except Exception as e:
#         # print(e)    
#         print("Say that again please...")  
#         return "None"
#     return query

# def chat(request):
#     # Check if the form is submitted
#     wishMe()
#     # if request.method == 'POST':
#     #     query = request.POST.get('user_input', '').lower()
#     #     response = ""

#     #     # Logic for executing tasks based on query
#     #     if 'open youtube' in query:
#     #         webbrowser.open("youtube.com")
#     #         response='openingggg youtubbeeee'
        
#     #     if 'wikipedia' in query:
#     #         response = 'Searching Wikipedia...'
#     #         query = query.replace("wikipedia", "")
#     #         results = wikipedia.summary(query, sentences=2)
#     #         response = f"According to Wikipedia: {results}"
       

        
#     #     while True:
#     #     # if 1:
#     #         query = takeCommand().lower()

#     #         # Logic for executing tasks based on query
#     #         if 'wikipedia' in query:
#     #             speak('Searching Wikipedia...')
#     #             query = query.replace("wikipedia", "")
#     #             results = wikipedia.summary(query, sentences=2)
#     #             speak("According to Wikipedia")
#     #             print(results)
#     #             speak(results)

#     #         elif 'open youtube' in query:
#     #             webbrowser.open("youtube.com")

#     #         elif 'open google' in query:
#     #             webbrowser.open("google.com")

#     #         elif 'open stackoverflow' in query:
#     #             webbrowser.open("stackoverflow.com")   

#     #     # Add other chat logic here for other commands

#     #     return render(request, 'home.html', {'response': response})

#     return render(request, 'home.html')



# # import pyttsx3 #pip install pyttsx3
# # import speech_recognition as sr #pip install speechRecognition
# # import datetime
# # import wikipedia #pip install wikipedia
# # import webbrowser
# # import os
# # import smtplib

# # engine = pyttsx3.init('sapi5')
# # voices = engine.getProperty('voices')
# # # print(voices[1].id)
# # engine.setProperty('voice', voices[0].id)


# # def speak(audio):
# #     engine.say(audio)
# #     engine.runAndWait()



# # def sendEmail(to, content):
# #     server = smtplib.SMTP('smtp.gmail.com', 587)
# #     server.ehlo()
# #     server.starttls()
# #     server.login('youremail@gmail.com', 'your-password')
# #     server.sendmail('youremail@gmail.com', to, content)
# #     server.close()

# # if __name__ == "__main__":


#         # elif 'play music' in query:
#         #     music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
#         #     songs = os.listdir(music_dir)
#         #     print(songs)    
#         #     os.startfile(os.path.join(music_dir, songs[0]))

#         # elif 'the time' in query:
#         #     strTime = datetime.datetime.now().strftime("%H:%M:%S")    
#         #     speak(f"Sir, the time is {strTime}")

#         # elif 'open code' in query:
#         #     codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
#         #     os.startfile(codePath)

#         # elif 'email to harry' in query:
#         #     try:
#         #         speak("What should I say?")
#         #         content = takeCommand()
#         #         to = "harryyourEmail@gmail.com"    
#         #         sendEmail(to, content)
#         #         speak("Email has been sent!")
#         #     except Exception as e:
#         #         print(e)
#         #         speak("Sorry my friend harry bhai. I am not able to send this email")    




from django.shortcuts import render
from django.http import JsonResponse
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def chat(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '').lower()

        # Your logic for processing user input and generating the response
        if 'wikipedia' in user_input:
            speak('Searching Wikipedia...')
            user_input = user_input.replace("wikipedia", "")
            results = wikipedia.summary(user_input, sentences=2)
            speak("According to Wikipedia")
            response_data = {'response': results}
        elif 'open youtube' in user_input:
            webbrowser.open("https://www.youtube.com/")
            response_data = {'response': 'Opening YouTube...'}
        elif 'open google' in user_input:
            webbrowser.open("https://www.google.com/")
            response_data = {'response': 'Opening Google...'}
        # Add other logic for different commands here

        else:
            response_data = {'response': "Sorry, I don't understand. Please try again."}

        # Returning the response as a JSON object
        return JsonResponse(response_data)

    return render(request, 'home.html')
