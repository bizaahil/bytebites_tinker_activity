from models import Customer, MenuItem, Menu, Order


# --- Customer tests ---

def test_customer_is_not_verified_with_empty_history():
    customer = Customer("Alex")
    assert customer.is_verified() == False

def test_customer_is_verified_with_purchase_history():
    customer = Customer("Alex")
    customer.purchase_history.append("order_001")
    assert customer.is_verified() == True


# --- MenuItem tests ---

def test_menu_item_stores_attributes():
    item = MenuItem("Spicy Burger", 8.99, "Mains", 4.5)
    assert item.name == "Spicy Burger"
    assert item.price == 8.99
    assert item.category == "Mains"
    assert item.popularity_rating == 4.5


# --- Menu tests ---

def test_filter_by_category_returns_correct_items():
    menu = Menu()
    menu.add_item(MenuItem("Large Soda", 2.49, "Drinks", 3.8))
    menu.add_item(MenuItem("Spicy Burger", 8.99, "Mains", 4.5))
    result = menu.filter_by_category("Drinks")
    assert len(result) == 1
    assert result[0].name == "Large Soda"

def test_filter_by_category_returns_empty_for_no_match():
    menu = Menu()
    menu.add_item(MenuItem("Spicy Burger", 8.99, "Mains", 4.5))
    result = menu.filter_by_category("Desserts")
    assert result == []

def test_get_all_items_returns_everything():
    menu = Menu()
    menu.add_item(MenuItem("Spicy Burger", 8.99, "Mains", 4.5))
    menu.add_item(MenuItem("Large Soda", 2.49, "Drinks", 3.8))
    menu.add_item(MenuItem("Chocolate Cake", 4.99, "Desserts", 4.8))
    assert len(menu.get_all_items()) == 3


# --- Order tests ---

def test_calculate_total_with_multiple_items():
    customer = Customer("Alex")
    order = Order(customer)
    order.add_item(MenuItem("Burger", 10.00, "Mains", 4.0))
    order.add_item(MenuItem("Soda", 5.00, "Drinks", 3.5))
    assert order.compute_total() == 15.00

def test_order_total_is_zero_when_empty():
    customer = Customer("Alex")
    order = Order(customer)
    assert order.compute_total() == 0

def test_get_summary_contains_customer_name():
    customer = Customer("Alex")
    order = Order(customer)
    order.add_item(MenuItem("Spicy Burger", 8.99, "Mains", 4.5))
    assert "Alex" in order.get_summary()