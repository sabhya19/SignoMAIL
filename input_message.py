import speech_recognition as s_r
import pyttsx3
import pyaudio
import winsound
import msvcrt as m
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
frq=400
dur= 700
engine = pyttsx3.init() 
engine.setProperty('rate',150)
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', en_voice_id)
#function to ask the user reciever id while sending mail
def askreciever() :
   engine.say("Please provide reciever's email address;")
   engine.runAndWait()
   r= s_r.Recognizer()
   my_mic = s_r.Microphone(device_index=1)
   with my_mic as source: 
      print("Enter or speak reciever's email address")
      myaudio= r.listen(source, timeout= 5)
   try:
      print("you said-",r.recognize_google(myaudio))
   except LookupError:
      print("Sorry, could not process!!")
      engine= pyttsx3.init()
      engine.say("sorry, could not process")
      engine.runAndWait()
   reciever= r.recognize_google(myaudio)
   reciever= reciever +'@gmail.com'
   print("the reciever's id is: ",reciever)
   engine= pyttsx3.init()
   engine.say("the reciever's id is: ",reciever)
   engine.runAndWait()
   return reciever
#function to ask subject to be put in mail subject
def ask_subject():
   engine= pyttsx3.init()
   engine.say('Please enter or speak subject for mail; for no subject, say nil')
   engine.runAndWait()
   with my_mic as source:
      print("Enter or Speak Subject")
      myaudio= r.listen(source,phrase_time_limit= 15)
   subject= r.recognize_google(myaudio)
   print('Subject: ',subject)
   engine= pyttsx3.init()
   engine.say('Subject;;')
   engine.say(subject)
   engine.runAndWait()
   return subject
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#function to ask the content of mail
def ask_content():
   engine.say('Please speak the content of mail')
   engine.runAndWait()
   with my_mic as source:
      print("Enter or speak your mail")
      myaudio= s_r.listen(source)
   content= s_r.recognize_google(myaudio)
   print("My Content: ",content)
   engine= pyttsx3.init()
   engine.say('content-')
   engine.say(content)
   engine.runAndWait()
   return content
#

