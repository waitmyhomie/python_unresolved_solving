from src.interfaces.AddressBook import AddressBook
from src.interfaces.Record import Record
from src.interfaces.Contact import Birthday, Email, Name
import pickle
from datetime import datetime, timedelta
import shlex    
def input_error(handler):
    def wrapper(*args, **kwargs):
        try:
            return handler(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            return str(e)
    return wrapper

@input_error
def add_contact(args, book: AddressBook):
    if len(args) < 2:
        raise ValueError("Not enough arguments. Usage: add [name] [phone] [birthday (optional)] [address (optional)] [email (optional)]")
    
    # Parsing the arguments
    name, phone, *rest = args
    birthday = rest[0] if len(rest) > 0 else None
    address = rest[1] if len(rest) > 1 else None
    email = rest[2] if len(rest) > 2 else None

    # Validate and process each field
    if birthday:
        try:
            Birthday(birthday)
        except ValueError as e:
            return f"Failed to add contact. {e}"

    if email:
        if not Email.validate_email(email):
            return "Failed to add contact. Invalid email format."

    # Search and update or create new record
    record = book.find(name)
    message = "Contact updated." if record else "Contact added."

    if record is None:
        record = Record(name)
        book.add_record(record)

    # Add fields to the record if provided
    if birthday:
        try:
            record.add_birthday(birthday)
        except ValueError as e:
            return f"Failed to add contact. {e}"
    
    if phone:
        record.add_phone(phone)

    if address:
        record.add_address(address)
    
    if email:
        record.add_email(email)

    return message

@input_error
def add_birthday(args, book):
    name, birthday, *_ = args
    record = book.find(name)
    if record is None:
        return f"Contact {name} not found."
    record.add_birthday(birthday)
    return f"Birthday added for contact {name}."

# refactor need to get a parameter in days in get_upcoming_birthdays method
@input_error
def show_birthday(args, book):
    name, *_ = args
    record = book.find(name)
    if record is None:
        return f"Contact {name} not found."
    if record.birthday:
        return f"{name}'s birthday is on {record.birthday.value.strftime('%d.%m.%Y')}"
    else:
        return f"Birthday for contact {name} is not set."

#  refactor need to get a parameter in days in get_upcoming_birthdays method

@input_error
def birthdays(args, book):
    upcoming_birthdays = book.get_upcoming_birthdays()
    if not upcoming_birthdays:
        return "No upcoming birthdays in the next week."
    result = "Upcoming birthdays:\n"
    for record in upcoming_birthdays:
        result += f"{record.name.value} on {record.birthday.value.strftime('%d.%m.%Y')}\n"
    return result

def parse_input(user_input):
    parts = shlex.split(user_input)
    command = parts[0].lower()
    args = parts[1:]
    return command, args

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()
    
@input_error
def show_birthdays_future(args, book):
    if not args:
        raise ValueError("Not enough arguments. Usage: show-birthdays-future [days]")
    
    days = int(args[0]) 
    today = datetime.today().date()
    future_date = today + timedelta(days=days)

    upcoming_birthdays = []

    for record in book.data.values():
        if record.birthday:
          
            next_birthday = record.birthday.value.date().replace(year=today.year)
            if next_birthday < today:
                next_birthday = next_birthday.replace(year=today.year + 1)

           
            if today <= next_birthday <= future_date:
                days_until_birthday = (next_birthday - today).days
      
                upcoming_birthdays.append(
                    f"{record}\nNext birthday: {next_birthday.strftime('%d.%m.%Y')} ({days_until_birthday} days)"
                )

    if upcoming_birthdays:
        return "Upcoming birthdays:\n" + "\n\n".join(upcoming_birthdays)
    else:
        return f"No birthdays in the next {days} days."

def edit_contact(args, book):
    if len(args) < 3:
        return "Not enough arguments. Usage: edit [name] [field] [new_value]"

    name, field, new_value = args
    record = book.find(name)

    if not record:
        return f"Contact {name} not found."

    if field == "phone":
        old_phone, new_phone = new_value.split(",")
        return record.edit_phone(old_phone, new_phone)
    elif field == "name":
        record.name = Name(new_value)
        return f"Name changed to {new_value}."
    elif field == "email":
        return record.change_email(new_value)
    elif field == "birthday":
        return record.edit_birthday(new_value)
    elif field == "address":
        return record.edit_address(new_value)
    else:
        return f"Field {field} not recognized."

def delete_contact(args, book):
    if not args:
        return "Not enough arguments. Usage: delete [name]"
    
    name = args[0]
    record = book.find(name)
    if record:
        book.remove_record(name)
        return f"Contact {name} deleted."
    else:
        return f"Contact {name} not found."

def show_all_contacts(book):
    if not book.data:
        return "No contacts found."
    
    return "\n".join(str(record) for record in book.data.values())