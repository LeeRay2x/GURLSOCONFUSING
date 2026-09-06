from datetime import datetime

from customer import customerList, newCustomer
from menu import menuList, showMenu

orderIDCounter = 1000
completedOrders = []                 

class OrderItem:
    def __init__(self, menu_item, quantity):
        self.menu_item = menu_item
        self.quantity = quantity

    def get_subtotal(self):
        price = float(self.menu_item.price)     # menu.py sometimes stores price as text
        return price * self.quantity

    def __str__(self):
        return f"{self.quantity}x {self.menu_item.menuName} - PHP {self.get_subtotal()}"

class Order:
    def __init__(self, customer):
        global orderIDCounter
        orderIDCounter += 1

        self.order_id = orderIDCounter
        self.customer = customer
        self.items = []
        self.status = "Pending"
        self.date_created = datetime.now()

    def add_item(self, menu_item, quantity):
        self.items.append(OrderItem(menu_item, quantity))

    def get_subtotal(self):
        total = 0
        for i in self.items:
            total += i.get_subtotal()
        return total

    def get_service_fee(self):
        return 0            # pickup / default order has no fee

    def get_total(self):
        return self.get_subtotal() + self.get_service_fee()

    def get_receipt(self):
        print(f"Order #{self.order_id} - {self.customer.name}")
        print(f"Date: {self.date_created.strftime('%Y-%m-%d %H:%M')}")
        print(f"Status: {self.status}")
        print("-" * 35)
        for i in self.items:
            print(i)
        print("-" * 35)
        print(f"Subtotal: PHP {self.get_subtotal():.2f}")
        print(f"Service Fee: PHP {self.get_service_fee():.2f}")
        print(f"TOTAL: PHP {self.get_total():.2f}")

class DeliveryOrder(Order):
    def __init__(self, customer):
        super().__init__(customer)
        self.delivery_address = customer.address

    def get_service_fee(self):
        return 49.00

class PickupOrder(Order):
    pass                     

def findCustomerByID(customer_id):
    for Customer in customerList:
        if Customer.unique_ID == customer_id:
            return Customer
    return None

def findMenuItemByID(item_id):
    item_id = item_id.upper()
    for item in menuList:
        if item.item_ID == item_id:
            return item
    return None

def createOrder():
    customer = None
    while customer == None:
        userInput = input("Enter your Customer ID (or type REGISTER if you're new): ")

        if userInput.upper() == "REGISTER":
            print("\nLet's get you registered!")
            newCustomer()
            customer = customerList[-1]
            continue

        customer_id = int(userInput)          
        customer = findCustomerByID(customer_id)
        if customer == None:
            print("No customer found with that ID. Try again.")

    print("\nWelcome,", customer.name + "!")
    print("Address:", customer.address)
    print("Phone:", customer.phone)

    orderType = input("\nOrder type - Delivery [1] or Pickup [2]: ")
    if orderType == "1":
        order = DeliveryOrder(customer)
    else:
        order = PickupOrder(customer)

    print()
    showMenu()
    print()

    while True:
        itemID = input("Enter Item ID to add (or type DONE to finish): ")
        if itemID.upper() == "DONE":
            if len(order.items) == 0:
                print("You haven't added anything yet.")
                continue
            break

        item = findMenuItemByID(itemID)
        if item == None:
            print("That item ID doesn't exist. Check the menu above.")
            continue

        qty = int(input(f"Quantity for {item.menuName}: "))
        order.add_item(item, qty)
        print(f"Added {qty}x {item.menuName} to your order.\n")

    order.status = "Confirmed"
    print()
    order.get_receipt()
    print("\n")

    order.status = "Completed"
    completedOrders.append(order)
    print("Order completed. Thank you!\n")

    return order

if __name__ == "__main__":
    createOrder()
