# ByteBites 🍔

A backend system for a campus food ordering app, built with Python classes and simple algorithms.

## Project Overview

ByteBites manages customers, food items, menus, and orders. The system is designed to be clean, readable, and strictly limited to the four core classes described in the feature specification.

## Classes

| Class | Description |
|---|---|
| `Customer` | Stores a customer's name and purchase history; can verify if they're a real user |
| `MenuItem` | Represents a food item with a name, price, category, and popularity rating |
| `Menu` | Holds all menu items; supports filtering by category |
| `Order` | Groups selected items for a customer and computes the total cost |

## Project Structure

```
bytebites_tinker_activity/
├── models.py                   # Core class implementations
├── test_bytebites.py           # pytest test suite
├── bytebites_spec.md           # Original feature request + candidate classes
├── bytebites_design.md         # Final UML class design
├── draft_from_copilot.md       # Initial AI-generated UML draft
├── ByteBites_Design_Reference.md  # Behavioral instructions for AI assistant
└── README.md
```

## Setup

No external libraries required. To run the app:

```bash
python3 models.py
```

To run the test suite:

```bash
pip install pytest
pytest test_bytebites.py -v
```

## Example Usage

```python
from models import Customer, MenuItem, Menu, Order

# Create a customer
customer = Customer("Alex")
customer.purchase_history.append("order_001")
print(customer.is_verified())  # True

# Build a menu
menu = Menu()
menu.add_item(MenuItem("Spicy Burger", 8.99, "Mains", 4.5))
menu.add_item(MenuItem("Large Soda", 2.49, "Drinks", 3.8))
menu.add_item(MenuItem("Chocolate Cake", 4.99, "Desserts", 4.8))

# Filter by category
drinks = menu.filter_by_category("Drinks")
print(drinks[0].name)  # Large Soda

# Place an order
order = Order(customer)
order.add_item(MenuItem("Spicy Burger", 8.99, "Mains", 4.5))
order.add_item(MenuItem("Large Soda", 2.49, "Drinks", 3.8))
print(order.get_summary())
# Order for Alex: Spicy Burger, Large Soda — Total: $11.48
```

## Out of Scope

This project intentionally excludes authentication, databases, APIs, and any external frameworks — per the design specification.