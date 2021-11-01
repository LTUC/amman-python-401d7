
def is_fizz_buzz(val):
    """
    A function will check if a number is divisible by 3 or 5 or both or none
    """
    if val%3 == 0 and val%5 == 0:
        return 'fizz buzz'

    if val%3 == 0:
        return 'fizz'
    
    if val%5 == 0:
        return 'buzz'
    
    return val
    
