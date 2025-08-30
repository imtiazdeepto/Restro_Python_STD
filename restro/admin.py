"""
Module containing the Admin class for the restaurant management system.
"""
from typing import List, Optional
from .models import MenuItem
from .customer import Customer


class Admin:
    """Represents an administrator who can manage the restaurant system."""
    
    def __init__(self, username: str, password: str):
        """Initialize an admin.
        
        Args:
            username: Admin's username
            password: Admin's password
        """
        self.username = username
        self.password = password
    
    def add_customer(self, restaurant, name: str, email: str, address: str) -> Optional[Customer]:
        """Add a new customer account.
        
        Args:
            restaurant: The restaurant object
            name: Customer's name
            email: Customer's email
            address: Customer's address
            
        Returns:
            The created Customer object if successful, None otherwise
        """
        return restaurant.add_customer(name, email, address)
    
    def view_customers(self, restaurant) -> List[Customer]:
        """View all customer accounts.
        
        Args:
            restaurant: The restaurant object
            
        Returns:
            List of all customers
        """
        return restaurant.get_customers()
    
    def remove_customer(self, restaurant, customer_id: str) -> bool:
        """Remove a customer account.
        
        Args:
            restaurant: The restaurant object
            customer_id: ID of the customer to remove
            
        Returns:
            True if successful, False otherwise
        """
        return restaurant.remove_customer(customer_id)
    
    def add_menu_item(self, restaurant, name: str, price: float, category: str = "Food") -> MenuItem:
        """Add a new item to the menu.
        
        Args:
            restaurant: The restaurant object
            name: Name of the menu item
            price: Price of the menu item
            category: Category of the item
            
        Returns:
            The created MenuItem object
        """
        return restaurant.add_menu_item(name, price, category)
    
    def remove_menu_item(self, restaurant, item_name: str) -> bool:
        """Remove an item from the menu.
        
        Args:
            restaurant: The restaurant object
            item_name: Name of the item to remove
            
        Returns:
            True if successful, False otherwise
        """
        return restaurant.remove_menu_item(item_name)
    
    def update_menu_item_price(self, restaurant, item_name: str, new_price: float) -> bool:
        """Update the price of a menu item.
        
        Args:
            restaurant: The restaurant object
            item_name: Name of the item to update
            new_price: New price for the item
            
        Returns:
            True if successful, False otherwise
        """
        return restaurant.update_menu_item_price(item_name, new_price)
