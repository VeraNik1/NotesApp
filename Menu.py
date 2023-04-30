from NotesApplication import NotesApp


class Menu:
    def __init__(self):
        self.notes_app = NotesApp("notes.csv")

    def show(self):
        print("Welcome to Note App!")
        while True:
            print("Choose the option:")
            print("1. Add a new note")
            print("2. Show all notes")
            print("3. Update note's title or description")
            print("4. Delete the note")
            print("5. Find the note")
            print("6. Exit")
            choice = input("Input your choice (1-6): ")
            if choice == "1":
                title = input("Enter the title of your new note: ")
                body = input("Type the description: ")
                self.notes_app.add_note(title, body)
            elif choice == "2":
                self.notes_app.show_notes()
            elif choice == "3":
                id_note = input("Input note's id you'd like to change: ")                 
                title = input("Input new title: ")
                body = input("Type new description: ")
                self.notes_app.edit_note_by_id(int(id_note), title, body)
            elif choice == "4":
                id_note = input("Input id of the note you want to delete: ")
                self.notes_app.delete_note_by_id(int(id_note))
            elif choice == "5":
                id_note = input("Input id of the note you want to find: ")
                print(self.notes_app.find_note_by_id(int(id_note)))
            elif choice == "6":
                print("Have a good day, bye!")
                break
            else:
                print("Incorrect choice. You need to choose numbers from 1 to 6.")