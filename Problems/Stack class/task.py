class Stack():
    def __init__(self):
        self.elements = []

    def push(self, el):
        self.elements.append(el)

    def pop(self):
        return self.elements.pop()

    def peek(self):
        last_index = len(self.elements) - 1
        return self.elements[last_index]

    def is_empty(self):
        length = len(self.elements)
        return length == 0
