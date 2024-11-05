from src.functions.AddressBookFunctions import (
    add_contact, edit_contact, delete_contact, show_all_contacts,
    add_birthday, show_birthday, show_birthdays_future,
    load_data, save_data, parse_input
)

def show_help():
    commands = """
Available commands:
1. create [name] [phone] [birthday (optional)] [address (optional)] [email (optional)] - Add a new contact.
2. edit [name] [field] [new_value] - Edit a contact's information (fields: phone, name, email, birthday, address).
3. delete [name] - Delete a contact by name.
4. show-all-contacts - Show all contacts in the address book.
5. add-birthday [name] [birthday] - Add a birthday to a contact.
6. show-birthday [name] - Show the birthday of a specific contact.
7. show-birthdays [days] - Show contacts with upcoming birthdays within a specified number of days.
8. help - Show this help message.
9. close or exit - Save data and close the assistant.
"""
    print(commands)

def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    show_help()  # Display commands at startup

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book)
            print("Good bye!")
            break

        elif command == "help":
            show_help()

        # Контакты
        elif command == "create":
            print(add_contact(args, book))
        
        elif command == "edit":
            print(edit_contact(args, book))
        
        elif command == "delete":
            print(delete_contact(args, book))

        elif command == "show-all-contacts":
            print(show_all_contacts(book))

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
        
        elif command == "show-birthdays":
            if not args:
                print("Not enough arguments. Usage: show-birthdays [days]")
                continue
            print(show_birthdays_future(args, book))

        else:
            print("Invalid command. Type 'help' to see the list of available commands.")

if __name__ == "__main__":
    main()
