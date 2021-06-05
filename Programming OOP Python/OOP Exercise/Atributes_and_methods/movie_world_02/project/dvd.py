from datetime import datetime

class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        day, month, year = date.split('.')
        x = datetime(int(year), int(month), int(day))
        creation_year = int(year)
        creation_month = x.strftime('%B')
        return cls(name, id, creation_year, creation_month,age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has " \
               f"age restriction {self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"