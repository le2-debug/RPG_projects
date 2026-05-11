inventory=[]

while True:
    #User selects option
    menu = ("View inventory", "Add item", "Remove item", "Exit")
    for options in menu:
        print(options)
    user_input= input("Select an option: ")
    
    #Inventory Validation
    
    if user_input == "View inventory":
        if len(inventory)<1:
            print("Inventory is empty")
        else:
            for items in inventory:
                print(items)
        print("*************"*3)
        
    

    if user_input == "Add item":
        add_item = input("Enter item:")
        if len(inventory)>=6:
            print("Inventory is full")
        elif add_item == "":
            print("Item cannot be empty")
        else:
            inventory.append(add_item)
            print(f"Added {add_item}")
        print("*************"*3)

    if user_input == "Remove item":
        if len(inventory)<1:
            print("Inventory is empty")
        for items in inventory:
            print(items)
        remove_item= input("Which item would you like to remove:")
        if remove_item=="":
            print("Enter an item in the inventory")
        elif remove_item not in inventory:
            print("The item is not found")
        else:
            inventory.remove(remove_item)
            print(f"Removed {remove_item}")
        print("*************"*3)

    if user_input == "Exit":
        print("Thank you for testing the system")
        break