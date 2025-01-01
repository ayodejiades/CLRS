class TreeNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left_child = left
        self.right_child = right

class BinarySearchTree:
    def __init__ (self):
        self.root = None

    def search(self, search_value):
        current_node = self.root
        while current_node:
            if search_value == current_node.data:
                return True
            elif search_value < current_node.data:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        return False
    
    def insert(self, data):
        new_node = TreeNode(data)
        if self.root is None:
            self.root = new_node
            return
        else:
            current_node = self.root
            while True:
                if data < current_node.data:
                    if current_node.left_child is None:
                        current_node.left_child = new_node
                        return
                    else:
                        current_node = current_node.left_child
                elif data > current_node.data:
                    if current_node.right_child is None:
                        current_node.right_child = new_node
                        return
                    else:
                        current_node = current_node.right_child

    def find_min(self):
        current_node = self.root
        while current_node.left_child:
            current_node = current_node.left_child
        return current_node.data
    
bst = BinarySearchTree()

bst.insert(13)
bst.insert(1)
bst.insert(2)

print(bst.search(1))
print(bst.find_min())