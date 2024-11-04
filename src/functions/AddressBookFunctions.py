from src.interfaces.AddressBook import AddressBook
from src.interfaces.Record import Record
from src.interfaces.Contact import Birthday


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
        raise ValueError("Not enough arguments. Usage: add [name] [phone]")
    name, phone, *rest = args
    birthday = rest[0] if rest else None

    if birthday:
        try:
            Birthday(birthday)
        except ValueError as e:
            return f'Failed to add contact. {e}'
    
    record = book.find(name)
    message = "Contact updated."

    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
        
    if birthday:
        try:
            record.add_birthday(birthday)
        except ValueError as e:
            return f'Failed to add contact. {e}'
    if phone:
        record.add_phone(phone)

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
    parts = user_input.split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args
