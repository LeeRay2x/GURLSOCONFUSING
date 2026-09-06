class menuItem: 
    def __init__(self, menuName, price, item_ID):               # state the class of each menu item
        self.menuName = menuName
        self.price = price
        self.item_ID = item_ID

    def display_Menu(self):
        print(f"Name: {self.menuName:<30} Price: {self.price:>5}PHP    [{self.item_ID}]")

menuList = [
    menuItem("Classic Caesar Salad", 850, "AP1"),                   # preloaded menu
    menuItem("Aged Steak Tartare", 1720, "AP2"),
    menuItem("Pea & Asparagus Soup", 680, "AP3"),
    menuItem("Bar and Grill Burger", 1650, "MC1"),
    menuItem("Duck Ragu Pasta", 1888, "MC2"),
    menuItem("Signature Beef Wellington", 3988, "MC3"),
    menuItem("Butter Mash Potatoes",  450, "SD1"),
    menuItem("Truffle Fries", 480, "SD2"),
    menuItem("Caramelised Apple Tart Tatin", 1680, "DS1"),
    menuItem("House Brewed Tea", 220, "D1")
]

def showMenu():                                         # displays menu
    print("Menu Items")
    print()
    for menuItem in menuList:
        menuItem.display_Menu()

def addMenuItem():                                      # add new item in the menu
    menuName = input("Enter the name of the Item: ")
    price = input("Enter price of the Item: ")
    item_ID  = input("Enter the item ID: ")
    
    newItem = menuItem(menuName, price, item_ID)
    menuList.append(newItem)
    print("New item added to the menu!")

def editMenu():                                        # update the menu
    for menuItem in menuList: 
        menuItem.display_Menu() 

    edit_ID = input("Enter the item ID of the Item you would like to update: ") 
    edit_ID = edit_ID.upper() 

    for menuItem in menuList: 

        if menuItem.item_ID == edit_ID: 

            print(f"{menuItem.menuName}\t{menuItem.price}\t{menuItem.item_ID}") 

            while True: 

                confirm = input("Confirm the Item (y/n): ") 
                print() 

                if confirm.lower() == "y": 

                    while True: 
                        edit = int(input(
                            "What would you like to edit?\n"
                            "Name     [1]\n"
                            "Price    [2]\n"
                            "Item_ID  [3]\n"
                            "Return   [4]\n"
                            "option: "
                        ))  

                        if edit == 1: 
                            menuItem.menuName = input(
                                "Enter the new name of the Item: "
                            )
                            print("Updated Successfully!") 
                            break 

                        elif edit == 2: 
                            menuItem.price = input(
                                "Enter the new price: "
                            )
                            print("Updated Successfully!") 
                            break 

                        elif edit == 3: 
                            menuItem.item_ID = input(
                                "Enter new item_ID: "
                            ).upper()
                            print("Updated Successfully!") 
                            break 

                        elif edit == 4: 
                            return 

                        else: 
                            print("Invalid Option!") 

                elif confirm.lower() == "n": 
                    return

                else: 
                    print("Invalid Option") 

            break

    else: 
        print("That Item does not exist") 

def deleteItem():                                       # delete the menu
    for menuItem in menuList: 
        menuItem.display_Menu() 

    remove_ID = input("Enter the item ID of the Item you would like to remove: ").upper() 
    print()

    item_found = False
    
    for menuItem in menuList:
        if menuItem.item_ID == remove_ID:
            item_found = True
            print("Item found!")
            print(f"{menuItem.menuName}\t{menuItem.price}\t{menuItem.item_ID}")
            print()
            
            confirm = input("Are you sure to permanently delete this Item?(y/n): ")
            if confirm.lower() == "y":
                menuList.remove(menuItem)
                print("Item is deleted successfully!")
            else:
                print("Deletion cancelled.")
            break

    if not item_found:
        print("Invalid Option! Item ID not found

    sdfgh


