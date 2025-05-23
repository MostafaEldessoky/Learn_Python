
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value > temp.value:
                if temp.right is not None:
                    temp = temp.right
                else:
                    temp.right = new_node
                    return True
            elif new_node.value < temp.value:
                if temp.left is not None:
                    temp = temp.left
                else:
                    temp.left = new_node
                    return True
            else:
                return False

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value == temp.value:
                return True
            if value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False







my_tree = BST()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)


print(my_tree.contains(27))

print(my_tree.contains(17))



























