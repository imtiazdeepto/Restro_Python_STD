# Restaurant Management System

A comprehensive restaurant management application built in Python that allows restaurant owners to manage their menu, customer accounts, and orders through an interactive command-line interface.

## Features

### Customer Features
- View restaurant menu (food and drinks)
- Place orders by selecting items from the menu
- Check available balance before placing orders
- View order history
- Add funds to account balance

### Admin Features
- Create and manage restaurant menu (add/remove items, update prices)
- Manage customer accounts (add/view/remove customers)
- Full control over restaurant operations

### Restaurant Features
- Menu management system
- Customer account management
- Order processing and tracking

## Project Structure

```
restro/
│
├── __init__.py        # Package initialization
├── admin.py           # Admin class implementation
├── customer.py        # Customer class implementation
├── interface.py       # Command-line interface
├── main.py            # Main entry point for the application
├── models.py          # Data models (MenuItem, Order)
└── restaurant.py      # Restaurant class implementation
│
app.py                 # Application launcher
run_restaurant.py      # Alternative application launcher
```

## File Details

### Core Classes
- **`restro/models.py`**: Contains essential data models:
  - `MenuItem`: Represents food/drink items with name, price, and category
  - `Order`: Manages order information, calculation of total price, and timestamps

- **`restro/customer.py`**: Implements the Customer class with functionality for:
  - Viewing the restaurant menu
  - Placing orders with available balance check
  - Adding funds to balance
  - Viewing order history

- **`restro/admin.py`**: Implements the Admin class with administrative capabilities:
  - Authentication with username/password
  - Menu management (add/remove items, update prices)
  - Customer account management (add/view/remove)

- **`restro/restaurant.py`**: Core restaurant management functionality:
  - Stores and manages the menu collection
  - Handles customer database operations
  - Provides customer lookup and menu operations

### Interface and Main Files
- **`restro/interface.py`**: User interface implementation:
  - Text-based menu system
  - User input handling and validation
  - Navigation between different features
  - Display formatting for data presentation

- **`restro/main.py`**: Application initialization:
  - Creates the Interface instance
  - Starts the main application loop

- **`restro/__init__.py`**: Package configuration:
  - Imports and exports classes for easier access
  - Defines the package structure

### Launcher Files
- **`app.py`**: Minimal launcher that imports and runs the main function
- **`run_restaurant.py`**: Alternative launcher that directly creates the interface

## Getting Started

### Prerequisites
- Python 3.6 or higher

### Installation
1. Clone this repository or download the code
2. Navigate to the project directory

### Running the Application
You can run the application using either of the following commands:

```bash
python3 app.py
```

or

```bash
python3 run_restaurant.py
```

## Usage Guide

### First-time Setup
When you first run the application, you'll see a main menu with these options:
1. Admin Login
2. Customer Login
3. Register as New Customer
4. Exit

### Admin Access
- Default admin credentials:
  - Username: `admin`
  - Password: `admin123`

### As an Admin, you can:
- Add new menu items with name, price, and category
- Remove menu items
- Update menu item prices
- View the complete menu
- View all registered customers
- Remove customer accounts

### As a Customer, you can:
- Register a new account (name, email, address)
- Login with your customer ID
- View the restaurant menu
- Place orders
- Check your order history
- Add funds to your balance

## Development

This project uses a simple object-oriented structure with classes that represent the main entities in a restaurant management system: `Restaurant`, `Admin`, `Customer`, `MenuItem`, and `Order`.

The interface is handled by the `Interface` class which provides a command-line interactive menu system.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Created as a Python programming exercise
- Designed for educational purposes to demonstrate object-oriented programming concepts
