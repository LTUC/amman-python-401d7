from types import new_class
from linked_list import LinkedList


class HashTable(object):
    def __init__(self, size=1024):
        self.size = size
        self.map = [None]*size
        # self.map = [LinkedList()]*size
        # self.map = [[]]*size

    def custom_hash(self, key):
        sum_of_asccii = 0
        for ch in key:
            asccii_of_ch = ord(ch)
            sum_of_asccii+= asccii_of_ch
        temp_value = sum_of_asccii*19
        hashed_key = temp_value%self.size
        return hashed_key

    def add(self, key, value):
        # def __set_item__()
        hashed_key = self.custom_hash(key)
        if not self.map[hashed_key]:
            self.map[hashed_key] = value
        else:
            if isinstance(self.map[hashed_key], LinkedList):
                self.map[hashed_key].add([key,value])
            else:   
                chain = LinkedList()
                existing_pair = self.map[hashed_key]
                new_pair =[key,value]
                self.map[hashed_key]=chain
                chain.add(existing_pair)
                chain.add(new_pair)

    def get_value(self, key):
        # def __get_item__()
        hashed_key=self.custom_hash(key)
        return self.map[hashed_key]
if __name__ == "__main__":
    hashtable= HashTable()
    hashtable.add("AHMAD",30)
    hashtable.add("YAHYA",30)
    hashtable.add("HAMAD",55)

    for index,item in enumerate(hashtable.map):
        if item:
            print(index, item)

