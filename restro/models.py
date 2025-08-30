"""
Module containing the MenuItem and Order classes for the restaurant management system.
"""
from datetime import datetime
from typing import List


class MenuItem:
    """Represents a food or drink item on the restaurant menu."""
    
    def __init__(self, name: str, price: float, category: str = "Food"):
        """Initialize a menu item.
        
        Args:
            name: The name of the menu item
            price: The price of the menu item
            category: The category of the item (e.g., "Food", "Drink")
        """
        self.name = name
        self.price = price
        self.category = category
        
    def __str__(self) -> str:
        """Return a string representation of the menu item."""
        return f"{self.name} (${self.price:.2f}) - {self.category}"


class Order:
    """Represents an order placed by a customer."""
    
    def __init__(self, items: List[MenuItem], customer_id: str):
        """Initialize an order.
        
        Args:
            items: List of menu items in the order
            customer_id: ID of the customer who placed the order
        """
        self.items = items
        self.customer_id = customer_id
        self.total_price = sum(item.price for item in items)
        self.timestamp = datetime.now()
        self.order_id = f"{customer_id}-{self.timestamp.strftime('%Y%m%d%H%M%S')}"
        
    def __str__(self) -> str:
        """Return a string representation of the order."""
        items_str = "\n".join(f"  - {item}" for item in self.items)
        return (
            f"Order ID: {self.order_id}\n"
            f"Date: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Items:\n{items_str}\n"
            f"Total: ${self.total_price:.2f}"
        )
