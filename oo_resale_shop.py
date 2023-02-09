"""
   Filename: oo_resale_shop.py
Description: Academic project A1 for the class CSC 120: Object Oriented Programming, prof. R. Jordan Crouser. This file contains the class written for an imagined resale shop, with all the appropriate functions.
     Author: Linh Pham (@lpham-creator)
       Date: 8 Feb 2023

"""
from computer import Computer
from typing import Dict, Union, Optional
#change inventory to a list?
class ResaleShop:

    inventory : Dict[int, Dict[str, Union[str, int, bool]]] = {}
    itemID = 0

    def __init__(self, inventory: dict, itemID: int) -> None:
        self.inventory = inventory
        self.itemID = itemID
    
    def buy(self, x: Computer) -> None:
        self.itemID += 1 # increment itemID
        self.inventory[self.itemID] = x
        return x.description

    def update_price(self, itemID: int, new_price: float) -> None:
        if itemID in self.inventory:
            self.inventory[itemID].price = new_price
        else: 
            print("Item", itemID, "not found. Cannot update price.")
    
    def sell(self, itemID:int) -> None:
        if itemID in self.inventory:
            del self.inventory[itemID]
            self.itemID -= 1
            print("Item", itemID, "sold!")
        else: 
            print("Item", itemID, "not found. Please select another item to sell.")
    
    def print_inventory(self) -> str:
    # If the inventory is not empty
        if self.inventory:
        # For each item
            for itemID in self.inventory:
                # Print its details
                print(f'Item ID: {itemID} : {self.inventory[itemID].getInfo()}')
        else:
            print("No inventory to display.")
    
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


