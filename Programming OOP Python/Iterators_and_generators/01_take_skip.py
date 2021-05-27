class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.start = 0
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        current_start = self.start
        if self.counter < self.count:
            self.start += self.step
            self.counter += 1
            return current_start
        raise StopIteration


numbers = take_skip(10, 5)
for number in numbers:
    print(number)
