class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node
    
    def __str__(self):
        output = "head -> "
        if self.head is None:
            output += None
        else:
            current = self.head
            while(current):
                output += f"{current.value} -> "
                current = current.next
            output += "None"
            return output

# "head -> 1 -> 2 -> 3 -> 4 -> None"


# ll = LinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(3)
# ll.append(4)

# value = 3
# node = Node(3)   # node.next = None


# ll
# head
# Node(1) -> Node(2) -> Node(3) -> None
# current




if __name__=="__main__":
    # node1 = Node('Abdullah')
    # node2 = Node('Jana')
    # node3 = Node(34)
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    print(ll)

# 6.78

# head
# node1  ->   node2  ->  node3  ->  node(value) -> None



# class Band:
#     pass


# band1 = Band()
# band1.members = [guitarist1, basist1, basist2]