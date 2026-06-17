from models import Customer, MenuItem, Menu, Order

# Test Customer
customer = Customer("Alex")
print("Customer name:", customer.name)
print("Purchase history:", customer.purchase_history)

# Test MenuItem
item1 = MenuItem("Spicy Burger", 8.99, "Mains", 4.5)
item2 = MenuItem("Large Soda", 2.49, "Drinks", 3.8)
print("\nMenuItem name:", item1.name)
print("MenuItem price:", item1.price)
print("MenuItem category:", item1.category)
print("MenuItem popularity_rating:", item1.popularity_rating)

# Test Menu
menu = Menu()
menu.add_item(item1)
menu.add_item(item2)
print("\nMenu items:", menu.items)

# Test Order
order = Order(customer)
order.add_item(item1)
order.add_item(item2)
print("\nOrder customer:", order.customer.name)
print("Order items:", order.items)

print("\nAll scaffolds loaded successfully!")