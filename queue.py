class queue(object):
	list_of_items = []

	def __init__(self):
		pass

	def enqueue(self,item):
		self.list_of_items.append(item)

	def dequeue(self):
		self.list_of_items.pop(0)

	def peek(self):
		try:
			return self.list_of_items[0]
		except IndexError:
			print("看屁看，没见过空的list啊") # No, it will not run in Python 2
