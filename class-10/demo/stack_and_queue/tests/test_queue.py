from stack_and_queue.queue import Queue

# test is_empty
# test enqueue
# test dequeue
# test front
# test rear
# test peek

# 1
# 2
# 'Python'

def test_is_empty():
    """
    Testing is_empty method for a queue
    """
    queue=Queue()
    expected=True
    actual= queue.is_empty()
    assert expected == actual

def test_enqueue():
    """
    Testing enqueue method for a queue
    """
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue("Python")
    expected="Python"
    actual=queue.rear.value

    assert expected == actual


