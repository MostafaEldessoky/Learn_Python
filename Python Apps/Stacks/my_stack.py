
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_stack = Node(value)
        self.top = new_stack
        self.length = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_stack = Node(value)
        if self.length == 0:
            self.top = new_stack
        else:
            new_stack.next = self.top
            self.top = new_stack
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.length -= 1
        return temp


my_stack = Stack(7)
my_stack.push(23)
my_stack.push(3)
my_stack.push(11)
print(my_stack.pop(), '\n')
my_stack.print_stack()