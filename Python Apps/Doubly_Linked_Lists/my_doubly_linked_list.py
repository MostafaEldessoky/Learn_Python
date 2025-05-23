
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.pre = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail.next.pre = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail.pre.next = None
            self.tail = self.tail.pre
            self.tail.next = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.pre = new_node
            self.head.pre.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.pre.next = None
            self.head.pre = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index > self.length - 1:
            return None
        if index <= (self.length/2):
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.pre
            return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        new_node = Node(value)
        temp = self.get(index-1)
        if temp.next:
            new_node.next = temp.next
            new_node.pre = temp
            temp.next.pre = new_node
            temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        temp = self.get(index - 1)
        if temp.next:
            temp.next = temp.next.next
            temp.next.pre.pre = None
            temp.next.pre.next = None
            temp.next.pre = temp
        self.length -= 1
        return True


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(3)
my_doubly_linked_list.prepend(5)
my_doubly_linked_list.prepend(3)
my_doubly_linked_list.pop_first()
my_doubly_linked_list.pop_first()
my_doubly_linked_list.insert(3,9)
my_doubly_linked_list.set_value(4, 7)
my_doubly_linked_list.remove(3)
my_doubly_linked_list.print_list()




































