#Name: (Corbin Woods)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 11/10/22
#Project #: M09
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

# displays the title message
def display_title():
    print("Corbin Woods's Wizard Inventory Game")
    print()

# displays the command menu
def display_menu():
    print("COMMAND MENU")
    print()
    print("show - Show all items")
    print("grab - Grab an item")
    print("edit - Edit an item")
    print("drop - Drop an item")
    print("exit - Exit program")

# defines the commands and what they do when entered
def main():
    display_title()
    display_menu()

    while True:        
        command = input("Command: ")       
        if command == "show":            # show command, shows current inventory
            show(inventory)                 
        elif command == "grab":          # grab command, grabs the object that the user types in
            grab_item(inventory)
        elif command == "edit":          # edit command, edits the name of an item
            edit_item(inventory)
        elif command == "drop":          # drop command, drops the selected item
            drop_item(inventory)
        elif command == "exit":          # exit command, exits the game
            break
        else:
            print("Not a valid command. Please try again.\n") # error message if the user enters an invalid command
    print("Bye!")

def show(inventory):         # code for the show command, which shows all items curenty in inventory
    for number, item in enumerate(inventory, start=1):
        print(f"{number}. {item}")   # prints the item number and then the item name
        print()     #prints a space after each item

def grab_item(inventory):               # code for the grab command
    if len(inventory) >= 4:
        print("You can't carry any more items. Drop something first.\n")        # if the player has 4 items in their inventory, displays this message
    else:
        item = input("Name: ")      # lets the user enter a custom name for an item.
        inventory.append(item)      # adds the item to the list for inventory
        print(f"{item} was added.\n")       # says that the item was successfully added

def edit_item(inventory):           # code for the edit command
    number = int(input("Number: "))         # lets the user enter the number of which item they want to edit
    if number < 1 or number > len(inventory): # if the user enters a number that doesn't exist, shows the error message below
        print("Invalid item number.\n")         # error message
    else:
        item = input("Updated name: ")      # shows that the item's name was updated
        inventory[number-1] = item                 # updates the item name
        print(f"Item number {number} was updated.\n")       # success message

def drop_item(inventory):           # code for the drop command
    number = int(input("Number: "))         # lets the user enter the item number they wish to drop
    if number < 1 or number > len(inventory):       # code for invalid numbers
        print("Invalid item number.\n")     # error message if they enter an invalid number
    else:
        item = inventory.pop(number-1)      # code for a correctly entered number
        print(f"{item} was dropped.\n")     # says that the item was dropped or removed from inventory.


inventory = ["Magical Staff", "Potion", "Old Wizard Hat"]       # starting inventory 

if __name__ == "__main__":  main()
main()      #starts the game code