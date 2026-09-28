while True:
    print("\nDaily Notes App ")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Enter your choice: ")

    
    if choice == "1":
        note = input("Enter your note: ")

        file = open("notes.txt", "a")
        file.write(note + "\n")
        file.close()

        print("Note saved successfully!")

    
    elif choice == "2":
        file = open("notes.txt", "r")
        content = file.read()
        file.close()

        print("\n-------------- Your Notes ----------------")
        
        if content:
            print(content)
        else:
            print("No notes found.")

    
    elif choice == "3":
        print("Thank you for using Daily Notes App!")
        break

    
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")