import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class JsonParser:
    def parse(self, obj):
        return json.dumps(obj.__dict__)


class CsvParser:
    def parse(self, obj):
        result = [
            ', '.join(obj.__dict__.keys()),
            ', '.join(str(x) for x in (obj.__dict__.values()))
        ]
        return '\n'.join(result)


class StringParser:
    def parse(self, obj):
        return str(obj)


class ParserFactory:
    def get(self, format):
        if format == 'json':
            result = JsonParser()
        elif format == 'csv':
            result = CsvParser()
        else:
            result = StringParser()
        return result


person = Person('Pesho', 11)
format = input()
parser_factory = ParserFactory()
parser = parser_factory.get(format)
print(parser.parse(person))