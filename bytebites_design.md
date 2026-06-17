# ByteBites UML Design (Final)

Generated with reference file constraints applied.

## Classes

### Customer
- Attributes: `name: str`, `purchase_history: list`
- Methods: `is_verified() -> bool`

### MenuItem
- Attributes: `name: str`, `price: float`, `category: str`, `popularity_rating: float`

### Menu
- Attributes: `items: list[MenuItem]`
- Methods: `add_item(item: MenuItem)`, `filter_by_category(category: str) -> list`, `get_all_items() -> list`

### Order
- Attributes: `customer: Customer`, `items: list[MenuItem]`
- Methods: `add_item(item: MenuItem)`, `compute_total() -> float`, `get_summary() -> str`

## Relationships
- `Order` → `Customer` — an Order belongs to a Customer
- `Menu` → `MenuItem` — a Menu contains MenuItems
- `Order` → `MenuItem` — an Order holds MenuItems

## Out of scope
- Authentication or user login
- Database or file storage
- Any class beyond the four above
- External libraries or frameworks