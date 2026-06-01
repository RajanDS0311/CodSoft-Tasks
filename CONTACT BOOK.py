class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")

        contact = {"name":name,"phone":phone,"email":email,"address":address}
        self.contacts.append(contact)
        print("Contact added successfully")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts added to this book")
        else:
            print("====List of Contacts=====")
            for index,contact in enumerate(self.contacts,start=1):
                print(f"{index}.{contact["name"]},{contact['phone']},{contact['email']},{contact['address']}")
            print()

    def search_contact(self):
        search = input("Enter Name or Phone to Search: ")
        found = False
        for contact in self.contacts:
            if contact["name"] == search.lower() or contact["phone"] == search:
                print("Contact found successfully")
                print(f"Name : {contact['name']}")
                print(f"Phone : {contact['phone']}")
                print(f"Email : {contact['email']}")
                print(f"Address : {contact['address']}")
                found = True

            if not found:
                print("Contact not found")

    def update_contact(self):
        phone = input("Enter new phone number: ")
        for contact in self.contacts:
            if contact["phone"] == phone:
                print("Enter Details")
                contact['naem'] = input("Enter Name: ")
                contact["phone"] = input("Enter new phone number: ")
                contact["email"] = input("Enter new email: ")
                contact["address"] = input("Enter new address: ")
                return
                print("Contact updated successfully")
        print("Contact not found")


    def delete_contact(self):
        phone = input("Enter new phone number: ")
        for contact in self.contacts:
            if contact["phone"] == phone:
                self.contacts.remove(contact)
                print("Contact deleted successfully")
                return
        print("Contact not found")

c = ContactBook()
while True:
    print("===== CONTACT BOOK MENU =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        c.add_contact()

    elif choice == 2:
        c.view_contacts()

    elif choice == 3:
        c.search_contact()

    elif choice == 4:
        c.update_contact()

    elif choice == 5:
        c.delete_contact()

    elif choice == 6:
        print("Exiting.....")
        break

    else:
        print("Invalid choice")