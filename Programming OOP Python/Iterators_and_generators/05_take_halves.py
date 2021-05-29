def solution():
    def integers():
        first_int = 1
        while True:
            yield first_int
            first_int += 1

    def halves():
        for i in integers():
            half = i / 2
            yield half

    def take(n, seq):
        counter = 0
        my_list = []
        for num in seq:
            if counter == n:
                return my_list
            my_list.append(num)
            counter += 1

    return (take, halves, integers)

take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

