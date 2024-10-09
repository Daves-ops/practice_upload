DunkinDonuts = ['chocolate donut', 'strawberry donut', 'glazed donut', 'blueberry donut', "s'mores donut", 'bagel', 'bacon egg and cheese on bagel', 'hashbrowns']
MyOrder = []
DunkinDonutsRec = DunkinDonuts.copy()

def display_menus():
    #Display Dunkin Donuts menu and current order#
    print("\nDunkin Donuts: ", DunkinDonuts if DunkinDonuts else "None")
    print("My Order: ", MyOrder if MyOrder else "None")

def add_item():
    #Add item from menu to MyOrder#
    item = input('\nWhat would you like to order? ').lower()
    if item in DunkinDonuts:
        DunkinDonuts.remove(item)
        MyOrder.append(item)
        print(f"{item} added to your order.")
    else:
        print('Item not on our menu.')

def remove_item():
    #Remove item from MyOrder and return it to the Dunkin' Donuts menu#
    item = input('\nWhat would you want to remove from your order? ').lower()
    if item in MyOrder:
        MyOrder.remove(item)
        DunkinDonuts.append(item)
        print(f"{item} was removed from your order.")
    else:
        print(f'{item} is not in your order.')

def insert_item():
    """Add a recommendation to the Dunkin' Donuts menu."""
    rec = input("\nDunkin' wants to know what items you'd like to see in the future. Just let us know! ").lower()
    DunkinDonutsRec.append(rec)
    print(f"We added your recommendation: {rec} to our menu! We'll give it a look!")

def restart():
    """Restart the order, resetting Dunkin' Donuts menu and clearing MyOrder."""
    global DunkinDonuts, MyOrder
    MyOrder.clear()
    DunkinDonuts = ['chocolate donut', 'strawberry donut', 'glazed donut', 'blueberry donut', "s'mores donut", 'bagel', 'bacon egg and cheese on bagel', 'hashbrowns']
    print('Order restarted.')

def program():
    """Main program loop."""
    while True:
        display_menus()  # Show current menu and order
        print("\nOptions: ")
        print("1. Order")
        print("2. Remove item from order")
        print("3. Add recommendation to menu")
        print("4. Restart")
        print("5. Quit")

        choice = input("\nEnter your choice 1-5: ")

        if choice == '1':
            add_item()
        elif choice == '2':
            remove_item()
        elif choice == '3':
            insert_item()  # Corrected from insert_items to insert_item
        elif choice == '4':
            restart()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


program()
