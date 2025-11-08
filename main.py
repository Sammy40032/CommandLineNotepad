import datetime
import sys
from weakref import finalize

FILE_NAME = 'journal.txt'

def addEntry():
    try:
        with open(FILE_NAME, "r") as f:
            pass
    except FileNotFoundError:
        open(FILE_NAME, "w").close()

    entry = input("Write what you would like to add to your journal: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILE_NAME, "a") as file:
        file.write(f"[{timestamp}] {entry}\n")

    print("Entry Saved!")

def deleteEntry():
    with open(FILE_NAME, "r") as file:
        entries = file.readlines()
    for i, entry in enumerate(entries, start=1):
        print(f"{i}. {entry.strip()}")

    try:
        choice = int(input("Enter the number of the entry to remove: "))
        if 1 <= choice <= len(entries):
            removed = entries.pop(choice - 1)
            with open(FILE_NAME, "w") as file:
                file.writelines(entries)
            print(f"Removed: {removed.strip()}")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")


def viewEntry():
    try:
        with open(FILE_NAME, 'r') as file:
            print("\n--- Your Journal ---")
            print(file.read())
    except FileNotFoundError:
        print("No entries yet!\n")

def main():
    while True:
        print("1. Add entrie")
        print("2. View entries")
        print("3. Remove entrie")
        print("4. Exit")
        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("INVALID INPUT. Please enter a number.\n")
            continue

        if choice == 1:
            addEntry()
        elif choice == 2:
            viewEntry()
        elif choice == 3:
            deleteEntry()
        elif choice == 4:
            print("Have a good day! Bye!")
            sys.exit()
        else:
            print("INVALID CHOICE PICK A NUMBER 1-3 try again\n")

if __name__ == "__main__":
    main()




