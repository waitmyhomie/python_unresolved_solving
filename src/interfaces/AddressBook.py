
from datetime import datetime, timedelta
from collections import UserDict

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return True
        print("Record not found.")
        return False

    def get_upcoming_birthdays(self, days=7):
        upcoming_birthdays = []
        today = datetime.now()
        next_week = today + timedelta(days=days)
        for record in self.data.values():
            if record.birthday:
                birthday_this_year = record.birthday.value.replace(year=today.year)
                if today <= birthday_this_year <= next_week:
                    upcoming_birthdays.append(record)
        return upcoming_birthdays
