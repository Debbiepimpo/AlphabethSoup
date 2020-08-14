#!/usr/bin/python
# -*- coding: utf-8 -*-


import function as f
import os #for clear screen 

# Main loop - infinite
while True:
	os.system('clear')
	print("Do you have enough letters? Let's find it.")
	print("******************************************\n")


	phrase, soup = f.inputStrings()

	if(len(phrase) > len(soup)):
		print("\nUnfortunately you dont have enough letters in your bowl.")
		f.runOrFight()

	elif(len(phrase) == 0 or len(soup) == 0):
		print("\nOpps! It looks like the bowl is empty...")
		f.runOrFight()

	else: # Start Game
		# Messages
		isOk = "Correct! "
		notOk = "Unfortunately the phrase is not found on the soup."

		print("\n---------------------------------------------------------\n")
		result, time   = eval("f.compareSoup(phrase, soup)")
		print("==================================================\n" )

		print("\nTotal results: \n")
		print(" ", (isOk if result else notOk), "Time elapsed: ", time)

		f.runOrFight()