def concatenate(*args):
    result = ''
    for i in range(len(args)):
        result += args[i]
    return result


print(concatenate("Soft", "Uni", "Is", "Great", "!"))