class Computer:

    # What attributes will it need?
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, starting_price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = starting_price
    
    def getInfo(self):
        return self.description, self.processor_type, self.hard_drive_capacity, self.memory, self.operating_system, self.year_made, self.price

