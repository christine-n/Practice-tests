class Stack:
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		self.items.pop()

	def isEmpty(self):
		return self.items == []

