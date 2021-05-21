from random import randint


class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return f'[{", ".join(self.data[::-1])}]'


# class Stack2(list):
#     def push(self, value):
#         self.append(value)
#
#     def peek(self):
#         return self[-1]
#
#     def is_empty(self):
#         return len(self) == 0

ll = Stack()
[ll.push(str(randint(0,100))) for _ in range(15)]
print(ll.pop())
print(ll.peek())
print(ll.is_empty())
print(ll)