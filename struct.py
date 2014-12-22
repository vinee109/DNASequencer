class BinaryHeap():
	"""
	A BinaryHeap that holds the k smallest values. Each item is compared by a given function
	"""
	def __init__(self, k, f=lambda x: x):
		self.items = [None]
		self.size = 0
		self.f = f
		self.MAXSIZE = k

	def __str__(self):
		return str(self.items[1:])

	def empty(self):
		"""
		Returns true if the heap is emtpy, false otherwise
		"""
		return self.size == 0

	def insert(self, item):
		"""
		Inserts an item into the heap
		>>> heap = BinaryHeap(3)
		>>> heap.insert(5)
		>>> heap.size
		1
		>>> heap.insert(2)
		>>> heap.size
		2
		>>> heap.insert(13)
		>>> heap.size
		3
		>>> print heap
		[13, 2, 5]
		>>> heap.insert(6)
		>>> print heap
		[6, 2, 5]
		"""
		def insert_helper(item):
			if self.empty():
				self.size += 1
				self.items.append(item)
			else:
				self.size += 1
				self.items.append(item)
				self.bubbleUp(self.size)

		if self.size < self.MAXSIZE:
			insert_helper(item)
		elif self.size >= 1 and min(item, self.max(), key=self.f) == item:
			self.removeMax()
			insert_helper(item)

	def bubbleUp(self, index):
		if index == 1 or max(self.items[index], self.items[self.parent(index)], key=self.f) == self.items[self.parent(index)]:
			return
		self.items[index], self.items[self.parent(index)] = self.items[self.parent(index)], self.items[index]
		self.bubbleUp(self.parent(index))

	def bubbleDown(self, index):
		if self.rightChild(index) >= self.size or max(self.items[index], self.items[self.rightChild(index)], self.items[self.leftChild(index)], key=self.f) == self.items[index]:
			return
		swapped = 0
		if max(self.items[self.rightChild(index)], self.items[self.leftChild(index)], key=self.f) == self.items[self.rightChild(index)]:
			swapped = self.rightChild(index)
		else:
			swapped = self.leftChild(index)
		self.items[index], self.items[swapped] = self.items[swapped], self.items[index]
		self.bubbleDown(swapped)

	def removeMax(self):
		"""
		Removes the minimum item in the heap
		>>> heap = BinaryHeap(5)
		>>> heap.insert(10)
		>>> heap.insert(5)
		>>> heap.insert(6)
		>>> heap.insert(7)
		>>> heap.removeMax()
		10
		>>> heap.removeMax()
		7
		>>> heap.removeMax()
		6
		>>> heap.removeMax()
		5
		>>> print heap
		[]
		"""
		if self.size == 1:
			self.size -= 1
			return self.items.pop()
		self.size -= 1
		maximum, self.items[1] = self.items[1], self.items.pop()
		self.bubbleDown(1)
		return maximum

	def max(self):
		"""
		Returns the largest item in the heap
		"""
		return self.items[1]

	def get_items(self):
		"""
		Returns a list of all the items in the heap
		"""
		return self.items[1:]

	def parent(self, index):
		return index/2

	def rightChild(self, index):
		return index*2

	def leftChild(self, index):
		return index*2 + 1
