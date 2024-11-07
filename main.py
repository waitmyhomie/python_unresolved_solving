from src.functions.AddressBookFunctions import (
    add_contact, edit_contact, delete_contact, show_all_contacts,
    show_birthday, show_birthdays_future,
    load_data, save_data, parse_input
)
from src.functions.SearchContact import SearchContact  # Імпортуємо SearchContact
from colorama import init, Fore, Style

init(autoreset=True)

def show_help():
    commands = f"""
{Fore.CYAN}Available commands:
{Fore.GREEN}1. create {Fore.YELLOW}[name] {Fore.YELLOW}[phone] {Fore.YELLOW}[birthday (optional)] {Fore.YELLOW}[address (optional)] {Fore.YELLOW}[email (optional)]{Style.RESET_ALL} - Add a new contact.
{Fore.GREEN}2. edit {Fore.YELLOW}[name] {Fore.YELLOW}[field] {Fore.YELLOW}[new_value]{Style.RESET_ALL} - Add or edit a contact's information (fields: phone, name, email, birthday, address).
{Fore.GREEN}3. del {Fore.YELLOW}[name]{Style.RESET_ALL} - Delete a contact by name.
{Fore.GREEN}4. show-all{Style.RESET_ALL} - Show all contacts in the address book.
{Fore.GREEN}5. show-bday {Fore.YELLOW}[name]{Style.RESET_ALL} - Show the birthday of a specific contact.
{Fore.GREEN}6. show-bdays {Fore.YELLOW}[days]{Style.RESET_ALL} - Show contacts with upcoming birthdays within a specified number of days.
{Fore.GREEN}7. help{Style.RESET_ALL} - Show this help message.
{Fore.GREEN}8. close or exit{Style.RESET_ALL} - Save data and close the assistant.
{Fore.GREEN}9. find {Fore.YELLOW}[name]{Style.RESET_ALL} - Find a contact by name.
"""
    print(commands)

def main():
    book = load_data()
    search_contact = SearchContact(book)  # Створюємо екземпляр класу SearchContact
    print(f"{Fore.YELLOW}Welcome to the assistant bot!{Style.RESET_ALL}")
    show_help()  

    try:
        while True:
            user_input = input(f"{Fore.BLUE}Enter a command: {Style.RESET_ALL}")
            command, args = parse_input(user_input)

            if command in ["close", "exit"]:
                save_data(book)
                print(f"{Fore.RED}Good bye!{Style.RESET_ALL}")
                break

            elif command == "help":
                show_help()

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

            elif command == "find": #команда пошуку контактів
                if not args:
                    print(f"{Fore.RED}Not enough arguments. Usage: find [name]{Style.RESET_ALL}")
                    continue
                print(search_contact.find_contact_by_name(args[0]))

            else:
                print(f"{Fore.RED}Invalid command. Type 'help' to see the list of available commands.{Style.RESET_ALL}")

    except KeyboardInterrupt:
        save_data(book)
        print(f"\n{Fore.RED}Program interrupted by user. Data saved. Exiting gracefully.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
