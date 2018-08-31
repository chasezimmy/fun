class Node:
	def __init__(self, val, next=None):
		self.val = val
		self.next = next

class LinkedList:
	def __init__(self, head=None, tail=None):
		self.head = head
		self.tail = tail

	def push(self, val):
		new = Node(val)
		new.next = self.head
		self.head = new


	def insert(self, val):
		new = Node(val)

		curr = self.head

		while curr.next:
			curr = curr.next
		curr.next = new

	def print(self):
		curr = self.head
		while curr:
			yield curr.val

			if curr.next:
				curr = curr.next
			else:
				break

linked_list = LinkedList()
linked_list.push(2)
linked_list.push(1)
linked_list.push(0)
linked_list.insert(3)


for i in linked_list.print():
	print(i)

