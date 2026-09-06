from Customer import customerList, newCustomer, manageCustomer
from Menu import menuList, showMenu, manageMenu
from Order import createOrder, completedOrders
from pay_and_deliver import (
    processPayment,
    createDelivery,
    showPayments,
    showDeliveries,
    updateDelivery
)


def customer_menu():
    while True:
        print("\n===== CUSTOMER MANAGEMENT =====")
        print("[1] Register New Customer")
        print("[2] Manage Customer")
        print("[3] View Customers")
        print("[4] Return")

        choice = input("Enter option: ")

        if choice == "1":
            newCustomer()

        elif choice == "2":
            manageCustomer()

        elif choice == "3":
            if len(customerList) == 0:
                print("No customers found.")
            else:
                print("\n===== CUSTOMER LIST =====")
                for customer in customerList:
                    customer.display_info()

        elif choice == "4":
            break

        else:
            print("Invalid option.")


def menu_management():
    while True:
        print("\n===== MENU MANAGEMENT =====")
        print("[1] View Menu")
        print("[2] Manage Menu")
        print("[3] Return")

        choice = input("Enter option: ")

        if choice == "1":
            showMenu()

        elif choice == "2":
            manageMenu()

        elif choice == "3":
            break

        else:
            print("Invalid option.")


def order_menu():
    while True:
        print("\n===== ORDER MANAGEMENT =====")
        print("[1] Create New Order")
        print("[2] View Completed Orders")
        print("[3] Return")

        choice = input("Enter option: ")

        if choice == "1":
            createOrder()

        elif choice == "2":
            if len(completedOrders) == 0:
                print("No completed orders.")
            else:
                print("\n===== COMPLETED ORDERS =====")
                for order in completedOrders:
                    order.get_receipt()
                    print()

        elif choice == "3":
            break

        else:
            print("Invalid option.")


def payment_delivery_menu():
    while True:
        print("\n===== PAYMENT & DELIVERY =====")
        print("[1] Process Payment")
        print("[2] Create Delivery")
        print("[3] Update Delivery")
        print("[4] View Payments")
        print("[5] View Deliveries")
        print("[6] Return")

        choice = input("Enter option: ")

        if choice == "1":
            if len(completedOrders) == 0:
                print("No orders available.")
                continue

            order = completedOrders[-1]

            print(f"\nOrder #{order.order_id}")
            print(f"Customer: {order.customer.name}")
            print(f"Total: PHP {order.get_total():.2f}")

            processPayment(
                order.order_id,
                order.get_total()
            )

        elif choice == "2":
            if len(completedOrders) == 0:
                print("No orders available.")
                continue

            order = completedOrders[-1]

            if order.__class__.__name__ == "PickupOrder":
                print("This order is for pickup and does not require delivery.")
            else:
                createDelivery(
                    order.order_id,
                    order.customer.unique_ID,
                    order.customer.address
                )

        elif choice == "3":
            updateDelivery()

        elif choice == "4":
            showPayments()

        elif choice == "5":
            showDeliveries()

        elif choice == "6":
            break

        else:
            print("Invalid option.")


def main():
    while True:
        print("\n")
        print("=" * 45)
        print("       FOOD DELIVERY SYSTEM")
        print("=" * 45)
        print("[1] Customer Management")
        print("[2] Menu Management")
        print("[3] Order Processing")
        print("[4] Payment and Delivery")
        print("[5] Exit")
        print("=" * 45)

        choice = input("Enter option: ")

        if choice == "1":
            customer_menu()

        elif choice == "2":
            menu_management()

        elif choice == "3":
            order_menu()

        elif choice == "4":
            payment_delivery_menu()

        elif choice == "5":
            print("\nThank you for using the Food Delivery System!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
