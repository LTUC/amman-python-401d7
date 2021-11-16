from queue import Queue

class Dog:
    pass

class Cat:
    pass


class AnimalShelter:
    def __init__(self):
        self.cats = Queue()
        self.dogs = Queue()
        self.animals = Queue()

    def dequeue(self, pref):
        if not pref:
            animal = self.animals.dequeue()
            # Also dequeue from cats or dogs
            if type(animal)is Dog:
                self.dogs.dequeue()
            return animal
        if pref == 'cat':
            cat = cats.dequeue()
            # Also dequeue from cats
            return cat
        if pref == 'dog':
            dog = dogs.dequeue()
            # Also dequeue from dogs
            return dog
    def enqueue(self, animal):
        if type(animal) == Dog:
            self.dogs.enqueue(animal)
            self.animals.enqueue(animal)
        else:
            self.cats.enqueue(animal)
            self.animals.enqueue(animal)


