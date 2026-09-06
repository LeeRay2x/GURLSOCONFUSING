# PAYMENT CLASS

class Payment:
    def __init__(self, payment_ID, order_ID, amount, method):
        self.payment_ID = payment_ID
        self.order_ID = order_ID
        self.amount = amount
        self.method = method
        self.status = "Pending"

    def display_payment(self):
        print(f"Payment ID: {self.payment_ID}")
        print(f"Order ID: {self.order_ID}")
        print(f"Amount: {self.amount} PHP")
        print(f"Payment Method: {self.method}")
        print(f"Payment Status: {self.status}")
        print()


# DELIVERY CLASS

class Delivery:
    def __init__(self, delivery_ID, order_ID, customer_ID, address):
        self.delivery_ID = delivery_ID
        self.order_ID = order_ID
        self.customer_ID = customer_ID
        self.address = address
        self.status = "Preparing"

    def display_delivery(self):
        print(f"Delivery ID: {self.delivery_ID}")
        print(f"Order ID: {self.order_ID}")
        print(f"Customer ID: {self.customer_ID}")
        print(f"Address: {self.address}")
        print(f"Delivery Status: {self.status}")
        print()


# PRELOADED PAYMENTS AND DELIVERIES

paymentList = []

deliveryList = []


# PROCESS PAYMENT

def processPayment(order_ID, amount):

    print()
    print("Payment")
    print()

    print("Payment Methods")
    print("Cash       [1]")
    print("GCash      [2]")
    print("Card       [3]")

    while True:

        choice = input("Choose Payment Method: ")

        if choice == "1":
            method = "Cash"
            break

        elif choice == "2":
            method = "GCash"
            break

        elif choice == "3":
            method = "Card"
            break

        else:
            print("Invalid option. Please try again.")

    # generate Payment ID
    payment_ID = f"PAY{len(paymentList) + 1:03d}"

    payment = Payment(
        payment_ID,
        order_ID,
        amount,
        method
    )

    # payment is considered successful
    payment.status = "Paid"

    paymentList.append(payment)

    print()
    print("Payment processed successfully!")
    print(f"Payment ID: {payment_ID}")
    print(f"Method: {method}")
    print(f"Amount: {amount} PHP")
    print()

    return payment


# CREATE DELIVERY

def createDelivery(order_ID, customer_ID, address):

    delivery_ID = f"DEL{len(deliveryList) + 1:03d}"

    delivery = Delivery(
        delivery_ID,
        order_ID,
        customer_ID,
        address
    )

    deliveryList.append(delivery)

    print()
    print("Delivery created successfully!")
    print(f"Delivery ID: {delivery_ID}")
    print(f"Status: {delivery.status}")
    print()

    return delivery


# UPDATE DELIVERY STATUS 

def updateDelivery():

    if not deliveryList:
        print("There are no deliveries.")
        return

    delivery_ID = input(
        "Enter the Delivery ID you would like to update: "
    )

    for delivery in deliveryList:

        if delivery.delivery_ID == delivery_ID.upper():

            print()
            delivery.display_delivery()

            print("Update Delivery Status")
            print("Preparing          [1]")
            print("Out for Delivery   [2]")
            print("Delivered          [3]")
            print("Cancel             [4]")

            while True:

                choice = input("Option: ")

                if choice == "1":
                    delivery.status = "Preparing"
                    break

                elif choice == "2":
                    delivery.status = "Out for Delivery"
                    break

                elif choice == "3":
                    delivery.status = "Delivered"
                    break

                elif choice == "4":
                    return

                else:
                    print("Invalid option.")

            print()
            print("Delivery status updated successfully!")
            print()

            return

    print("That Delivery ID doesn't exist.")


# SHOW ALL PAYMENTS

def showPayments():

    if not paymentList:
        print("There are no payments.")
        return

    print()
    print("Payment Records")
    print()

    for payment in paymentList:
        payment.display_payment()


# SHOW ALL DELIVERIES

def showDeliveries():

    if not deliveryList:
        print("There are no deliveries.")
        return

    print()
    print("Delivery Records")
    print()

    for delivery in deliveryList:
        delivery.display_delivery()


# FIND PAYMENT

def findPayment():

    payment_ID = input(
        "Enter the Payment ID: "
    )

    for payment in paymentList:

        if payment.payment_ID == payment_ID.upper():

            payment.display_payment()
            return payment

    print("That Payment ID doesn't exist.")


# FIND DELIVERY

def findDelivery():

    delivery_ID = input(
        "Enter the Delivery ID: "
    )

    for delivery in deliveryList:

        if delivery.delivery_ID == delivery_ID.upper():

            delivery.display_delivery()
            return delivery

    print("That Delivery ID doesn't exist.")


# MANAGE PAYMENT AND DELIVERY

def managePaymentDelivery():

    while True:

        print()
        print("Payment and Delivery Management")
        print()
        print("View Payments              [1]")
        print("Find Payment               [2]")
        print("View Deliveries            [3]")
        print("Find Delivery              [4]")
        print("Update Delivery Status     [5]")
        print("Return                     [6]")

        choice = input("Option: ")

        if choice == "1":

            showPayments()

        elif choice == "2":

            findPayment()

        elif choice == "3":

            showDeliveries()

        elif choice == "4":

            findDelivery()

        elif choice == "5":

            updateDelivery()

        elif choice == "6":

            return

        else:

            print("Invalid option.")
