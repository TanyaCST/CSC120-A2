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
    # Gather computer's information
    def computerInfo(self):
        # return the product description
        return {"description":self.description,
                "processor_type":self.processor_type,
                "hard_drive_capacity":self.hard_drive_capacity,
                "memory":self.memory,
                "operating_system":self.operating_system,
                "year_made":self.year_made,
                "price":self.price}

    # Update the price
    def price_change(self,
                     new_price: int):
        self.price = new_price

    # Update the operating system
    def system_update(self,
                      new_system: str):
        self.operating_system = new_system
        
