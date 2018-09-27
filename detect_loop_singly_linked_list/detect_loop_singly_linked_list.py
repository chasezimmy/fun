class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def detect_loop(self, head):
        d = {}
        while head is not None:
            if head.val not in d.keys():
                d[head.val] = []
            else:
                return True # loop detected
            head = head.next

        return False # no loop

linked_list = Node(0)
linked_list.next = Node(1)
linked_list.next.next = Node(2)
linked_list.next.next.next = Node(3)
linked_list.next.next.next = Node(4)

ll = LinkedList()

print(ll.detect_loop(linked_list))