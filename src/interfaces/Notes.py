import pickle
import re
from colorama import Fore, Style


class Notes:
    def __init__(self):
        self.notes = {}  # A dictionary for saving notes.
        self.next_id = 1  # A counter for generating unique IDs for notes

    def add_note(self, content):
        # Adds a new note with the specified content
        note_id = self.next_id
        self.notes[note_id] = content
        self.next_id += 1
        print(f"The note is saved with ID: {note_id}.")

    def edit_note(self, note_id, new_content):
        # Edits an existing note by ID
        if note_id in self.notes:
            self.notes[note_id] = new_content
            print(f"The note with ID {note_id} is updated.")
        else:
            print("The note with this ID is not found.")

    def delete_note(self, note_id):
        # Deletes the note by ID
        if note_id in self.notes:
            del self.notes[note_id]
            print(f"The note with ID {note_id} is deleted.")
        else:
            print("The note with this ID is not found.")

    def show_notes(self):
        # Shows all the notes
        if not self.notes:
            print("There are no notes.")
        else:
            for note_id, content in self.notes.items():
                print(f"ID: {note_id} - {content}")

    def find_note_by_text(self, text):
        # Searches for notes by text
        results = []
        search_term_lower = text.lower()

        for note_id, note_content in self.notes.items():
            if search_term_lower in note_content.lower():
                highlighted_text = re.sub(
                    re.compile(re.escape(text), re.IGNORECASE),
                    lambda match: f"{Fore.YELLOW}{match.group(0)}{Style.RESET_ALL}",
                    note_content
                )
                formatted_note = f"ID: {note_id} - Text: {highlighted_text}"
                results.append(formatted_note)

        if results:
            return "\n".join(results)
        else:
            return f"No notes found with the text '{text}'."


def save_data_notes(book, filename="notesbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)
    print("Data saved.")


def load_data_notes(filename="notesbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("The file is not found. A new notebook has been created.")
        return Notes()