#!/usr/bin/env python
# Exercise 1  
# Write a function that reads the words in words.txt and stores them as keys
# in a dictionary (returning the dictionary). It doesnt matter what the 
# values are. Then you can use the in operator as a fast way to check whether
# a string is in the dictionary.
##############################################################################
import random
def store_to_dict():
	with open('words.txt') as f:
		dict_1 = {x.strip():random.randint(1,10000) for x in f}
	return dict_1

	##############################################################################
def main():  # DO NOT CHANGE BELOW
	words_dict = store_to_dict()
	if "this" in words_dict:
		print "Yup."
	if "qwertyuiop" in words_dict:
		print "Hmm."

if __name__ == '__main__':
	main()
