import pickle


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
                print("Notes:")
                print(f"ID: {note_id} - {content}")


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