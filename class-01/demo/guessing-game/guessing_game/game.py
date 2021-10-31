"""
Let's create the classic guessing game I Spy. We'll need...
- A list of things to guess
  - Each thing should be a dictionary with name and hints attributes
  - name is a string
  - hints is a list of strings
"""

things = [
    {
        "name": "clock",
        "hints": [
            "bigger than a bread box",
            "rectangular",
            "tells you something",
            "changes frequently",
        ],
    },
    {
        "name": "chair",
        "hints": [
            "has multiple legs",
            "has a restful interface",
            "not used in stand up meetings",
            "avoid electric ones",
        ],
    },
]


def guess_a_thing(riddle_index):

    thing = things[riddle_index] # Dictionary that represents the thing

    success = False

    guess = input("I spy with my little eye... ")

    hints = thing["hints"]

    correct_answer = thing["name"]

    while len(hints):

        if guess == correct_answer:
            success = True
            break

        hint = hints.pop(0)
        
        print(f"Nope, but here's a hint - {hint}")

        guess = input("I spy with my little eye... ")

    if success or guess == correct_answer:
        print("Crushed it")
    else:
        print(f"Too bad. It's a {correct_answer}")

def play():
    riddle_index = 0

    response = ""
    while response != "n":
        guess_a_thing(riddle_index)
        riddle_index += 1
        if riddle_index > 1: # Play twice only
            break
        response = input("Wanna play?")

    print("Thanks for playing!")


if __name__ == "__main__":
    play()
