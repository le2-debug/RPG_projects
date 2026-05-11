inventory=[]

while True:
    menu = ("View inventory", "Add item", "Remove item", "Exit")
    print(menu)
    user_input= input("Select an option: ")

    if user_input == "View inventory":
        print(inventory)
        if len(inventory)<1:
            print("Inventory is empty")
        
    if user_input == "Add item":
        add_item = input("Enter item:")
        if len(inventory)>=6:
            print("Inventory is full")
        if not isinstance(add_item, str):
            print("Item should be a string")
        inventory.append(add_item)
        print(f"Added {add_item}")

    if user_input == "Remove item":
        print(inventory)
        remove_item= input("Which item would you like to remove:")
        if not isinstance(remove_item,str):
            print("Item should be a string")
        inventory.remove(remove_item)
        print(f"Removed {remove_item}")

    if user_input == "Exit":
        print("Thank you for testing the system")
        break