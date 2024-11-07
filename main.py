from src.functions.AddressBookFunctions import (
    add_contact, edit_contact, delete_contact, show_all_contacts,
    show_birthday, show_birthdays_future,
    load_data, save_data, parse_input
)
from src.functions.SearchContact import SearchContact  # Імпортуємо SearchContact
from src.interfaces.Notes import load_data_notes, save_data_notes  # Імпортуємо функції для роботи з нотатками
from colorama import init, Fore, Style

init(autoreset=True)

def show_main_help():
    commands = f"""
{Fore.CYAN}Available commands:
{Fore.GREEN}1. contact{Style.RESET_ALL} - Use the contact book.
{Fore.GREEN}2. notes{Style.RESET_ALL} - Use the notes.
{Fore.GREEN}3. help{Style.RESET_ALL} - Show this help message.
{Fore.GREEN}4. close or exit{Style.RESET_ALL} - Save data and close the assistant.
"""
    print(commands)

def show_contact_help():
    commands = f"""
{Fore.CYAN}Contact book commands:
{Fore.GREEN}1. create {Fore.YELLOW}[name] {Fore.YELLOW}[phone] {Fore.YELLOW}[birthday (optional)] {Fore.YELLOW}[address (optional)] {Fore.YELLOW}[email (optional)]{Style.RESET_ALL} - Add a new contact.
{Fore.GREEN}2. edit {Fore.YELLOW}[name] {Fore.YELLOW}[field] {Fore.YELLOW}[new_value]{Style.RESET_ALL} - Add or edit a contact's information (fields: phone, name, email, birthday, address).
{Fore.GREEN}3. del {Fore.YELLOW}[name]{Style.RESET_ALL} - Delete a contact by name.
{Fore.GREEN}4. show-all{Style.RESET_ALL} - Show all contacts in the address book.
{Fore.GREEN}5. show-bday {Fore.YELLOW}[name]{Style.RESET_ALL} - Show the birthday of a specific contact.
{Fore.GREEN}6. show-bdays {Fore.YELLOW}[days]{Style.RESET_ALL} - Show contacts with upcoming birthdays within a specified number of days.
{Fore.GREEN}7. find {Fore.YELLOW}[name]{Style.RESET_ALL} - Find a contact by name.
{Fore.GREEN}8. back{Style.RESET_ALL} - Go back to the main menu.
{Fore.GREEN}9. help{Style.RESET_ALL} - Show this help message.
{Fore.GREEN}10. close or exit{Style.RESET_ALL} - Save data and close the assistant.
"""
    print(commands)

def show_notes_help():
    commands = f"""
{Fore.CYAN}Notes commands:
{Fore.GREEN}1. note-add{Style.RESET_ALL} - Add a note.
{Fore.GREEN}2. note-edit {Style.RESET_ALL} - Edit a note by ID.
{Fore.GREEN}3. note-del {Style.RESET_ALL} - Delete a note by ID.
{Fore.GREEN}4. note-show{Style.RESET_ALL} - Show all notes.
{Fore.GREEN}5. back{Style.RESET_ALL} - Go back to the main menu.
{Fore.GREEN}6. help{Style.RESET_ALL} - Show this help message.
{Fore.GREEN}7. close or exit{Style.RESET_ALL} - Save data and close the assistant.
"""
    print(commands)

def contact_book_mode(book, search_contact):
    show_contact_help()
    while True:
        user_input = input(f"{Fore.BLUE}Enter a contact book command: {Style.RESET_ALL}")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book)
            print(f"{Fore.RED}Good bye!{Style.RESET_ALL}")
            exit()

        elif command == "back":
            show_main_help()
            break

        elif command == "help":
            show_contact_help()

        elif command == "create":
            print(add_contact(args, book))  
        
        elif command == "edit":
            print(edit_contact(args, book))
        
        elif command == "del":
            print(delete_contact(args, book))

        elif command == "show-all":
            print(show_all_contacts(book))

        elif command == "show-bday":
            if not args:
                print(f"{Fore.RED}Not enough arguments. Usage: show-bday [name]{Style.RESET_ALL}")
                continue
            print(show_birthday(args, book))
        
        elif command == "show-bdays":
            if not args:
                print(f"{Fore.RED}Not enough arguments. Usage: show-bdays [days]{Style.RESET_ALL}")
                continue
            print(show_birthdays_future(args, book))

        elif command == "find":
            if not args:
                print(f"{Fore.RED}Not enough arguments. Usage: find [name]{Style.RESET_ALL}")
                continue
            print(search_contact.find_contact_by_name(args[0]))

        else:
            print(f"{Fore.RED}Invalid command. Type 'help' to see the list of available commands.{Style.RESET_ALL}")

def notes_mode(notes):
    show_notes_help()
    while True:
        command = input(f"{Fore.BLUE}Enter a notes command: {Style.RESET_ALL}").strip().lower()

        if command in ["close", "exit"]:
            save_data_notes(notes)
            print(f"{Fore.RED}Good bye!{Style.RESET_ALL}")
            exit()

        elif command == "back":
            show_main_help()
            break

        elif command == "help":
            show_notes_help()

        elif command == "note-add":
            content = input("Enter note content: ").strip()
            if content:
                notes.add_note(content)
            else:
                print(f"{Fore.RED}Note content cannot be empty.{Style.RESET_ALL}")

        elif command == "note-edit":
            try:
                note_id = int(input("Enter note ID to edit: ").strip())
                new_content = input("Enter new content: ").strip()
                if new_content:
                    notes.edit_note(note_id, new_content)
                else:
                    print(f"{Fore.RED}New content cannot be empty.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Invalid ID format. Please enter a number.{Style.RESET_ALL}")

        elif command == "note-del":
            try:
                note_id = int(input("Enter note ID to delete: ").strip())
                notes.delete_note(note_id)
            except ValueError:
                print(f"{Fore.RED}Invalid ID format. Please enter a number.{Style.RESET_ALL}")

        elif command == "note-show":
            notes.show_notes()

        else:
            print(f"{Fore.RED}Unknown command. Try again.{Style.RESET_ALL}")

def main():
    book = load_data()
    notes = load_data_notes()
    search_contact = SearchContact(book)  # Створюємо екземпляр класу SearchContact
    print(f"{Fore.YELLOW}Welcome to the assistant bot!{Style.RESET_ALL}")
    show_main_help()

    try:
        while True:
            user_input = input(f"{Fore.BLUE}Enter a command: {Style.RESET_ALL}").strip().lower()

            if user_input in ["close", "exit"]:
                save_data(book)
                save_data_notes(notes)
                print(f"{Fore.RED}Good bye!{Style.RESET_ALL}")
                break

            elif user_input == "help":
                show_main_help()

            elif user_input == "contact":
                contact_book_mode(book, search_contact)

            elif user_input == "notes":
                notes_mode(notes)

            else:
                print(f"{Fore.RED}Invalid command. Type 'help' to see the list of available commands.{Style.RESET_ALL}")

    except KeyboardInterrupt:
        save_data(book)
        save_data_notes(notes)
        print(f"\n{Fore.RED}Program interrupted by user. Data saved. Exiting gracefully.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()