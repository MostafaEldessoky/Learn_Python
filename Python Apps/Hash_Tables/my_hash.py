
class Hash:
    def __init__(self, size):
        self.table = [None] * size

    def print_table(self):
        for i, val in enumerate(self.table):
            print(i, ": ", val)

    def __hash(self, key):
        index = 0
        for i in key:
            index = (index + ord(i)) % len(self.table)
        return index

    def set_value(self, key, value):
        index = self.__hash(key)
        if self.table[index] is None:
            self.table[index] = []
        self.table[index].append([key, value])

    def get(self, key):
        index = self.__hash(key)
        if self.table[index] is None:
            return None
        else:
            for i in range(len(self.table[index])):
                if self.table[index][i][0] == key:
                    return self.table[index][i][1]

    def keys(self):
        temp = []
        for i in self.table:
            if i is not None:
                for j in i:
                    temp.append(j[0])
        return temp







my_hash_table = Hash(7)

my_hash_table.set_value('bolts', 1400)
my_hash_table.set_value('washers', 50)

print(my_hash_table.get('bolts'))
print(my_hash_table.get('washers'))
print(my_hash_table.get('lumber'))
print(my_hash_table.keys())
