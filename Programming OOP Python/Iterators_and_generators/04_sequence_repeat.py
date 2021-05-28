from collections import deque


class sequence_repeat:
    def __init__(self,sequence,number):
        self.sequence = deque(sequence)
        self.number = number
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        current_element = self.sequence.popleft()
        while self.counter < self.number:
            self.counter += 1
            self.sequence.append(current_element)
            return current_element
        raise StopIteration()


result = sequence_repeat('abc', 10)
for item in result:
    print(item, end ='')
