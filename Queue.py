
### Question 1

class Node:
	def __init__(self, value, next):
		self.value = value
		self.next = next

class Queue:
	def __init__(self):
		self.head = None
		self.tail = None

	def push(self, value):
	# # push 
	# oldhead = self.head
	# newhead = Node(value, oldhead)
	# self.head = newhead

	# if (self.tail is None):
	# 	self.tail = self.head

		newnode = Node(value, None)

		if (self.tail is None):
			self.tail = newnode
			self.head = newnode

		else:
			self.tail.next = newnode
			self.tail = newnode 

	def pop(self):
		# pop
		oldhead = self.head

		if (oldhead is not None):
			self.head = oldhead.next
		else:
			return None

		if (self.head is None):
			self.tail = None

		return oldhead.value

	def dump(self):
		#dump
		current = self.head
		while (current is not None):
			print current.value,
			current = current.next
		print


queue = Queue()

queue.push(2)
queue.push(2)
queue.push(2)
queue.push(1)
queue.push(3)
queue.push(3)
queue.push(4)
queue.push(6)
queue.push(5)
queue.push(7)
queue.push(8)
queue.push(9)
queue.push(10)

print "State of queue after pushing: ",
queue.dump()

# print "Popping from queue:"
# print queue.pop() #3
# print queue.pop() #2
# print queue.pop() #1
# queue.push(4)
# print queue.pop() #None





### Question 2

def removeEvens(headNode):
			# remove the even numbers from a list.
			currentNode = headNode
			previousNode = None

			while (currentNode is not None):
				nextNode = currentNode.next
				
				if (currentNode.value % 2 == 0):
					if (currentNode == headNode):
						headNode = nextNode
					else: 
						previousNode.next = nextNode
				
				else:
					previousNode = currentNode
				
				currentNode = nextNode
			
			# should return the head node when complete
			return headNode


queue.head = removeEvens(queue.head)
queue.dump()