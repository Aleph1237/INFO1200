#Name: (Corbin Woods)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date:12/01/22
#Project #: M11
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

#imports the csv libraries and makes a new variable called FILENAME
import csv
FILENAME = "contacts.csv"

#displays the title when program starts
def display_title():
    print("Corbin Woods's Contact Manager App")
    print()

#displays the menu when program starts
def display_menu():
    print("COMMAND MENU")
    print()
    print("list - Display all contacts")
    print("view - View a contact")
    print("add - Add a contact")
    print("del - Delete a contact")
    print("exit - Exit program")

#reads the contacts from the list
def read_contacts():
    #makes a new variable of an empty array called contacts
    contacts = []
    #opens the file and reads the data
    with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                #appends the data in the list
                contacts.append(row)

#displays contacts in csv file
def display(contacts):
    for i, row in enumerate(contacts, start=1):
            print(f"{i}. {row[0]}")
            print()

def view(contacts):
    number = get_contact_number(contacts)
    if number > 0:
        contact = contacts[number-1]
        print("Name:", contact[0])
        print("Email:", contact[1])
        print("Phone:", contact[2])
        print()

def get_contact_number(contacts):
    while True:
        try:
            number = int(input("Number: "))
        except ValueError:
            print("Invalid integer.\n")
            return -1
            
        if number < 1 or number > len(contacts):
            print("Invalid contact number.\n")
            return -1
        else:
            return number

def add(contacts):
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    contact = []
    contact.append(name)
    contact.append(email)
    contact.append(phone)
    contacts.append(contact)
    write_contacts(contacts)
    print("{contact[0]} was added.")
    print()

def write_contacts(contacts):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

def delete(contacts):
    number = get_contact_number(contacts)
    if number > 0:
        contact = contacts.pop(number-1)
        print(f"{contact[0]} was deleted.\n")
    write_contacts(contacts)


def main():
    contacts = read_contacts()
    display_title()
    display_menu()
    while True:
        command = input("Command: ")
        if command == "list":
            display(contacts)
        elif command == "view":
            view(contacts)
        elif command == "add":
            add(contacts)
        elif command == "del":
            delete(contacts)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":  main()