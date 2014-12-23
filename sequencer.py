import struct

def sequence(reads):
	reads = remove_substrings(reads)

def overlap(u, v):
	"""
	Calculates the largest overlap of u on the left and v on the right.
	Returns a tuple containing the length of the overlap and the actual overlap
	>>> overlap('abcd', 'bcdefgh')
	(3, 'bcd')
	>>> overlap('abcd', 'abcdefgh')
	(4, 'abcd')
	>>> overlap('abcd', 'dog')
	(1, 'd')
	"""
	for i in range(min(len(u), len(v)), 0, -1):
		if u[len(u)-i:] == v[:i]:
			return i, v[:i]
	return 0, ''

def remove_substrings(reads):
	lst = []
	for i in range(len(reads)):
		for j in range(len(reads)):
			if i != j and reads[i] in reads[j]:
				lst.append(reads[j])
	return lst 


