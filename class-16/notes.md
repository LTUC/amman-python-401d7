# Notes

## Sentiment Analysis
```python
review1 = "I didn't like the food"
review2 = "I feel sick"
review3 = "The food is amazing"
review4 = "wow! What a great experience"
```

## Nested functions (Closure)

### What?
Function inside another function

### Why?
- Keep the value of variable for the current call
- Single Responsibility Priciple:
    - Outer function: initialization and global variables (local to outer but global to inner)
    - Inner function: recursion

### How?
```python

def outer(*args):
    # initialize some variables (Global to inner but Local to outer)
    def inner(*args):
        # Functionality - In general
        #   Base case
        #   Maniplulate global variables if needed
        #   Recursive call
    # Call the inner function
    #   Updates the global variables
    
    # Call the function and return immediatelly
    #   e.g. return n * fact(n-1)
    
```