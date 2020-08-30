#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from collections import Counter, OrderedDict

from datetime import datetime

def runOrFight():
	"""
		Handless the user interactivity to continue or stop
	"""
	answer = " "
	while answer[0].upper() not in ["Y", "N"]:
		answer = input("\nDo you want to try again (Y/n)? ")
		if(len(answer) > 0): # If user just it Enter key, it is assumed "Y"
			if(answer[0].upper() == "N"):
				print("\nThank you for playing. Bye!")
				exit()
		else:
			answer = "Y"

def inputStrings():
	"""
		Grab the input data.
		First string with the phrase
		Second string with de letter soup
	"""

	print("Spaces are important too.")
	a = input("Your phrase, please: ")
	b = input("And now your bowl of letters, please: ")

	return a,b

def compareSoup(phrase, soup):
	"""
		Get every different char in phrase, and it's number of occurencies.
		After, we compare its number with count in soup string.
		we avoid the necessity to count all chars in soup, when we only need the ones in phrase  
		We sort phrase dict, as consumes time
		We use a list for soup.
	"""
	start_time = datetime.now()

	# We have to convert soup to list once strings are immutable

	soup = list(soup)
	lp = len(phrase)
	ls = len(soup)

	"""
		We check for every element of the phrase in soup.
		If it fails, we know that have elements on phrase that are not in soup.
		So we only process the number of elements in phrase, and count repeted elements
	"""

	result = 1

	try:
		[soup.remove(x) for x in phrase ]
	except:
		# remove failed, some element of Phrase are missing in soup
		result = 0
	
	end_time = datetime.now()

	print ("\nLength of phrase (n): ", lp)
	print ("Length of soup (m): ", ls)
	print ("Big-O [O(n*m)]:", lp*ls)

	print("Start Time: ", start_time)
	print("End Time: ", end_time)

	duration = end_time - start_time
	print('Duration: {}'.format(duration))
	
	return result, duration
