class Calculator:

    @staticmethod
    def add(n,*args):
        result = n
        for i in range(len(args)):
            result += args[i]
        return result

    @staticmethod
    def multiply(n,*args):
        result = n
        for i in range(len(args)):
            result *= args[i]
        return result

    @staticmethod
    def divide(n, *args):
        result = n
        for i in range(len(args)):
            result /= args[i]
        return result

    @staticmethod
    def subtract(n,*args):
        result = n
        for i in range(len(args)):
            result -= args[i]
        return result


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
