import random

# Generate random number in Python

def randomize():
    """
    Generate random numbers between 1 and 6
    """
    return random.randint(1,6)
    # Aternatively: int(random.random()*6+1)


if __name__=="__main__":
    print(randomize())