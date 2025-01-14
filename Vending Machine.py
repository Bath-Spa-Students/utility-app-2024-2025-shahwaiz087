#To make a display that looks like a table, you don't have to use the tabulate module.
#This code creates a vending machine menu using a dictionary.
class VendingMachine:
    def __init__(self):
        # Add categories and goods to the vending machine's menu at first
        self.menu = {
            "Munchies": {
                "M1": {"Name": "Takis", "Price $": 9.75, "Stock": 10},
                "M2": {"Name": "Lays", "Price $": 3.25, "Stock": 14},
                "M3": {"Name": "Doritos", "Price $": 5.50, "Stock": 16},
                "M4": {"Name": "Pringles", "Price $": 7.75, "Stock": 10},
                "M5": {"Name": "Skittles", "Price $": 2.00, "Stock": 17},
                "M6": {"Name": "ringos", "Price $": 2.75, "Stock": 7},
            },
            "Drinks": {
                "D1": {"Name": "Sting", "Price $": 7.75, "Stock": 10},
                "D2": {"Name": "Mountain Dew", "Price $": 3.75, "Stock": 0},
                "D3": {"Name": "Seven Up", "Price $": 2.75, "Stock": 10},
                "D4": {"Name": "Coca Cola ", "Price $": 4.50, "Stock": 9},
                "D5": {"Name": "Pepsi", "Price $": 3.75, "Stock": 7},
                "D6": {"Name": "Bottled Water", "Price $": 0.50, "Stock": 10},
            },
            "Chocolates": {
                "C1": {"Name": "KitKat", "Price $": 3.75, "Stock": 17},
                "C2": {"Name": "Dark Chocolate", "Price $": 5.25, "Stock": 15},
                "C3": {"Name": "Mars", "Price $": 3.75, "Stock": 12},
                "C4": {"Name": "Bounty", "Price $": 3.75, "Stock": 14},
                "C5": {"Name": "Snickers", "Price $": 4.00, "Stock": 18},
            },
            "Hot Beverages": {
                "B1": {"Name": "Hot Chocolate", "Price $": 2.75, "Stock": 15},
                "B2": {"Name": "Cappuccino", "Price $": 4.95, "Stock": 14},
                "B3": {"Name": "Espresso", "Price $": 4.75, "Stock": 6},
                "B4": {"Name": "Tea", "Price $": 1.25, "Stock": 25},
                "B5": {"Name": "Mocha", "Price $": 5.05, "Stock": 10},
                "B6": {"Name": "Macha", "Price $": 7.95, "Stock": 5},
            },
            "Ice-Creams": {
                "I1": {"Name": "Vanilla Ice Cream", "Price $": 3.75, "Stock": 12},
                "I2": {"Name": "Chocolate Ice Cream", "Price $": 3.75, "Stock": 10},
                "I3": {"Name": "Blueberry Sorbet Popsicle", "Price $": 5.00, "Stock": 5},
                "I4": {"Name": "Brownie Ice Cream Sandwich", "Price $": 7.25, "Stock": 10},
            },
        }

    def display_menu(self):
        # show the user the menu
        print("\nMenu:")
        for category, items in self.menu.items():
            print(f"\n{category}:")
            for code, details in items.items():
                print(f"  {code}: {details['Name']} - ${details['Price $']} ({details['Stock']} in stock)")

    def purchase_item(self):
        # Manage the process of purchasing the item.
        self.display_menu()  # Show the user the menu.
        category = input("\nChoose any ONE category you want :) (i.e; Munchies, Drinks, Chocolates, Hot Beverages, Ice-Creams): ").strip()

        # Verify the entry for categories
        if category not in self.menu:
            print("Category not valid, Try Again Please :( .")
            return

        code = input("Type the item code :) (e.g., S1, D2): ").strip()

        # Verify that the item code entered is correct.
        if code not in self.menu[category]:
            print("Item Code not valid, try again please :( ).")
            return

        item = self.menu[category][code]

        # Verify whether the item is available.
        if item["Stock"] <= 0:
            print(f"Apologies, {item['Name']} is not available.")
            return

        try:
            # Request money from the user.
            payment = float(input(f"The price of {item['Name']} is ${item['Price $']}. Enter your payment: "))
        except ValueError:
            print("Invalid payment amount, try again ,Please.")
            return

        # Verify if the money is enough.
        if payment < item["Price $"]:
            print("Not enough money. Cancelled transaction :( ).")
        else:
            change = round(payment - item["Price $"], 2)  # Compute the change.
            item["Stock"] -= 1  # Cut the stock by one.
            print(f"We appreciate your purchase. {item['Name']}! The change you have is ${change}.")

    def run(self):
        # loop of the main program
        while True:
            print("\nThe Vending Machine welcomes you!")
            print("1. Check Out the Menu")
            print("2. Buy the item")
            print("3. Leave")

            choice = input("Pick a choice.: ")

            if choice == "1":
                self.display_menu()  # Show the menu.
            elif choice == "2":
                self.purchase_item()  # Get the purchasing process started.
            elif choice == "3":
                print("We appreciate your use of the vending machine, Have a good day !!")
                break  # End the program and get out of the loop.
            else:
                print("Choice not valid, try again please.")

if __name__ == "__main__":
    # Launch the application after creating a Vending Machine instance.
    vending_machine = VendingMachine()
    vending_machine.run()


    