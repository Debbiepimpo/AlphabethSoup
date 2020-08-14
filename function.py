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
	
	# Count char occurencies in phrase 
	phElem = Counter(phrase)
	
	# Once dictionarys are unordered, covert it to a reversed rdered list.
	# So, loop will exit soon by testing for bigger occurenciesm which are the ines that have most probability of failling

	nPhrase = OrderedDict(sorted(phElem.items(), key=lambda t: t[1], reverse=True)) 
	
	lSoup = list(soup) #Maybe we can still using string

	result = 1
	iterations = 0 # Index for number of tests made

	# Check if for any char have fewer occurencies in soup that in phrase
	# We use a regular loop instead of a comprehension loop, so we can break it after the first negative match 

	for x in nPhrase:
		iterations +=1
		if  lSoup.count(x) < phElem[x]:
			result = 0
			print("Not enougth '{}' letters. Have {}, {} needed.".format(x, lSoup.count(x), phElem[x]))
			break

	lp = len(phrase)
	ls = len(soup)

	nlp = len(nPhrase)

	"""
		Big-O depends on:
			- Number of char in phrase to map
			- Number of char in mapped phrase, once it is the one that lead the comparation loop
			- So, in this case we will have a O(n1), where n1 < n for n=#phsares 
			- The efficiency of algorithm will increase with bigger datasets and when repetitions of char in them became more frequent.
			- Will also deppend from the efficiency of counting method in list.count().
			- For small datasets and low level of repetitions the method 1 (loop over list) will remain faster, once processing 
			dictionaries are "heavier" than lists
			- For really big datasets we will have to consider using better tools like Pandas or Spark. 
	"""

	print("\nLength of phrase (n): ", lp)
	print("Length of soup (m): ", ls )
	print("Count of individual char in phrase: (n1): ", nlp )
	print("Big-O (n1 <= n [O(n1)]:", nlp )
	print("# of iterations:", iterations )
	
	end_time = datetime.now()

	print("Start Time: ", start_time)
	print("End Time: ", end_time)

	duration = end_time - start_time
	print('Duration: {}'.format(duration))
	
	return result, duration
