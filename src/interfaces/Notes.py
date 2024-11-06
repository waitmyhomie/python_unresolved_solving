import pickle


class PersonalAssistantNotes:
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


def save_data(book, filename="notesbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)
    print("Data saved.")


def load_data(filename="notesbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("The file is not found. A new notebook has been created.")
        return PersonalAssistantNotes()


def main():

    book = load_data()

    while True:
        command = (
            input("\nEnter command (add, edit, delete, show, exit): ").strip().lower()
        )

        if command == "add":
            content = input("Enter note content: ").strip()

            if content:
                book.add_note(content)
            else:
                print("Note content cannot be empty.")

        elif command == "edit":
            try:
                note_id = int(input("Enter note ID to edit: ").strip())
                new_content = input("Enter new content: ").strip()

                if new_content:
                    book.edit_note(note_id, new_content)
                else:
                    print("New content cannot be empty.")
            except ValueError:
                print("Invalid ID format. Please enter a number.")

        elif command == "delete":
            try:
                note_id = int(input("Enter note ID to delete: ").strip())
                book.delete_note(note_id)
            except ValueError:
                print("Invalid ID format. Please enter a number.")

        elif command == "show":
            print("Notes:")
            book.show_notes()

        elif command == "exit":
            save_data(book)
            print("Exiting the program.")
            break

        else:
            print("Unknown command. Try again.")


if __name__ == "__main__":
    main()

