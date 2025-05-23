class Node:
    def __init__(self, value):
        self.value = value
        self.pointer = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_linked_list(self):
        temp = self.head
        for _ in range(self.length):
            print(temp.value)
            temp = temp.pointer

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.pointer = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head.value = None
            self.head.pointer = None
        else:
            i = 0
            temp = self.head
            while i != self.length - 2:
                i += 1
                temp = temp.pointer
            self.tail = temp
            self.tail.pointer = None
        self.length -= 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.pointer = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.pointer
            temp.pointer = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return True

    def get_value(self, index):
        if index > self.length - 1 or index < 0:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.pointer
        return temp

    def set_value(self, index, value):
        temp = self.get_value(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index > self.length - 1 or index < 0:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get_value(index - 1)
        new_node.pointer = temp.pointer
        temp.pointer = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index > self.length - 1 or index < 0:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp1 = self.get_value(index - 1)
        temp2 = temp1.pointer
        temp1.pointer = temp2.pointer
        temp2.pointer = None
        self.length -= 1
        return temp2

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        for _ in range(self.length):
            after = temp.pointer
            temp.pointer = before
            before = temp
            temp = after


my_linked_list = LinkedList(1)
my_linked_list.append(9)
my_linked_list.append(25)
my_linked_list.append(8)

my_linked_list.set_value(1,5)

my_linked_list.print_linked_list()
