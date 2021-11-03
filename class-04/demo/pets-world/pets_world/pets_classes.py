from abc import ABC, abstractmethod


class Pet():
    counter = 0
    # Constructor method
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Pet.counter += 1
    # Instance method (Default)
    def greet(self):
        return f'Hello my name is {self.name}, I\'m {self.age} months old.'
    
    # Decorator
    @abstractmethod
    def speak(self):
        pass
        # return 'This is a Pet'
    
    @classmethod
    def get_pets_count(cls):
        return cls.counter


class Cat(Pet):
    def __init__(self, name, age, has_hair):
        super().__init__(name, age)
        self.has_hair = has_hair
    def speak(self):
        if self.has_hair:
            return 'Meoooooowwwww! I have hair'
        else:
            return 'Meoooooowwwww! I DO NOT have hair'
    def __str__(self):
        return f"< CAT : {self.name} >"


class Dog(Pet):
    def speak(self):
        return 'Whoooooooffff'

    @staticmethod
    def get_average_age():
        return 7

    def __str__(self):
        return f"< DOG : {self.name} >"
    def __repr__(self):
        return f"<-- This is a dog that has a name {self.name} -->"




if __name__ == "__main__":
    # Instantiation
    oscar = Dog('Oscar', 4) 
    snowy = Cat('Snowy', 8, True)
   
    print(snowy.greet())
    print(snowy.speak())
   
    print(oscar.greet())
    print(oscar.speak())

    print('Calling a static method')
    print(f"Average age for dogs is {oscar.get_average_age()} month OR you can use {Dog.get_average_age()} months.")

    generic_pet = Pet('GP', 1000)
    print(generic_pet.greet())
    print(generic_pet.speak())


    print(Pet.get_pets_count())

    # Str and Repr
    print(oscar)
    print(snowy)

    # Question about Input Validation
    # age = input('Enter your age: ')
    # try:
    #     age = int(age)
    # except ValueError:
    #     print("Age must be an integer!")

