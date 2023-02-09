"""
   Filename: oo_resale_shop.py
Description: Academic project A1 for the class CSC 120: Object Oriented Programming, prof. R. Jordan Crouser. This file contains the class written for an imagined resale shop, with all the appropriate functions.
     Author: Linh Pham (@lpham-creator)
       Date: 8 Feb 2023

"""
from computer import Computer
from typing import Dict, Union, Optional

""" The class ResaleShop, which contains a constructor and methods, mimics the operations of a real resale store.\
"""
class ResaleShop:
    """ inventory: a dictionary where we store the inventory
    The key is an int representing the item number
    The value is another dictionary containing information about the machine
    """
    inventory : Dict[int, Dict[str, Union[str, int, bool]]] = {}
    itemID = 0

    """The class constructor, which takes in the inventory and itemID as arguments
    """
    def __init__(self, inventory: dict, itemID: int) -> None:
        self.inventory = inventory
        self.itemID = itemID
    
    """
    Takes in an object of the Computer class,
    adds it to the inventory, returns the description of the object
    """
    def buy(self, x: Computer) -> None:
        self.itemID += 1 # increment itemID
        self.inventory[self.itemID] = x
        return x.description
    
    """
    Takes in an item_id and a new price, updates the price of the associated
    computer if it is the inventory, prints error message otherwise
    """
    def update_price(self, itemID: int, new_price: float) -> None:
        if itemID in self.inventory:
            self.inventory[itemID].price = new_price
        else: 
            print("Item", itemID, "not found. Cannot update price.")
    
    """
    Takes in an item_id, removes the associated computer if it is the inventory, 
    prints error message otherwise
    """
    
    def sell(self, itemID:int) -> None:
        if itemID in self.inventory:
            del self.inventory[itemID]
            self.itemID -= 1
            print("Item", itemID, "sold!")
        else: 
            print("Item", itemID, "not found. Please select another item to sell.")
    
    """
    Prints all the items in the inventory (if it isn't empty), prints error otherwise
    """
    def print_inventory(self) -> str:
    # If the inventory is not empty
        if self.inventory:
        # For each item
            for itemID in self.inventory:
                # Print its details
                print(f'Item ID: {itemID} : {self.inventory[itemID].getInfo()}')
        else:
            print("No inventory to display.")
    
    """Takes in an item ID and a new OS operating system, locates the computer in the inventory, modifies its price based on the year made, and 
    changes the operating system"""
    def refurbish(self, itemID:int, new_os) -> None:
        if itemID in self.inventory:
            Computer = self.inventory[itemID] # locate the computer
            if Computer.year_made < 2000:
                Computer.price = 0 # too old to sell, donation only
            elif Computer.year_made < 2012:
                Computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif Computer.year_made < 2018:
                Computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                Computer.price = 1000 # recent stuff

            if new_os is not None:
                Computer.operating_system = new_os # update details after installing new OS
        else:
            print("Item", itemID, "not found. Please select another item to refurbish.")


