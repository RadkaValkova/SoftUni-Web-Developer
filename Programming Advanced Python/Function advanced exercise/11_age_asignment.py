def age_assignment(*args, **kwargs):
    # result = {}
    # for arg in args:
    #     for key,value in kwargs.items():
    #         if arg[0] == key:
    #             result[arg] = kwargs[key]
    # return result
    return {arg: kwargs[arg[0]] for arg in args}


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))