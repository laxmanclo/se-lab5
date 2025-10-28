"""Inventory management system with proper error handling and security."""
import json
from datetime import datetime


# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """
    Add items to inventory.

    Args:
        item: Item name (string)
        qty: Quantity to add (integer)
        logs: Optional list to log operations
    """
    if logs is None:
        logs = []

    if not isinstance(item, str):
        raise TypeError("Item must be a string")
    if not isinstance(qty, int):
        raise TypeError("Quantity must be an integer")
    if not item:
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """
    Remove items from inventory.

    Args:
        item: Item name
        qty: Quantity to remove
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Error: Item '{item}' not found in inventory")


def get_qty(item):
    """
    Get quantity of an item.

    Args:
        item: Item name

    Returns:
        Quantity of item
    """
    try:
        return stock_data[item]
    except KeyError:
        print(f"Error: Item '{item}' not found")
        return 0


def load_data(file_path="inventory.json"):
    """
    Load inventory data from JSON file.

    Args:
        file_path: Path to JSON file
    """
    global stock_data  # pylint: disable=global-statement
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            stock_data = json.load(file)
    except FileNotFoundError:
        print(f"Warning: {file_path} not found, starting fresh")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {file_path}")


def save_data(file_path="inventory.json"):
    """
    Save inventory data to JSON file.

    Args:
        file_path: Path to JSON file
    """
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(stock_data, file, indent=2)


def print_data():
    """Print current inventory report."""
    print("Items Report")
    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")


def check_low_items(threshold=5):
    """
    Check for items below threshold.

    Args:
        threshold: Minimum quantity threshold

    Returns:
        List of items below threshold
    """
    result = []
    for item, quantity in stock_data.items():
        if quantity < threshold:
            result.append(item)
    return result


def main():
    """Main function to demonstrate inventory system."""
    add_item("apple", 10)
    add_item("banana", 2)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    print('Safe alternative to eval')


if __name__ == "__main__":
    main()
