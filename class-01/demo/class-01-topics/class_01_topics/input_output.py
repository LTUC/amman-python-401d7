def in_n_out():
    name = input("What's your name?  ")
    age = input("How old are you?  ")
    print(format_my_text(name, age))

def format_my_text(name, age):
    """
    This function is used to format a good looking text
    that includes name and age of a person.

    Input:
        name: string 
        age: integer
    
    Output:
        returns a fromatted text of the original sentence including name and age
        example: My name is Ahmad and I am 25 years old.
    """
    # way 1: using format
    # return "My name is {} and I am {} years old.".format(name, age)

    # way 2: concatenation
    # return "My name is "+str(name)+" and I am "+str(age)+" years old."

    # way 3: formatted string (BEST WAY)
    return f"My name is {name} and I am {age} years old."

    # way 4: using % - coming from python 2
    # return "My name is %s and I am %d years old."%(name, age)


if __name__=="__main__":
    # format_my_text("Ahmad", 25)
    # print(help(input))
    # print(help(format_my_text))
    # print(format_my_text('Yahia', 23))
    print("Hi from input_ouput.py to the shell")
    in_n_out()