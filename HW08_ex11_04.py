#!/usr/bin/env python
# Exercise 4  
# (1) Modify reverse_lookup_old so that it builds and returns a list of all
# keys that map to v, or an empty list if there are none.

# (2) Paste in your completed functions from HW08_ex_11_02.py

# (3) Do not edit what is in main(). It should print what is returned, a list
# of the keys that map to the values passed.
##############################################################################
def reverse_lookup_old(d, v):
	a = []
	for k in d:    
		if str(d[k]) == v:
			a.append(k)
	return a
	raise ValueError

def reverse_lookup_new(d, v):
	rev_keys = []
	for k in d:
		if str(d[k]) == v:
			rev_keys.append(k)
	return rev_keys


##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 BELOW: ##################
##############################################################################
def histogram_new(s):
	dict_ = {}
	for item in s:
		dict_[item] = dict_.get(item, 0) + 1
	return dict_
def get_pledge_list():
	""" Opens pledge.txt and converts to a list, each item is a word in 
	the order it appears in the original file. returns the list.
	"""
	with open('pledge.txt') as f:
		pledge_list = f.read().split()
		pledge_list = [item[:-1] if item[-1] in [".", ",",":"] else item for item in pledge_list]
	return pledge_list



##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 ABOVE: ##################
##############################################################################
def main():   # DO NOT CHANGE BELOW
	pledge_histogram = histogram_new(get_pledge_list())
	print reverse_lookup_new(pledge_histogram, "1")
	print reverse_lookup_new(pledge_histogram, "9")
	print reverse_lookup_new(pledge_histogram, "Python")

if __name__ == '__main__':
    main()
