from .Field import Field

import datetime

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):

        if self.validate_phone(value): 
            super().__init__(value)
        else:
            raise ValueError("Phone number must be exactly 10 digits.")

    @staticmethod
    def validate_phone(value):
        return value.isdigit() and len(value) == 10
    
class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        
class Address(Field):
    def __init__(self, value):
        super().__init__(value)