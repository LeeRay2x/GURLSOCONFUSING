import random
# things to do:
# 1.) make list directory
# 2.) create new user
# 3.) find user using Unique ID
# 4.) Edit user detaile
# 5.) deleter user

class Customer:                                      # define the class and attribute
    def __init__(self, unique_ID, name, address, phone):      
        self.unique_ID = unique_ID
        self.name = name
        self.address = address
        self.phone = phone

    def display_info(self):                                    # to display info per customer
        print(f"ID: {self.unique_ID}")
        print(f"Name: {self.name}")
        print(f"address: {self.address}")
        print(f"phone: {self.phone}")
        print()

customerList = [                                               # preloaded customers
    Customer(12345, "Natalie", "Cavite", "0912345"),
    Customer(56789, "Xhay", "Pasig", "0956789"),
    Customer(12389, "Alyssa", "Naic", "0912389")
]

def newCustomer():                                             # create new user/customer
    unique_ID = random.randint(10000, 99999)
    print(f"Your User ID: {unique_ID}")
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    phone = input("Enter your phone number: ")

    customer = Customer(unique_ID, name, address, phone)
    customerList.append(customer)
    print("Customer added!")


def deleteCustomer():                                          # deletes exisitng user
    findID = int(input("Enter the ID of the user you would like to remove: "))  
     
    for Customer in customerList:  
        if Customer.unique_ID == findID:                  
            print("Unique ID:", Customer.unique_ID) 
            print("Name:", Customer.name) 
            print("Address:", Customer.address)                      
            print("Phone Number:", Customer.phone) 
            print()  
 
            while True:  
                confirm = input(
                    "Are you sure to permanently delete this user? (y/n): "
                ) 

                if confirm.lower() == "y": 
                    customerList.remove(Customer) 
                    print("User deleted successfully!")
                    return

                elif confirm.lower() == "n": 
                    return

                else: 
                    print("Invalid. Please enter y or n.")

    else: 
        print("That ID does not exist")

def editInfo():                                      # edits existing user info
    findID = int(input("Enter the ID of the user you would like to edit: "))

    for Customer in customerList:
        if Customer.unique_ID == findID:

            print("Unique ID:", Customer.unique_ID)
            print("Name:", Customer.name)
            print("Address:", Customer.address)
            print("Phone Number:", Customer.phone)
            print()

            while True:
                choice = int(input(
                    "What would you like to edit?\n"
                    "name         [1]\n"
                    "address      [2]\n"
                    "phone number [3]\n"
                    "none         [4]\n"
                    "option: "
                ))

                if choice == 1:
                    Customer.name = input("Enter the new name: ")

                elif choice == 2:
                    Customer.address = input("Enter new address: ")

                elif choice == 3:
                    Customer.phone = input("Enter new phone number: ")

                elif choice == 4:
                    return

                else:
                    print("Invalid Option.")

            break

    else:
        print("That ID does not exist.")





