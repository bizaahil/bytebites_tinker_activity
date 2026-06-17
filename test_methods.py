from models import Customer, MenuItem, Menu, Order

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
