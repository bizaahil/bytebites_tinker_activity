# ByteBites - models.py
# This file contains the four core classes for the ByteBites campus food ordering app.
#
# Classes:
#   - Customer: represents a user of the app; stores name and purchase history
#   - MenuItem: represents a single food item; stores name, price, category, and popularity rating
#   - Menu: represents the full collection of food items; supports filtering by category
#   - Order: represents a single transaction; holds selected items and computes the total cost


class Customer:
    def __init__(self, name):
        self.name = name
        self.purchase_history = []

    def is_verified(self):
        # A customer is verified if they have at least one past purchase
        return len(self.purchase_history) > 0


class MenuItem:
    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        # Add a MenuItem to the menu
        self.items.append(item)

    def filter_by_category(self, category):
        # Return only items that match the given category string
        result = []
        for item in self.items:
            if item.category == category:
                result.append(item)
        return result

    def get_all_items(self):
        # Return the full list of menu items
        return self.items


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, item):
        # Add a MenuItem to this order
        self.items.append(item)

    def compute_total(self):
        # Sum the price of every item in the order
        total = 0
        for item in self.items:
            total += item.price
        return total

    def get_summary(self):
        # Return a readable string describing the order
        item_names = []
        for item in self.items:
            item_names.append(item.name)
        return (
            f"Order for {self.customer.name}: "
            f"{', '.join(item_names)} — "
            f"Total: ${self.compute_total():.2f}"
        )


if __name__ == "__main__":
    print("=== Testing Customer ===")
    customer = Customer("Alex")
    print("Verified (no history):", customer.is_verified())
    customer.purchase_history.append("order_001")
    print("Verified (with history):", customer.is_verified())

    print("\n=== Testing Menu ===")
    menu = Menu()
    menu.add_item(MenuItem("Spicy Burger", 8.99, "Mains", 4.5))
    menu.add_item(MenuItem("Veggie Wrap", 7.49, "Mains", 4.1))
    menu.add_item(MenuItem("Large Soda", 2.49, "Drinks", 3.8))
    menu.add_item(MenuItem("Chocolate Cake", 4.99, "Desserts", 4.8))

    print("All items:")
    for item in menu.get_all_items():
        print(" -", item.name)

    print("Filtered (Mains):")
    for item in menu.filter_by_category("Mains"):
        print(" -", item.name)

    print("\n=== Testing Order ===")
    order = Order(customer)
    order.add_item(MenuItem("Spicy Burger", 8.99, "Mains", 4.5))
    order.add_item(MenuItem("Large Soda", 2.49, "Drinks", 3.8))
    print("Summary:", order.get_summary())