def singleton(cls):
    instance = None

    def wrapper(*args, **kwargs):
        nonlocal instance
        if not instance:
            instance = cls(*args, **kwargs)
        return instance

    return wrapper


class JsonParser:
    def parse(self, obj):
        return f'json: {str(obj)}'


@singleton
class JsonParser2:
    def parse(self, obj):
        return f'json: {str(obj)}'

# print(JsonParser())
# print(JsonParser())
#
# print(JsonParser2())
# print(JsonParser2())

jp1 = JsonParser()
jp2 = JsonParser()
jp3 = JsonParser2()
jp4 = JsonParser2()
print(jp1)
print(jp2)
print(jp3)
print(jp4)



