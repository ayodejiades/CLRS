class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        newNode = Node(data)
        if self.head:
            newNode.next = self.head
            self.head = newNode
        else:
            self.tail = newNode
            self.head = newNode
    
    def remove_at_beginning(self):
        self.head = self.head.next