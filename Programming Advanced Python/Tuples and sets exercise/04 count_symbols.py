def get_unique_symbols(text):
    symbols_dict = {}
    for symbol in text:
        if symbol not in symbols_dict:
            symbols_dict[symbol] = 0
        symbols_dict[symbol] += 1
    return symbols_dict


def print_results(result):
    for key,value in sorted(result.items()):
        print(f'{key}: {value} time/s')


text = input()

print_results(get_unique_symbols(text))