import subprocess 
import wolframalpha 
import pyttsx3 
import tkinter 
import json 
import random 
import operator 
import speech_recognition as sr 
import datetime 
import wikipedia 
import webbrowser 
import os 
import winshell 
import pyjokes 
import feedparser 
import smtplib 
import ctypes 
import time 
import requests 
import shutil 
from twilio.rest import Client 
from clint.textui import progress 
from bs4 import BeautifulSoup 
import win32com.client as wincl 
from urllib.request import urlopen

engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)

def speak(audio): 
	engine.say(audio) 
	engine.runAndWait() 

def wishMe(): 
	hour = int(datetime.datetime.now().hour) 
	if hour>= 0 and hour<12: 
		speak("Good Morning Sir !") 

	elif hour>= 12 and hour<18: 
		speak("Good Afternoon Sir !") 

	else: 
		speak("Good Evening Sir !") 

	assname =("Alex") 
	speak("I am your Assistant") 
	speak(assname) 
	

def usrname(): 
	speak("What should i call you sir") 
	uname = takeCommand() 
	speak("Welcome Mister") 
	speak(uname) 
	columns = shutil.get_terminal_size().columns 
	
	print("#####################".center(columns)) 
	print("Welcome Mr.", uname.center(columns)) 
	print("#####################".center(columns)) 
	
	speak("How can i Help you, Sir") 

def takeCommand(): 
	
	r = sr.Recognizer() 
	
	with sr.Microphone() as source: 
		
		print("Listening...") 
		r.pause_threshold = 1
		audio = r.listen(source) 

	try: 
		print("Recognizing...")	 
		query = r.recognize_google(audio, language ='en-in') 
		print(f"User said: {query}\n") 

	except Exception as e: 
		print(e)	 
		print("Unable to Recognizing your voice.") 
		return "None"
	
	return query 

def sendEmail(to, content): 
	server = smtplib.SMTP('smtp.gmail.com', 587) 
	server.ehlo() 
	server.starttls() 
	
	# Enable low security in gmail 
	server.login('your email id', 'your email passowrd') 
	server.sendmail('your email id', to, content) 
	server.close() 

