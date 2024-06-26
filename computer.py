class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, 
                 description: str,
                 processor_type: str,
                 hard_drive_capacity: int,
                 memory: int,
                 operating_system: str,
                 year_made: int,
                 price: int):
        
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # What methods will you need?
    # Update the price
    def priceChange(self, new_price: int):
        if self.inventory.keys(self):
            self.price = new_price
        else:
            return "We don't have this computer in inventory"

    # Update the operating system
    def systemUpdate(self, new_system: str):
        if self.inventory.keys(self):
            self.operating_system = new_system
        else:
            return "We don't have this computer in inventory"

        
