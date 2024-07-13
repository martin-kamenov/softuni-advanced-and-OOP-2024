import calendar

class DVD:

    def __init__(self, name: str, id_: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id_
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id_: int, name: str, date: str, age_restriction: int) -> 'DVD':
        day, month, year = date.split('.')
        month = calendar.month_name[int(month)]

        return cls(name, id_, int(year), month, age_restriction)

    def __repr__(self):
        return (f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) "
                f"has age restriction {self.age_restriction}. "
                f"Status: {'' if self.is_rented else 'not '}rented")
