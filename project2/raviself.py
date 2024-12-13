import pyttsx3
import speech_recognition as sr
import webbrowser 
import datetime

def speech_text():
    recognizer= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try :
            print("recogining...")
            data = recognizer.recognize_google(audio)  
            print(data)
            return data
        except sr.UnknownValueError:
            print("not understand")
def text_speech(X):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        rate =engine.getProperty('rate')
        engine.setProperty('rate',150)
        engine.say(X)
        engine.runAndWait()
       


if __name__=='__main__':
    if "ravi" in speech_text().lower():
     
         while True:
           data1=speech_text().lower()
           if "your name"in data1:
               name="ravi raj"
               text_speech(name)
           elif "exit" in data1:
                speech_text('thank you')
           elif " your father's name " in data1:
                father="i am a program created by ravi raj, so my god is ravi raj. "
                text_speech(father)
           elif 'now time' in data1:
                time= datetime.datetime.now().strftime ("%I%M%p")
                text_speech(time)
           elif "have you eaten"in data1:
                eat="i can't eat food, but i need electricity for energy."
                text_speech(eat)
           elif 'open youtube' in data1:
                webbrowser.open("https://www.youtube.com/watch?v=x4Az6Ys-9DA&list=OLAK5uy_knqqEw9SO4zwqK70C08qhMBfTdB7xrma4&index=2&ab_channel=ShilpiRaj-Topic")
           elif"aapka naam"in data1:
                nam="mera naam ravi raj hai"
                text_speech(nam)
           elif "python kya "in data1:
                p="Python is a popular high-level programming language known for its simple syntax and powerful features, such as web development, data analysis, and artificial intelligence."
                text_speech(p)
           elif "bye" in data1:
                text_speech("Thank you. and  keep smile.")
                break

    else:
        print("thanks")
     