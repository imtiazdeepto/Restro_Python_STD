"""
Main entry point for the Restaurant Management System application.
"""
from restro.interface import Interface


def main():
    """Run the Restaurant Management System application."""
    interface = Interface()
    interface.run()


if __name__ == "__main__":
    main()
