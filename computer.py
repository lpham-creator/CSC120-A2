"""
   Filename: computer.py
Description: Academic project A1 for the class CSC 120: Object Oriented Programming, prof. R. Jordan Crouser. This file contains the class written for a computer and all the needed functions for that class.
     Author: Linh Pham (@lpham-creator)
       Date: 8 Feb 2023
"""

""" The class Computer, which contains a constructor and one method, mimics the attributes of a real computer.\
"""
class Computer:

    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, starting_price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = starting_price
    
    """
    Returns all the attributes of a computer
    """
    def getInfo(self):
        return self.description, self.processor_type, self.hard_drive_capacity, self.memory, self.operating_system, self.year_made, self.price

