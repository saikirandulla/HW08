#!/usr/bin/env python
# Exercise 2  
# Dictionaries have a method called get that takes a key and a default value.
# If the key appears in the dictionary, get returns the corresponding value; 
# otherwise it returns the default value. For example:

# >>> h = histogram('a')
# >>> print h
# {'a': 1}
# >>> h.get('a', 0)
# 1
# >>> h.get('b', 0)
# 0

# (1) Use get to write histogram_old more concisely. You should be able to
# eliminate the if statement.

# (2) Use histogram_new to take pledge.txt and create a dict histogram with
# word counts (do not change the case of the words).
##############################################################################

# Imports

# Body


pledge_histogram = {}

def histogram_old(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def histogram_new(s):
	dict_ = {}
	for item in s:
		dict_[item] = dict_.get(item, 0) + 1
	for key,value in sorted(dict_.items()):
		print key,value
	return dict_
def get_pledge_list():
	""" Opens pledge.txt and converts to a list, each item is a word in 
	the order it appears in the original file. returns the list.
	"""
	with open('pledge.txt') as f:
		pledge_list = []
		for line in f:
			words = line.split()
			pledge_list += words
	return pledge_list

##############################################################################
def main():  # DO NOT CHANGE BELOW
    print histogram_new(get_pledge_list())

if __name__ == '__main__':
    main()
