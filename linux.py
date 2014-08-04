#official HappyKit for Linux
import os, time, sys, random
from ConfigParser import SafeConfigParser

global setupUser

config = SafeConfigParser()
config.read("HappyConfig.cfg")

if config.has_section("settings") != True:
	config.add_section("settings")

if config.has_option("settings", "firsttime") != True :
	os.system("sudo apt-get install notify-send")
	config.set("settings", "firsttime", "false")

with open('HappyConfig.cfg', 'w') as f:
    config.write(f)
 
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
 	os.system("notify-send '" + nice + "' 'Happy Kit'")
 	
 	#The pop up will go on for ten seconds. Every 5 minutes a new quote comes up. 
 	time.sleep(310)
