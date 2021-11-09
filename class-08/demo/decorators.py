
def my_decorator(func,):
    def _warpper(*args, **kwargs):
        print("=============")
        func(*args, **kwargs)
        print("=============")

    return _warpper

@my_decorator
def say_hello(name, age):
    return (f"hello my name is {name}, Im {age} old")

@my_decorator
def say_goodbye(name):
    print(f"Goodbye {name}")

if __name__ == "__main__":
    print(say_hello("Ahmad",25))
    say_goodbye("Ahmad")