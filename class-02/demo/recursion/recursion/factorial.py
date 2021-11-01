

def fact(n):
    # base case
    if n <= 1:
        return 1
    #  general case

    return n*fact(n-1)

"""
fact(5)
    5 <= 1 ? 
    5*fact(5-1):
        4 <= 1 ?
        4*fact(4-1):
            ...
            3*fact(3-1):
                ...
                2*fact(2-1):
                    fact(1)=1

"""