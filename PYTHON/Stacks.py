class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        newNode = Node(data)
        if self.top:
            newNode.next = self.top
        self.top = newNode
        self.size += 1
    
    def pop(self):
        if self.top is None:
            return None
        else:
            poppedNode = self.top
            self.size -= 1
            self.top = self.top.next
            poppedNode.next = None
            return poppedNode.data
        
    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None


