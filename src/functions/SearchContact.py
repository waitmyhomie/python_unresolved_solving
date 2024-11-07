from src.interfaces.AddressBook import AddressBook
from src.interfaces.Record import Record
from src.functions.AddressBookFunctions import input_error  # Імпортуємо декоратор з AddressBookFunctions.py 
from colorama import Fore, Style
import re

class SearchContact:
    def __init__(self, address_book):
        self.address_book = address_book   
    
    @input_error  # Додаємо декоратор для обробки помилок
    def find_contact_by_name(self, name):
        results = []
        search_term_lower = name.lower()  # Робимо введений термін пошуку в нижньому регістрі

        for record in self.address_book.data.values():
            contact_name = record.name.value

            # Перевіряємо, чи введений термін міститься в імені контакту (незалежно від регістру)
            if search_term_lower in contact_name.lower():
                # Використовуємо регулярний вираз з прапором re.IGNORECASE для підсвічування
                highlighted_name = re.sub(
                    re.compile(re.escape(name), re.IGNORECASE),  # Ігнорування регістру під час пошуку
                    lambda match: f"{Fore.YELLOW}{match.group(0)}{Style.RESET_ALL}",  # Підсвічуємо знайдену частину з оригінальним регістром
                    contact_name
                )

                # Форматуємо запис для виведення з підсвіченим ім'ям
                formatted_record = str(record).replace(contact_name, highlighted_name)
                results.append(formatted_record)

        # Повертаємо всі знайдені контакти або повідомлення про відсутність
        if results:
            return "\n".join(results)
        else:
            return f"No contacts found with the name '{name}'."