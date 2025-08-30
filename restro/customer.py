"""
Module containing the Customer class for the restaurant management system.
"""
from typing import List, Optional
from .models import MenuItem, Order


class Customer:
    """Represents a customer who can place orders."""
    
    def __init__(self, name: str, email: str, address: str, customer_id: str):
        """Initialize a customer.
        
        Args:
            name: Customer's name
            email: Customer's email
            address: Customer's address
            customer_id: Unique identifier for the customer
        """
        self.name = name
        self.email = email
        self.address = address
        self.customer_id = customer_id
        self.balance = 0.0
        self.orders: List[Order] = []
        
    def view_menu(self, restaurant):
        """View the restaurant's menu.
        
        Args:
            restaurant: The restaurant object
            
        Returns:
            The restaurant's menu
        """
        return restaurant.get_menu()
    
    def place_order(self, restaurant, item_names: List[str]) -> Optional[Order]:
        """Place an order by selecting items from the menu.
        
        Args:
            restaurant: The restaurant object
            item_names: List of item names to order
            
        Returns:
            The created Order object if successful, None otherwise
        """
        menu = restaurant.get_menu()
        items = []
        total_cost = 0.0
        
        # Find requested items in the menu
        for item_name in item_names:
            found = False
            for menu_item in menu:
                if menu_item.name.lower() == item_name.lower():
                    items.append(menu_item)
                    total_cost += menu_item.price
                    found = True
                    break
            if not found:
                print(f"Item '{item_name}' not found in menu.")
                return None
        
        # Check if customer has enough balance
        if self.balance < total_cost:
            print(f"Insufficient balance. Order total: ${total_cost:.2f}, Your balance: ${self.balance:.2f}")
            return None
        
        # Create and process the order
        order = Order(items, self.customer_id)
        self.balance -= total_cost
        self.orders.append(order)
        return order
    
    def check_balance(self) -> float:
        """Check the customer's available balance.
        
        Returns:
            The customer's current balance
        """
        return self.balance
    
    def view_orders(self) -> List[Order]:
        """View a list of past orders.
        
        Returns:
            List of the customer's past orders
        """
        return self.orders
    
    def add_funds(self, amount: float) -> float:
        """Add funds to the customer's balance.
        
        Args:
            amount: Amount to add to the balance
            
        Returns:
            The updated balance
        """
        if amount <= 0:
            print("Amount must be positive.")
            return self.balance
        
        self.balance += amount
        return self.balance
    
    def __str__(self) -> str:
        """Return a string representation of the customer."""
        return f"Customer ID: {self.customer_id}, Name: {self.name}, Email: {self.email}"
