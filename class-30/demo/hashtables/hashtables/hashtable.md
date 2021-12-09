# How to access the data in a Hashtable?

- data
- key 
- hashtable(key)=>data

## to insert data to a hashtable

- data
- generate a key from the data
- insert the data hashtable(data)

## Hashing
- Used to generate/ determin a memory location from the key
- Hash key:
  - Deterministic : input determines the output
  - Not Random : Same key will always produce the same hash

# How hashing works?
asccii code = >

- converting a key to a memory location 
- memory location can be represented as an index of an array
- we have to set the size of the array or provide a default value of the array

```python
def hash(key):
    size = 1024 #1kb
    name = "Ahmad"
    map=[None]*size
    map=[[]]*size
    value = 26
    sum_of_asccii = 65+104+109+97+100
    temp_value = 475*13 #==>6175
    index = temp_value%size #6175%1024 31
    return index
# ######################
# Insert data to the map
hash("Ahmad")
26 --> map[31]
########################
#Access
map=[none,none]
index=hash("Ahmad")
return map[index]
```