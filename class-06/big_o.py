# Big O
# Complexity


"""
To calculate Big O you need to go through every single (excutable)line of code and calculate how much time/space it takes.
- Calculate against number of items
- So no actual time (no seconds), and no actual space (no KBites)
- For lists, always call number of items (n) - but you can use n,m, etc.
"""


def compare(a, b):
    """
    This function compares the two arrays of things and returns the common vlaues in both arrays
    in a tuple format

    Input: Two lists of things
    Output: A tuple of common vlaues (things)
    """
    output = [] # 1 ops
    # Sol 1: O(n^2)
    for i in a: # n ops
        for j in b: # m ops
            if i==j:
                output.append(i)
                break
    
    # Sol 2: O(n^2)
    for i in a: # n ops
        if i in b: # m ops
            output.append(i) # 1 ops
    

    # Sol 3: O(n+m) = O(n)
    # convert the list into a set
    # Why? Searching a set is O(1)
    c = set(b) # m ops {7,9,12,True,'401','56'}
    for i in a: # n ops
        if i in c: # 1 ops
            output.append(i) # 1 ops


    # people = {'moh':25, 'Haia':23, 'Trad':24}
    # if 'Trad' in people:
    #     print(people['Trad'])

    return tuple(output) # n ops


if __name__=="__main__":
    a = ['56',4,5,7.8,'hi',False]
    b = [7,9,12,True,'401','56']
    output = compare(a,b)
    print(output)
    # ('56', True)


