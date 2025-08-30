"""
Module for creating an interactive interface for the restaurant management system.
"""
import sys
from typing import List, Optional

from .admin import Admin
from .customer import Customer
from .models import MenuItem
from .restaurant import Restaurant


class Interface:
    """User interface for the restaurant management system."""
    
    def __init__(self):
        """Initialize the interface."""
        self.restaurant = Restaurant("Delicious Eats")
        self.admin = Admin("admin", "admin123")
        self.current_customer: Optional[Customer] = None
        
    def display_main_menu(self):
        """Display the main menu options."""
        print("\n===== Restaurant Management System =====")
        print("1. Admin Login")
        print("2. Customer Login")
        print("3. Register as New Customer")
        print("4. Exit")
        
    def admin_login(self):
        """Handle admin login."""
        print("\n===== Admin Login =====")
        username = input("Username: ")
        password = input("Password: ")
        
        if username == self.admin.username and password == self.admin.password:
            print("Login successful!")
            self.admin_menu()
        else:
            print("Invalid credentials. Access denied.")
    
    def admin_menu(self):
        """Display the admin menu options."""
        while True:
            print("\n===== Admin Menu =====")
            print("1. Add Menu Item")
            print("2. Remove Menu Item")
            print("3. Update Menu Item Price")
            print("4. View Menu")
            print("5. View All Customers")
            print("6. Remove Customer")
            print("7. Logout")
            
            choice = input("Enter your choice (1-7): ")
            
            if choice == "1":
                self.add_menu_item()
            elif choice == "2":
                self.remove_menu_item()
            elif choice == "3":
                self.update_menu_item_price()
            elif choice == "4":
                self.view_menu()
            elif choice == "5":
                self.view_all_customers()
            elif choice == "6":
                self.remove_customer()
            elif choice == "7":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")
    
    def add_menu_item(self):
        """Add a new menu item."""
        print("\n===== Add Menu Item =====")
        name = input("Enter item name: ")
        
        # Check if item already exists
        for item in self.restaurant.get_menu():
            if item.name.lower() == name.lower():
                print("An item with this name already exists.")
                return
        
        try:
            price = float(input("Enter item price: $"))
            if price <= 0:
                print("Price must be positive.")
                return
        except ValueError:
            print("Invalid price. Please enter a number.")
            return
        
        category = input("Enter item category (Food/Drink): ")
        if not category:
            category = "Food"
        
        item = self.admin.add_menu_item(self.restaurant, name, price, category)
        print(f"Menu item added: {item}")
    
    def remove_menu_item(self):
        """Remove a menu item."""
        print("\n===== Remove Menu Item =====")
        self.view_menu()
        
        if not self.restaurant.get_menu():
            return
        
        name = input("Enter the name of the item to remove: ")
        if self.admin.remove_menu_item(self.restaurant, name):
            print(f"Item '{name}' removed successfully.")
        else:
            print(f"Item '{name}' not found.")
    
    def update_menu_item_price(self):
        """Update the price of a menu item."""
        print("\n===== Update Menu Item Price =====")
        self.view_menu()
        
        if not self.restaurant.get_menu():
            return
        
        name = input("Enter the name of the item to update: ")
        
        try:
            new_price = float(input("Enter the new price: $"))
            if new_price <= 0:
                print("Price must be positive.")
                return
        except ValueError:
            print("Invalid price. Please enter a number.")
            return
        
        if self.admin.update_menu_item_price(self.restaurant, name, new_price):
            print(f"Price for '{name}' updated to ${new_price:.2f}.")
        else:
            print(f"Item '{name}' not found.")
    
    def view_menu(self):
        """Display the restaurant menu."""
        menu = self.restaurant.get_menu()
        
        if not menu:
            print("The menu is empty.")
            return
        
        print("\n===== Restaurant Menu =====")
        for i, item in enumerate(menu, 1):
            print(f"{i}. {item}")
    
    def view_all_customers(self):
        """Display all registered customers."""
        customers = self.admin.view_customers(self.restaurant)
        
        if not customers:
            print("No customers registered.")
            return
        
        print("\n===== Registered Customers =====")
        for i, customer in enumerate(customers, 1):
            print(f"{i}. {customer}")
    
    def remove_customer(self):
        """Remove a customer account."""
        print("\n===== Remove Customer =====")
        self.view_all_customers()
        
        customers = self.admin.view_customers(self.restaurant)
        if not customers:
            return
        
        customer_id = input("Enter the Customer ID to remove: ")
        if self.admin.remove_customer(self.restaurant, customer_id):
            print(f"Customer with ID '{customer_id}' removed successfully.")
        else:
            print(f"Customer with ID '{customer_id}' not found.")
    
    def customer_login(self):
        """Handle customer login."""
        print("\n===== Customer Login =====")
        customer_id = input("Enter your Customer ID: ")
        
        customer = self.restaurant.get_customer(customer_id)
        if customer:
            self.current_customer = customer
            print(f"Welcome back, {customer.name}!")
            self.customer_menu()
        else:
            print("Customer not found. Please register or try again.")
    
    def register_customer(self):
        """Register a new customer."""
        print("\n===== Register as New Customer =====")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        address = input("Enter your address: ")
        
        customer = self.admin.add_customer(self.restaurant, name, email, address)
        print(f"Registration successful! Your Customer ID is: {customer.customer_id}")
        print("Please remember this ID for future logins.")
        
        self.current_customer = customer
        self.customer_menu()
    
    def customer_menu(self):
        """Display the customer menu options."""
        while True:
            print(f"\n===== Customer Menu ({self.current_customer.name}) =====")
            print(f"Current Balance: ${self.current_customer.check_balance():.2f}")
            print("1. View Menu")
            print("2. Place Order")
            print("3. View Order History")
            print("4. Add Funds")
            print("5. Logout")
            
            choice = input("Enter your choice (1-5): ")
            
            if choice == "1":
                self.view_menu()
            elif choice == "2":
                self.place_order()
            elif choice == "3":
                self.view_order_history()
            elif choice == "4":
                self.add_funds()
            elif choice == "5":
                print("Logging out...")
                self.current_customer = None
                break
            else:
                print("Invalid choice. Please try again.")
    
    def place_order(self):
        """Place a new order."""
        print("\n===== Place Order =====")
        self.view_menu()
        
        if not self.restaurant.get_menu():
            return
        
        print(f"Your balance: ${self.current_customer.check_balance():.2f}")
        
        item_names: List[str] = []
        while True:
            item_name = input("Enter item name to add to order (or 'done' to finish): ")
            if item_name.lower() == 'done':
                break
            item_names.append(item_name)
        
        if not item_names:
            print("No items selected.")
            return
        
        order = self.current_customer.place_order(self.restaurant, item_names)
        if order:
            print("Order placed successfully:")
            print(order)
            print(f"Remaining balance: ${self.current_customer.check_balance():.2f}")
    
    def view_order_history(self):
        """View customer's order history."""
        orders = self.current_customer.view_orders()
        
        if not orders:
            print("You have no past orders.")
            return
        
        print("\n===== Your Order History =====")
        for i, order in enumerate(orders, 1):
            print(f"Order #{i}:")
            print(order)
            print("---")
    
    def add_funds(self):
        """Add funds to customer's balance."""
        print("\n===== Add Funds =====")
        print(f"Current balance: ${self.current_customer.check_balance():.2f}")
        
        try:
            amount = float(input("Enter amount to add: $"))
            if amount <= 0:
                print("Amount must be positive.")
                return
        except ValueError:
            print("Invalid amount. Please enter a number.")
            return
        
        new_balance = self.current_customer.add_funds(amount)
        print(f"Funds added successfully. New balance: ${new_balance:.2f}")
    
    def run(self):
        """Run the interface."""
        print("Welcome to the Restaurant Management System!")
        
        while True:
            self.display_main_menu()
            choice = input("Enter your choice (1-4): ")
            
            if choice == "1":
                self.admin_login()
            elif choice == "2":
                self.customer_login()
            elif choice == "3":
                self.register_customer()
            elif choice == "4":
                print("Thank you for using the Restaurant Management System. Goodbye!")
                sys.exit(0)
            else:
                print("Invalid choice. Please try again.")
