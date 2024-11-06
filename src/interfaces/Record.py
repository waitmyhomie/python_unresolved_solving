from src.interfaces.Contact import Email, Name, Phone, Birthday,Address
from datetime import datetime

class Record:
    def __init__(self, name):
        self.name = Name(name)
        # refactor to use a list of phones
        self.phones = None
        self.birthday = None
        self.address = None
        self.email = None

    def add_phone(self, phone_number):
        self.phones = Phone(phone_number)
   

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return f"Phone {phone_number} removed."
        return f"Phone {phone_number} not found."

    def edit_phone(self,new_phone):
        self.phones.value = new_phone
        return f"Phone changed to {new_phone}."
    
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
    
    def add_email(self, email):
        self.email = Email(email)
    
    def change_email(self, new_email):
        self.email.value = new_email
        return f"Email changed to {new_email}."
    
    def delete_email(self):
        del self.email
        return "Email deleted."

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
            phones = self.phones.value
            birthday = ""
            if self.birthday:
                birthday = f", birthday: {self.birthday.value.strftime('%d.%m.%Y')}"  
            address = f", address: {self.address.value}" if self.address else ""
            email = f", email: {self.email.value}" if self.email else ""
            
            return f"Contact name: {self.name.value}, phone: {phones}{birthday}{address}{email}"