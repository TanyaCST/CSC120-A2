from computer import Computer, computerInfo, price_change, system_update

class ResaleShop:

    # What attributes will it need?
    inventory: list

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self,
                 inventory: list):
        self.inventory = inventory

    # What methods will you need?
    # Buy computers
    def buy(self):
        # 1. Call Computer Constructor
        comp = computerInfo(self)

        # 2. Add computer information into inventory
        self.inventory.append(comp)

    # Sell Computers
    def sell(self):
        # 1. Call Computer Constructor
        comp = computerInfo(self)

        # 2. Remove computer information into inventory
        self.inventory.remove(comp)

    # Print the inventory
    def print_inventory(self):
        return self.inventory
    
    # Refurbish computer's price
    def refurbuish_price(self, new_price:int):

        if new_price != Computer(self.price):
            self.price = price_change(new_price)

    # Refurbuish computer's system
    def refurbish_system(self, system:str):
        if system != Computer(self.operating_system):
            self.operating_system = system_update(system)



    def main():
        print()

    main()