class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def enqueue(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
            
    def dequeue(self):
        if self.head:
            currentNode = self.head
            self.head = currentNode.next
            currentNode.next = None

            if self.head == None:
                self.tail = None         