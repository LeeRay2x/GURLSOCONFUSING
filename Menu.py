class menuItem: 
    def __init__(self, menuName, price, item_ID):
        self.menuName = menuName
        self.price = price
        self.item_ID = item_ID

    def display_Menu(self):
        print(f"Name: {self.menuName:<30} Price: {self.price:>5}PHP    [{self.item_ID}]")

menuList = [
    menuItem("Classic Caesar Salad", 850, "AP1"),
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

def showMenu():
    print("Menu Items")
    print()
    for menuItem in menuList:
        menuItem.display_Menu()

def manageMenu():
while True:
    item = input("Enter which Item you would like to Update: ")

    for menuItem in menuList:
        if menuItem.item_ID == item.upper():

            print(f"Name: {menuItem.menuName} Price: {menuItem.price}PHP [{menuItem.item_ID}]")

            edit = int(input(
                "What would you like to edit?\n"
                "Name [1]\n"
                "Price [2]\n"
                "Item ID [3]\n"
                "Option: "
            ))


            break

    else:
        print("That Item Doesn't Exist")
        continue

    break
manageMenu()
