import os, time, sys, random

quotes = [
 	"Be Happyyyy!.",#By nexae
 	"Try to be a rainbow in someones cloud.", #Maya Angelou
 	"Change your thoughts and you change the world.", #Norman Vincent Peale
 	"Every strike brings me closer to the next home run.", #By Babe Ruth
 	"The mind is everything. What you think you become.", #By Buddha
        "Don't waste your life living someone else's.", #Edited quote from Steve Jobs
 	"You can't use up creativity.", #True. By Maya Angelou
 	"It always seems impossible until its done.", #Nelson Mandela
 	"Most folks are as happy as they make their minds to be.", #Abraham Lincoln
 	"If you can dream it, you can do it.", #Walt Disney
 ]
 
while True:
 
	nice =  random.choice(quotes)
 	os.system('cd happykit')
 	os.system('cd windows')
 	os.system('notifu /m "Happy Kit" /p "' + nice + '" /d 10000 /t info /q /w')
 	#The pop up will go on for 10 seconds. Every 5 minutes a new quote comes up. 
 	time.sleep(310)

