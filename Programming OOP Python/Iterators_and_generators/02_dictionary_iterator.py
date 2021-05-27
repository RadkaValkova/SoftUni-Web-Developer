class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.counter = 0
        self.item = [el for el in dictionary.items()]

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.dictionary):
            current_item = self.item[self.counter]
            self.counter += 1
            return current_item
        raise StopIteration()


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
