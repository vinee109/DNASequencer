import struct

def sequence(reads):
	reads = remove_substrings(reads)
	while len(reads) > 1:
		overlaps = pair_overlap(reads)
		heap = struct.MaxHeap(overlaps, key=lambda x:x[2])
		i, j, length = heap.remove_max()
		u, v = reads[i], reads[j]
		merged = u[:len(u)-length] + v
		reads = reads[0:min(i, j)] + reads[min(i, j) + 1:max(i, j)] + reads[max(i, j)+1:]
		reads.append(merged)
	return reads[0]

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
	lst = []
	for i in range(len(reads)):
		for j in range(len(reads)):
			if i != j:
				len_overlap = overlap(reads[i], reads[j])[0]
				if len_overlap > 0:
					lst.append((i, j, len_overlap))
	return lst


