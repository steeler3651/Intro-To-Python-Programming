# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: J.W. Calinger
# Creation Date: October 7, 2020
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	#ERROR -- should be only one apostrophe on each end of quote
	print()

def chooseCave():
	cave = ''
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()
		#ERROR: Inconsistent use of tabs and spaces in indentation

	return caves
	#ERROR -- should be: return cave

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3)
	#ERROR -- should be timesleep(2)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		#ERROR -- program shouldn't compare a digit to a string
		print('Gives you his treasure!')
	else:
		print 'Gobbles you down in one bite!'
		#ERROR -- should have parentheses around quote to be printed

playAgain = 'yes'
while playAgain = 'yes' or playAgain = 'y':
	#ERROR -- should have double equal signs: while playAgain == 'yes' ...
	displayIntro()
	caveNumber = choosecave()
	#ERROR -- should be: chooseCave()
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
		print("Thanks for planing")
		#ERROR -- should be 'Thanks for playing'
		#ERROR -- program ends without end message for answers besides 'yes' or 'y', or 'no'
