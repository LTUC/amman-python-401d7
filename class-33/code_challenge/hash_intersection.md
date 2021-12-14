# Hashmap tree intersect

- create a hashtable based on one of the trees bt1 o(n)
- define an empty array o(n)
- check if one or both of the trees is empty
- we traverse the second tree o(n):
  - hash each node and get the key of each node
  - then access the location of this key and compare values
  - if match => append to the empty array