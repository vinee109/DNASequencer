import struct
THRESHOLD = 2

def sequence(reads):
	reads = remove_substrings(reads)
	overlaps, right_overlap_map, left_overlap_map = pair_overlap(reads)
	overlaps = sorted(overlaps, key=lambda x: x[2])
	left_overlap, right_overlap = {}, {}
	count = 0
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
	to_remove = set()
	for i in range(len(reads)):
		for j in range(len(reads)):
			if i != j and reads[i] in reads[j]:
				to_remove.add(i)
	return [reads[i] for i in range(len(reads)) if i not in to_remove]

def pair_overlap(reads):
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


