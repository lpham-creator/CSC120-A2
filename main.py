from computer import *
from oo_resale_shop import *
# Import a few useful containers from the typing module
from typing import Dict, Union

# Import the functions we wrote in procedural_resale_shop.py
from procedural_resale_shop import buy, update_price, sell, print_inventory, refurbish

""" This helper function takes in a bunch of information about a computer,
    and packages it up into a python dictionary to make it easier to store

    Note: because python is dynamically typed, you may not be used to seeing 
    explicit data types (str, int, etc.) listed in a python function. We're 
    going to go the extra step, because when we get to Java it'll be required!
"""
def create_computer(description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
    return {'description': description,
            'processor_type': processor_type,
            'hard_drive_capacity': hard_drive_capacity,
            'memory': memory,
            'operating_system': operating_system,
            'year_made': year_made,
            'price': price
    }

def main():
    
    # First, let's make a computer
    computer = create_computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )

    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Add it to the resale store's inventory
    print("Buying", computer["description"])
    print("Adding to inventory...")
    computer_id = buy(computer)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    print_inventory()
    print("Done.\n")

    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
    print("Updating inventory...")
    refurbish(computer_id, new_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    print_inventory()
    print("Done.\n")
    
    # Now, let's sell it!
    print("Selling Item ID:", computer_id)
    sell(computer_id)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    print_inventory()
    print("Done.\n")

    comp1 = Computer("Mac Pro (Late 2013)" ,"3.5 GHc 6-Core Intel Xeon E5", 1024 , 64 ,"macOS Big Sur" , 2013 , 1500)
    comp2 = Computer("Mac Pro (Late 2013)" ,"3.5 GHc 6-Core Intel Xeon E4", 1024 , 64 ,"macOS Big Sur" , 2013 , 1500)
    comp3 = Computer("Mac Pro (Late 2013)" ,"3.5 GHc 6-Core Intel Xeon E3", 1024 , 64 ,"macOS Big Sur" , 2013 , 1500)
    print(comp1)
    print("Computer memory is", comp1.memory)

    shop1 = ResaleShop({},0)
    print("We are buying", ResaleShop.buy(shop1,comp1))
    print(ResaleShop.update_price(shop1, 1, 3000))
    print(ResaleShop.sell(shop1,1))
    print(ResaleShop.print_inventory(shop1))
    ResaleShop.buy(shop1,comp1)
    ResaleShop.buy(shop1,comp2)
    ResaleShop.buy(shop1,comp3)
    print(ResaleShop.sell(shop1,1))
    print(ResaleShop.refurbish(shop1,2,"macOS 13: Ventura (Rome)"))
    print(ResaleShop.print_inventory(shop1))
    print(comp2.getInfo())




# Calls the main() function when this file is run
if __name__ == "__main__": main()
