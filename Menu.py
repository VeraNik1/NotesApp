from NotesApplication import NotesApp


class Menu:
    def __init__(self):
        self.notes_app = NotesApp("notes.csv")

    def show(self):
        print("Welcome to Noteы App!")
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
                title = input("Enter title of your new note: ")
                body = input("Type description: ")
                self.notes_app.add_note(title, body)
            elif choice == "2":
                self.notes_app.show_notes()
            elif choice == "3":
                id_note = input("Input note's id you'd like to change: ")
                if self.notes_app.find_note_by_id(id_note):                 
                    title = input("Input a new title: ")
                    body = input("Type a new description: ")
                    self.notes_app.edit_note_by_id(id_note, title, body)
                else: print(f"Note id{id_note} hasn't been found")
            elif choice == "4":
                id_note = input("Input id of the note you want to delete: ")
                self.notes_app.delete_note_by_id(id_note)
            elif choice == "5":
                print("1. Find the note by id")
                print("2. Find the note by text from title or description")
                find_choice = input()
                if find_choice == "1":
                    id_note = input("Input id of the note you want to find: ")
                    result = self.notes_app.find_note_by_id(id_note)
                    if result: print(result)
                    else: print("Nothing has been found")
                elif find_choice == "2":
                    text = input("Type the text you want to find ")
                    result = self.notes_app.find_note_by_text(text)
                    if result:
                        print(*result, sep="\n")
                    else: print("Nothing has been found")
                else: print("Wrong input, you've been returned to the main menu")


            elif choice == "6":
                print("Have a good day, bye!")
                break
            else:
                print("Incorrect choice. You need to choose numbers from 1 to 6.")