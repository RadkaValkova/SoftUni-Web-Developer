class vowels:
    def __init__(self, some_string):
        self.some_string = some_string
        self.vowels = ['a','e','i','u','o','y']
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.some_string):
            current_symbol = self.some_string[self.index]
            self.index += 1
            if current_symbol.lower() in self.vowels:
                return current_symbol
        raise StopIteration()

# solution with generator
# def vowels(text):
#     vowels = ['a','e','i','u','o','y']
#     for ch in text:
#         if ch in vowels:
#             yield ch

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
