from collections import deque

class Stack:
    def __init__(self):
        self.storage = deque()
    def push(self, value):
        self.storage.append(value)
    def pop(self):
        return self.storage.pop()



class Queue:
    def __init__(self):
        self.storage = deque()
    def enqueue(self, value):
        self.storage.append(value)
    def dequeue(self):
        return self.storage.popleft()


def validate_brackets(text):
    pass