import time


def exec_time(fn):
    def wrapper(*args):
        start_time = time.time()
        res = fn(*args)
        end_time = time.time()
        return end_time - start_time
    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total
print(loop(1, 10000000))
