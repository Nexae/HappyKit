import time, sys, random
from gi.repository import Notify

#Quotes left: 12

quotes = [
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
	"If you're offered a seat on a rocket ship, don't ask what seat! Just get on.", #Sheryl Sandberg
	"If you're going to be thinking anything, you might as well think big.", #Donald Trump
	"Pearls don't lie on the seashore. If you want one, you must dive for it.", # Chinese proverb
	"The universe has no restrictions. You place restrictions on the universe with your expectations.", #Deepak Chopra
	"In order to succeed, your desire for success should be greater than your fear of failure.", #Bill Cosby
	"There is only one way to avoid criticism: do nothing, say nothing, and be nothing.", #Aristotle
	"Always go with your passions. Never ask yourself if it's realistic or not.", #Deepak Chopra
	"Leap and the net will appear.", #Zen Saying
	"Be a yardstick of quality. Some people aren't used to an environment where excellence is expected.", #Awesome quote...;) By Steve Jobs
	"Only those who will risk going too far can possibly find out how far one can go.", #T. S. Eliot
	"The best time to plant a tree was 20 years ago. The second best time is now.", #Chinese Proverb
	"I am thankful for all of those who said NO to me. It's because of them I'm doing it myself.", #Albert Einstein
	"If you do what you've always done, you'll get what you've always gotten.", #Tony Robbins
	"Life is the art of drawing without an eraser." #John W. Gardner
	"The earth has music for those who listen."  #William Shakespeare
]

while True:
 
	RandomQuote =  random.choice(quotes)

	Notify.init("Quoti")
	ShowQuote = Notify.Notification.new("" + RandomQuote + "", "Quoti by Nexae", "dialog-information")
	ShowQuote.show()
 	
 	#The pop up will go on for eleven seconds. Every 15 minutes a new quote comes up. 
 	time.sleep(911)