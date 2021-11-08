# Linked List methods

## insert_before(value, new_value)

### Visualization
head -> [1] -> [3] -> [2] -> X
insert_before(3,5)
head -> [1] -> [5] -> [3] -> [2] -> X

### Algorithm


## insert_after

### Visualization
head -> [1] -> [3] -> [2] -> X
insert_after(3,5)
head -> [1] -> [3] -> [5] -> [2] -> X

### Algorithm
- Find the first node that has the value
    - start from head
    - compare nodes values with value
    - whenever you find the value, stop, found
    - otherwise, keep moving by moving the temporary variable (aka current)
- If value not found, raise an error and exit
- Add the new_value node after node that has value
    - save the next of node we found to a temporary variable
    - assign next of the node to the new_node
    - assign next of new_node to temporary variable (originally next of node)
- Exit


### Pseudo code
```
class LinkedList(){
    function insert_after(value, new_value){
        variable current = head-of-this-linked-list
        while (current != null){
            if (current.value == value){
                node = Node(new_value)
                temp = current.next
                current.next = node
                node.next = temp
            }
            current = current.next
        }
        raise Error ("We couldn't find a node that has your value!")
    }
}
```

