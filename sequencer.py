import struct
import time
from functools import wraps
THRESHOLD = 2

def sequence(reads):
	"""
	Takes in a list of reads and generates the shortest superstring that contains all the reads as
	substrings
	"""
	# removes all strings that are substrings of another read
	reads = remove_substrings(reads)
	# figure out all possible pairs of overlaps above a certain threshold
	overlaps, right_overlap_map, left_overlap_map = pair_overlap(reads)
	overlaps = sorted(overlaps, key=lambda x: x[2])
	
	left_overlap = {}	# mapping of overlaps where the key is the string on the left and the value is the string on the right
	right_overlap = {}	# mapping of overlaps where the key is the string on the right and the value is the string on the left

	count = 0	# number of overlaps processed
	# iterate through them from largest overlap to shortest overlap and create a mapping of all the largest overlaps
	# between pairs of reads
	# the loop stops when we either process all the overlaps or perform a merge for all of the reads
	while len(overlaps) > 0 and count < len(reads):
		u, v, length = overlaps.pop()
		if u not in left_overlap and v not in right_overlap:
			left_overlap[u] = (v, length)
			right_overlap[v] = (u, length)
			count += 1
	
	# finding the left most point in the sequence
	start = ''
	for u in left_overlap:
		if u not in right_overlap:
			start = u
	return generate_seq_from_overlaps(start, start, left_overlap)

def generate_seq_from_overlaps(seq, u, left_overlap):
	"""
	Creates a sequence given a starting point and a set of overlap mappings where for every key u, the value v represents
	an overlap of (u, v) of some length
	"""
	if u not in left_overlap:
		return seq
	v, length = left_overlap[u]
	return generate_seq_from_overlaps(seq[:len(seq)-length] + v, v, left_overlap)

# @profile
# def overlap(u, v):
# 	"""
# 	Calculates the largest overlap of u on the left and v on the right.
# 	Returns a tuple containing the length of the overlap and the actual overlap
# 	>>> overlap('abcd', 'bcdefgh')
# 	(3, 'bcd')
# 	>>> overlap('abcd', 'abcdefgh')
# 	(4, 'abcd')
# 	>>> overlap('abcd', 'dog')
# 	(1, 'd')
# 	"""
# 	for i in range(min(len(u), len(v)), 0, -1):
# 		if u[len(u)-i:] == v[:i]:
# 			return i, v[:i]
# 	return 0, ''

def overlap(text1, text2):
  	# Cache the text lengths to prevent multiple calls.  
  	text1_length = len(text1)  
  	text2_length = len(text2)  
  	# Eliminate the null case.  
  	if text1_length == 0 or text2_length == 0:  
		return 0  
  	# Truncate the longer string.  
  	if text1_length > text2_length:  
		text1 = text1[-text2_length:]  
  	elif text1_length < text2_length:  
		text2 = text2[:text1_length]  
  	# Quick check for the worst case.  
  	if text1 == text2:  
		length = min(text1_length, text2_length)  
		return length, text2[:length]
   
	# Start by looking for a single character match  
	# and increase length until no match is found.  
	best = 0  
	length = 1  
	while True:  
		pattern = text1[-length:]  
		found = text2.find(pattern)  
		if found == -1:  
			return best, text2[:best]  
		length += found  
		if text1[-length:] == text2[:length]:  
			best = length  
			length += 1  

def remove_substrings(reads):
	"""
	Takes in a list of reads and removes any read that is a substring of any other read
	"""
	to_remove = set()
	for i in range(len(reads)):
		for j in range(len(reads)):
			if i != j and reads[i] in reads[j]:
				to_remove.add(i)
	return [reads[i] for i in range(len(reads)) if i not in to_remove]

def pair_overlap(reads):
	"""
	Calculates all the lengths of overlaps above a threshold and creates a mapping of all overlaps
	Returns dictionaries for overlaps where the key is the string on the left and the key is the string on the right
	"""
	right_overlap_map = {}
	left_overlap_map = {}
	lst = []
	for i in reads:
		for j in reads:
			if i != j:
				len_overlap = overlap(i, j)[0]
				if len_overlap >= THRESHOLD:
					if i not in right_overlap_map:
						right_overlap_map[i] = []
					if j not in left_overlap_map:
						left_overlap_map[j] = []
					right_overlap_map[i] += [(j, len_overlap)]
					left_overlap_map[j] += [(i, len_overlap)]
					lst.append((i, j, len_overlap))
	return lst, right_overlap_map, left_overlap_map


