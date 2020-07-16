"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as
few lines as possible.
Make sure you pass the test cases too!"""

class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)
        head = self.storage[-1]
        pass

    def peek(self):
        return self.storage[-1]
        pass

    def dequeue(self):
        if len(self.storage)==0:
            return None

        temp=self.storage[0]
        self.storage=self.storage[1:]
        pass