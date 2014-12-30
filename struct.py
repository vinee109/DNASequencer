
class Heap():

    def __init__(self, items, key=lambda x:x):
        self.items = items
        self.f = key
        if len(items) > 0:
            self.heapify(self.items)
    
    # runs in linear time
    def heapify(self, lst):
        '''Turns a list `A` into a max-ordered binary heap.'''
        n = len(lst) - 1
        # start at last parent and go left one node at a time
        for node in range(n/2, -1, -1):
            self.__siftdown(node)
        return

    # runs in log(n) time
    def insert(self, val):
        '''Pushes a value onto the heap `A` while keeping the heap property 
        intact.  The heap size increases by 1.'''
        self.items.append(val)
        self.__siftup(len(self.items) - 1)   # furthest left node
        return

    # runs in log(n) time
    def remove_top(self):
        '''Returns the max value from the heap `A` while keeping the heap
        property intact.  The heap size decreases by 1.'''
        n = len(self.items) - 1
        self.__swap(self.items, 0, n)
        max = self.items.pop(n)
        self.__siftdown(0)
        return max

    def size(self):
        return len(self.items)
        
    def __swap(self, lst, i, j):
        # the pythonic swap
        lst[i], lst[j] = lst[j], lst[i]
        return

    # runs in log(n) time   
    def __siftdown(self, node):
        '''Traverse down a binary tree `A` starting at node `node` and 
        turn it into a max-heap'''
        child = 2*node + 1
        # base case, stop recursing when we hit the end of the heap
        if child > len(self.items) - 1:
            return
        # check that second child exists; if so find max
        if (child + 1 <= len(self.items) - 1) and (self.f(self.items[child+1]) > self.f(self.items[child])):
            child += 1
        # preserves heap structure
        if self.f(self.items[node]) < self.f(self.items[child]):
            self.__swap(self.items, node, child)
            self.__siftdown(child)
        else:
            return

    # runs in log(n) time    
    def __siftup(self, node):
        '''Traverse up an otherwise max-heap `A` starting at node `node`
        (which is the only node that breaks the heap property) and restore 
        the heap structure.'''
        parent = (node - 1)/2
        if self.f(self.items[parent]) < self.f(self.items[node]):
            self.__swap(self.items, node, parent)
        # base case; we've reached the top of the heap
        if parent <= 0:
            return
        else:
            self.__siftup(parent)

class MaxHeap(Heap):

    def __init__(self, items, key=lambda x:x):
        Heap.__init__(self, items, key=key)

    def max(self):
        return self.items[0]

    def remove_max(self):
        return self.remove_top()