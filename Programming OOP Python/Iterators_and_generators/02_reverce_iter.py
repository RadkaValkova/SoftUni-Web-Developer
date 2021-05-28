class reverse_iter:
    def __init__(self, ll):
        self.ll = ll
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index -= 1
        if abs(self.index) <= len(self.ll):
            current_num = self.ll[self.index]
            return current_num
        raise StopIteration

# class reverse_iter:
#     def __init__(self, ll):
#         self.ll = ll
#
#     def __iter__(self):
#         return reversed(self.ll)

# class reverse_iter:
#     def __init__(self, ll):
#         self.ll = list(ll)
#         self.index = len(self.ll) - 1
#
#     def __iter__(self):
#         return reversed(self.ll)
#     def __next__(self):
#         if self.index < 0:
#             raise StopIteration
#         value = self.ll[self.index]
#         self.index -= 1
#         return value


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
