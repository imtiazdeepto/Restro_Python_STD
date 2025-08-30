"""
Module containing the Restaurant class for the restaurant management system.
"""
from typing import List, Dict, Optional
from .models import MenuItem
from .customer import Customer


class Restaurant:
    """Represents a restaurant with menu and customer management."""
    
    def __init__(self, name: str):
        """Initialize a restaurant.
        
        Args:
            name: The name of the restaurant
        """
        self.name = name
        self.menu: List[MenuItem] = []
        self.customers: Dict[str, Customer] = {}
        self.next_customer_id = 1
    
    def get_menu(self) -> List[MenuItem]:
        """Get the restaurant's menu.
        
        Returns:
            List of menu items
        """
        return self.menu
    
    def add_menu_item(self, name: str, price: float, category: str = "Food") -> MenuItem:
        """Add a new item to the menu.
        
        Args:
            name: Name of the menu item
            price: Price of the menu item
            category: Category of the item
            
        Returns:
            The created MenuItem object
        """
        item = MenuItem(name, price, category)
        self.menu.append(item)
        return item
    
    def remove_menu_item(self, item_name: str) -> bool:
        """Remove an item from the menu.
        
        Args:
            item_name: Name of the item to remove
            
        Returns:
            True if successful, False otherwise
        """
        for i, item in enumerate(self.menu):
            if item.name.lower() == item_name.lower():
                self.menu.pop(i)
                return True
        return False
    
    def update_menu_item_price(self, item_name: str, new_price: float) -> bool:
        """Update the price of a menu item.
        
        Args:
            item_name: Name of the item to update
            new_price: New price for the item
            
        Returns:
            True if successful, False otherwise
        """
        for item in self.menu:
            if item.name.lower() == item_name.lower():
                item.price = new_price
                return True
        return False
    
    def add_customer(self, name: str, email: str, address: str) -> Customer:
        """Add a new customer.
        
        Args:
            name: Customer's name
            email: Customer's email
            address: Customer's address
            
        Returns:
            The created Customer object
        """
        customer_id = f"C{self.next_customer_id:04d}"
        self.next_customer_id += 1
        
        customer = Customer(name, email, address, customer_id)
        self.customers[customer_id] = customer
        return customer
    
    def get_customers(self) -> List[Customer]:
        """Get all customers.
        
        Returns:
            List of all customers
        """
        return list(self.customers.values())
    
    def get_customer(self, customer_id: str) -> Optional[Customer]:
        """Get a customer by ID.
        
        Args:
            customer_id: ID of the customer to get
            
        Returns:
            The Customer object if found, None otherwise
        """
        return self.customers.get(customer_id)
    
    def remove_customer(self, customer_id: str) -> bool:
        """Remove a customer.
        
        Args:
            customer_id: ID of the customer to remove
            
        Returns:
            True if successful, False otherwise
        """
        if customer_id in self.customers:
            del self.customers[customer_id]
            return True
        return False
    
    def __str__(self) -> str:
        """Return a string representation of the restaurant."""
        return f"Restaurant: {self.name} ({len(self.menu)} menu items, {len(self.customers)} customers)"