if __name__ == '__main__': 
	clear = lambda: os.system('cls') 
	
	# This Function will clean any 
	# command before execution of this python file 
	clear() 
	wishMe() 
	usrname() 
	
	while True: 
		
		query = takeCommand().lower() 
		
		# All the commands said by user will be 
		# stored here in 'query' and will be 
		# converted to lower case for easily 
		# recognition of command 
		if 'wikipedia' in query: 
			speak('Searching Wikipedia...') 
			query = query.replace("wikipedia", "") 
			results = wikipedia.summary(query, sentences = 3) 
			speak("According to Wikipedia") 
			print(results) 
			speak(results) 

		elif 'open youtube' in query: 
			speak("Here you go to Youtube\n") 
			webbrowser.open("youtube.com") 

		elif 'open google' in query: 
			speak("Here you go to Google\n") 
			webbrowser.open("google.com") 

		elif 'open stackoverflow' in query: 
			speak("Here you go to Stack Over flow.Happy coding") 
			webbrowser.open("stackoverflow.com") 

		elif 'play music' in query or "play song" in query: 
			speak("Here you go with music") 
			# music_dir = "G:\\Song" 
			music_dir = "D:\\songs"
			songs = os.listdir(music_dir) 
			print(songs)	 
			random = os.startfile(os.path.join(music_dir, songs[1])) 


		elif 'send a mail' in query: 
			try: 
				speak("What should I say?") 
				content = takeCommand() 
				speak("whome should i send") 
				to = input()	 
				sendEmail(to, content) 
				speak("Email has been sent !") 
			except Exception as e: 
				print(e) 
				speak("I am not able to send this email") 

		elif 'how are you' in query: 
			speak("I am so lucky to have such caring person like you, How are you sir") 
			speak("How are you, Sir") 

		elif 'fine' in query or "good" in query: 
			speak("It's good to know that your fine") 

		elif "change my name to" in query: 
			query = query.replace("change my name to", "") 
			assname = query 

		elif "change name" in query: 
			speak("What would you like to call me, Sir ") 
			assname = takeCommand() 
			speak("Thanks for naming me") 

		elif "what's your name" in query or "What is your name" in query: 
			speak("My friends call me") 
			speak(assname) 
			print("My friends call me", assname) 

		elif 'exit' in query: 
			speak("Thanks for giving me your time") 
			exit() 

		elif "who made you" in query or "who created you" in query: 
			speak("I have been created by Nachiket.") 
			
		elif 'joke' in query: 
			speak(pyjokes.get_joke()) 
			
		elif "calculate" in query: 
			
			app_id = "Wolframalpha api id"
			client = wolframalpha.Client(app_id) 
			indx = query.lower().split().index('calculate') 
			query = query.split()[indx + 1:] 
			res = client.query(' '.join(query)) 
			answer = next(res.results).text 
			print("The answer is " + answer) 
			speak("The answer is " + answer) 

		elif 'search' in query or 'play' in query: 
			
			query = query.replace("search", "") 
			query = query.replace("play", "")		 
			webbrowser.open(query) 

		elif "who i am" in query: 
			speak("If you talk then definately your human.") 

		elif "why you came to world" in query: 
			speak("Thanks to Nachiket. further It's a secret") 


		elif 'Kasa ahes' in query: 
			speak("Mi majet, tumhi kase aahat") 

		elif "who are you" in query: 
			speak("I am your virtual assistant created by Nachiket") 

		elif 'change background' in query: 
			ctypes.windll.user32.SystemParametersInfoW(20,0,"Location of wallpaper",0) 													 																										
			speak("Background changed succesfully") 
		
		elif 'lock window' in query: 
				speak("locking the device") 
				ctypes.windll.user32.LockWorkStation() 

		elif 'shutdown system' in query: 
				speak("Hold On a Sec ! Your system is on its way to shut down") 
				subprocess.call('shutdown / p /f') 
				
		elif 'empty recycle bin' in query: 
			winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
			speak("Recycle Bin Recycled") 

		elif "don't listen" in query or "stop listening" in query: 
			speak("for how much time you want to stop Alex from listening commands") 
			a = int(takeCommand()) 
			time.sleep(a) 
			print(a) 

		elif "where is" in query: 
			query = query.replace("where is", "") 
			location = query 
			speak("User asked to Locate") 
			speak(location) 
			webbrowser.open("https://www.google.nl / maps / place/" + location + "") 

		elif "camera" in query or "take a photo" in query: 
			ec.capture(0, "Alex Camera ", "img.jpg") 

		elif "restart" in query: 
			subprocess.call(["shutdown", "/r"]) 
			
		elif "hibernate" in query or "sleep" in query: 
			speak("Hibernating") 
			subprocess.call("shutdown / h") 

		elif "log off" in query or "sign out" in query: 
			speak("Make sure all the application are closed before sign-out") 
			time.sleep(5) 
			subprocess.call(["shutdown", "/l"]) 

		elif "write a note" in query: 
			speak("What should i write, sir") 
			note = takeCommand() 
			file = open('Alex.txt', 'w') 
			speak("Sir, Should i include date and time") 
			snfm = takeCommand() 
			if 'yes' in snfm or 'sure' in snfm: 
				strTime = datetime.datetime.now().strftime("% H:% M:% S") 
				file.write(strTime) 
				file.write(" :- ") 
				file.write(note) 
			else: 
				file.write(note) 
		
		elif "show note" in query: 
			speak("Showing Notes") 
			file = open("Alex.txt", "r") 
			print(file.read()) 
			speak(file.read(6)) 

		
		# NPPR9-FWDCX-D2C8J-H872K-2YT43 
		elif "Alex" in query: 
			
			wishMe() 
			speak("Alex 1 point o in your service Mister") 
			speak(assname) 

		elif "weather" in query: 
    			webbrowser.open("https://www.google.com/search?q=weather&oq=weather&aqs=chrome..69i57.2203j0j8&sourceid=chrome&ie=UTF-8") 
	    
		elif "Good Morning" in query: 
			speak("A warm" +query) 
			speak("How are you Mister") 
			speak(assname) 

		# most asked question from google Assistant 
		elif "will you be my gf" in query or "will you be my bf" in query: 
			speak("I'm not sure about, may be you should give me some time") 

		elif "how are you" in query: 
			speak("I'm fine, glad you me that") 

		elif "i love you" in query: 
			speak("It's hard to understand") 

		elif "what is" in query or "who is" in query: 
			
			# Use the same API key 
			# that we have generated earlier 
			client = wolframalpha.Client("API_ID") 
			res = client.query(query) 
			
			try: 
				print (next(res.results).text) 
				speak (next(res.results).text) 
			except StopIteration: 
				print ("No results") 

		# elif "" in query: 
			# Command go here 
			# For adding more commands 

