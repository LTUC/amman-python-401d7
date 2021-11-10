"""
ll1 = LinkedList()
ll2 = LinkedList()
ll1.zip(ll2)


ll1 = LinkedList()
ll2 = LinkedList()
ll3 = LinkedList()
ll3.zip(ll1,ll2)


def zip_lists(ll1, ll2):
    return zipped linked list

"""

from linked_list import LinkedList

def zip_lists(ll1, ll2):
    ll3 = LinkedList() # O(n) space
    current1 = ll1.head
    current2 = ll2.head
    while(current1 and current2):
        # append from ll1
        # append from ll2
        # update currents
        pass
    
    # Check which one still has nodes

def zip_lists_optimal(ll1,ll2):
    ll3 = LinkedList()
    current1 = ll1.head
    current2 = ll2.head
    # ll1 head -> [1] -> [3] -> [2] -> X
    # ll2 head -> [5] -> [9] -> [4] -> X
    # head -> 1 -> 5 -> 3 -> 2-> X
    # temp -> 9 -> 4 -> X
    while (current1 or current2):
        # move every node in ll2 to be after every node in ll1
        pass

