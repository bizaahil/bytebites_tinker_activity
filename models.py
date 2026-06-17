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
        pass  # TODO: implement in Part 3


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
        pass  # TODO: implement in Part 3

    def filter_by_category(self, category):
        pass  # TODO: implement in Part 3

    def get_all_items(self):
        pass  # TODO: implement in Part 3


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, item):
        pass  # TODO: implement in Part 3

    def compute_total(self):
        pass  # TODO: implement in Part 3

    def get_summary(self):
        pass  # TODO: implement in Part 3