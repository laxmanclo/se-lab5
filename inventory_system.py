"""Inventory management system with proper error handling and security."""
import json
from datetime import datetime


# Global variable
stock_data = {}


def addItem(item="default", qty=0, logs=None):
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


def removeItem(item, qty):
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


def getQty(item):
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


def loadData(file_path="inventory.json"):
    """
    Load inventory data from JSON file.
    
    Args:
        file_path: Path to JSON file
    """
    global stock_data
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            stock_data = json.load(file)
    except FileNotFoundError:
        print(f"Warning: {file_path} not found, starting fresh")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {file_path}")


def saveData(file_path="inventory.json"):
    """
    Save inventory data to JSON file.
    
    Args:
        file_path: Path to JSON file
    """
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(stock_data, file, indent=2)


def printData():
    """Print current inventory report."""
    print("Items Report")
    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")


def checkLowItems(threshold=5):
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
    addItem("apple", 10)
    addItem("banana", 2)
    # Fixed: removed invalid type call
    removeItem("apple", 3)
    removeItem("orange", 1)
    print("Apple stock:", getQty("apple"))
    print("Low items:", checkLowItems())
    saveData()
    loadData()
    printData()
    # Fixed: removed dangerous eval()
    print('Safe alternative to eval')


if __name__ == "__main__":
    main()
