from src.interfaces.Contact import Name, Phone, Birthday,Address
import datetime


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.address = None

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return f"Phone {phone_number} removed."
        return f"Phone {phone_number} not found."

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return f"Phone {old_phone} changed to {new_phone}."
        return f"Phone {old_phone} not found."
    
    def add_address(self, address):
        self.address = Address(address)

    def edit_address(self, new_address):
        self.address.value = new_address
        return f"Address changed to {new_address}."
    
    def delete_address(self):
        del self.address
        return "Address deleted."

    def add_birthday(self, birthday_date):
        self.birthday = Birthday(birthday_date)

    def edit_birthday(self, new_birthday):
        self.birthday.value = new_birthday
        return f"Birthday changed to {new_birthday}."
    
    def delete_birthday(self):
        del self.birthday
        return "Birthday deleted." 

    # refactor to use value + date.today for searching next birthday with a value
    def days_to_birthday(self,value):
        if not self.birthday:
            return None
        today = datetime.today().date()
        next_birthday = self.birthday.value.replace(year=today.year)
        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)
        return (next_birthday - today).days
    
    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        birthday = f", birthday: {self.birthday}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {phones}{birthday}"