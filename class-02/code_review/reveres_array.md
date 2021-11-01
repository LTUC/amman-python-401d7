"""
1. Problem domain:
  we have an array and we need to reverse it.

2. In/Out:
  In: an array of n elements
  Out: a revered array

3. Visual:
  [7,3,'x',-8] --> [-8,'x',3,7]

4. Big O:

5. Algorithm:
  a. Define a function that recieves and array as an argument.

  b. define a variable i and set the initial value for it to 0

  c. define a variable j and set it to the legnth of the recived array

  d. loop through the array

  e. on each iteration:
      [7,9,6,3,6]
      e.1 swap the elements : 0  <-> len(arr)-1
      e.2 increment i by 1
      e.3 decrement j by 1
  f. stop when we reach the middle

6. Pseudo Code:
  Define fun(arr): 1 time
    Define i=0,  j=len(arr)-1 / 1 time
    while i<j:n/2
      swap arr[i] and arr[j] 1 time
      i++ / 1 time
      j-- / 1 time
    
    return arr 1 time

    O= 1+1+1+ n/2 * (1+1+1)
    O= 3 + n/2*(3)
    O= constant + n/2 * constant
    O(n)

7. Code:
  def reveres_array(arr):
    # [3,'a',9,-33]
    i=0
    j=len(arr)-1

    while i<j:
      # swap
      arr[i],arr[j]=arr[j],arr[i]
      i+=1
      j-=1
    return arr

8. Verification:
In: [4,2,3,99,-14,"k"]
expected output: ["k",-14,99,3,2,4]
i=0
j=6-1=5

while 0<5: #ture
  arr[0],arr[5]=arr[5],arr[0]
  arr=["k",2,3,99,-14,-4]
  i=0+1=1
  j=5-1=4

i=1
j=5-1=4
while 1<4: #ture
  arr[1],arr[4]=arr[4],arr[1]
  arr=["k",-14,3,99,2,-4]
  i = 1+1 = 2
  j=4-1=3
....

i=3
j=3-1=2
while 3<2: #false
  stop the loop

final result=["k",-14,99,3,2,4]
"""
# def reverse_array(arr):
#   return arr[::-1]

"""
  Big O:
  complexity:
    time
    space
"""