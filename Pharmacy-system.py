class Medicine:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def reduce_stock(self, amount):
        if amount > self.quantity:
            print(f"Not enough stock of {self.name}.")
            return False
        self.quantity -= amount
        return True

    def __str__(self):
        return f"{self.name} | Quantity: {self.quantity} | Price: ${self.price}"


class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name} | Phone: {self.phone}"


class Pharmacy:
    def __init__(self):
        self.medicines = []
        self.customers = []

    # Medicine methods
    def add_medicine(self):
        name = input("Enter medicine name: ")
        try:
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
        except ValueError:
            print("Invalid input. Quantity must be an integer, price a number.")
            return
        
        medicine = next((m for m in self.medicines if m.name.lower() == name.lower()), None)
        if medicine:
            medicine.quantity += quantity
            medicine.price = price 
            print(f"Updated {medicine.name} stock.")
        else:
            self.medicines.append(Medicine(name, quantity, price))
            print(f"{name} added successfully!")

    def view_medicines(self):
        if not self.medicines:
            print("No medicines in stock.")
            return
        print("Medicine List:")
        for med in self.medicines:
            print(med)

    # Customer methods
    def add_customer(self):
        name = input("Enter customer name: ")
        phone = input("Enter phone number: ")
        self.customers.append(Customer(name, phone))
        print(f"{name} added successfully!")

    def view_customers(self):
        if not self.customers:
            print("No customers yet.")
            return
        print("Customer List:")
        for cust in self.customers:
            print(cust)

    # Sales
    def sell_medicine(self):
        if not self.customers:
            print("No customers found. Please add a customer first.")
            return
        if not self.medicines:
            print("No medicines in stock to sell.")
            return

        cust_name = input("Enter customer name: ")
        customer = next((c for c in self.customers if c.name.lower() == cust_name.lower()), None)
        if not customer:
            print("Customer not found. Please add the customer first.")
            return

        med_name = input("Enter medicine name: ")
        medicine = next((m for m in self.medicines if m.name.lower() == med_name.lower()), None)
        if not medicine:
            print("Medicine not found.")
            return

        try:
            quantity = int(input("Enter quantity to sell: "))
        except ValueError:
            print("Invalid quantity.")
            return

        if medicine.reduce_stock(quantity):
            total_price = quantity * medicine.price
            print(f"Sold {quantity} of {medicine.name} to {customer.name}. Total: ${total_price:.2f}")


def main():
    pharmacy = Pharmacy()
    while True:
        print("\n--- Pharmacy Management ---")
        print("1. Add Medicine")
        print("2. View Medicines")
        print("3. Add Customer")
        print("4. View Customers")
        print("5. Sell Medicine")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("Invalid input. Enter a number 1-6.")
            continue

        if choice == 1:
            pharmacy.add_medicine()
        elif choice == 2:
            pharmacy.view_medicines()
        elif choice == 3:
            pharmacy.add_customer()
        elif choice == 4:
            pharmacy.view_customers()
        elif choice == 5:
            pharmacy.sell_medicine()
        elif choice == 6:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Enter 1-6.")


if __name__ == "__main__":
    main()