from src.interfaces.AddressBook import AddressBook
from src.functions.AddressBookFunctions import add_contact, add_birthday, show_birthday, birthdays, parse_input


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            if len(args) < 3:
                print("Not enough arguments. Usage: change [name] [old_phone] [new_phone]")
                continue
            name, old_phone, new_phone = args
            record = book.find(name)
            if record:
                if record.edit_phone(old_phone, new_phone):
                    print(f"Phone number for {name} updated.")
                else:
                    print("Failed to update phone number.")
            else:
                print(f"Contact {name} not found.")
        elif command == "phone":
            if not args:
                print("Not enough arguments. Usage: phone [name]")
                continue
            name, *_ = args
            record = book.find(name)
            if record:
                print(f"{name}'s phone numbers: {', '.join(phone.value for phone in record.phones)}")
            else:
                print(f"Contact {name} not found.")

        elif command == "all":
            for name, record in book.data.items():
                print(record)

        elif command == "add-birthday":
            if len(args) < 2:
                print("Not enough arguments. Usage: add-birthday [name] [birthday]")
                continue
            print(add_birthday(args, book))


        elif command == "show-birthday":
            if not args:
                print("Not enough arguments. Usage: show-birthday [name]")
                continue
            print(show_birthday(args, book))


        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()