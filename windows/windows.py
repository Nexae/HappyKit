import os, time, sys, random

quotes = [
 	"Be Happyyyy!.",#By nexae
 	"Try to be a rainbow in someones cloud.", #Maya Angelou
 	"I can't change the direction of the wind, but I can adjust my sails to always reach my destination.", #Jimmy Dean
 	"Change your thoughts and you change the world.", #Norman Vincent Peale
 	"Every strike brings me closer to the next home run.", #By Babe Ruth
 	"The mind is everything. What you think you become.", #By Buddha
 	"Your time is limited, so don't waste it living someone else's life.", #One of my favorites. By Steve Jobs
 	"You can't use up creativity. The more you use, the more you have.", #True. By Maya Angelou
 	"It always seems impossible until its done.", #Nelson Mandela
 	"It is not in the stars to hold our destiny but in ourselves.", #By William Shakespeare
 	"Life is really simple, but we insist on making it complicated.", #Confucius
 	"Most folks are as happy as they make their minds to be.", #Abraham Lincoln
 	"Being deeply loved by someone gives you strength, while loving someone deeply gives you courage.", #Lao Tzu
 	"If you can dream it, you can do it.", #Walt Disney
 ]
 
while True:
 
	nice =  random.choice(quotes)
 	os.system('cd Desktop')
 	os.system('cd happykit')
 	os.system('cd windows')
 	os.system('notifu /m "Happy Kit" /p "' + nice + '" /d 10000')
 	
 	#The pop up will go on for 10 seconds. Every 5 minutes a new quote comes up. 
 	time.sleep(310)

