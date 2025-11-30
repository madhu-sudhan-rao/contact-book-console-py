# Simple Contacts Book using Dictionary
# Menu-driven

contacts = {}   # Dictionary to store contacts


def view_contacts():
    if not contacts:
        print("\nNo contacts found.\n")
        return
    print("\n--- Contact List ---")
    for name, phone in contacts.items():
        print(f"{name} : {phone}")
    print()


def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print("Contact added successfully!\n")


def edit_contact():
    name = input("Enter the name of the contact to edit: ")
    if name in contacts:
        new_phone = input("Enter new phone number: ")
        contacts[name] = new_phone
        print("Contact updated!\n")
    else:
        print("Contact not found!\n")


def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted!\n")
    else:
        print("Contact not found!\n")


while True:
    print("----- Contacts Book Menu -----")
    print("1. View Contact List")
    print("2. Add Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        view_contacts()
    elif choice == "2":
        add_contact()
    elif choice == "3":
        edit_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Exiting program... Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.\n")
