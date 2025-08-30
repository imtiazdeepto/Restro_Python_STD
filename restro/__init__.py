"""
Package initialization file for the restaurant management system.
"""
from .models import MenuItem, Order
from .customer import Customer
from .admin import Admin
from .restaurant import Restaurant
from .interface import Interface

__all__ = [
    'MenuItem',
    'Order',
    'Customer',
    'Admin',
    'Restaurant',
    'Interface'
]
