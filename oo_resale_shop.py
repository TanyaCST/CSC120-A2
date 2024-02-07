from computer import Computer

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
        comp = Computer(self)

        # 2. Add computer information into inventory
        self.inventory.append(comp)

    # Sell Computers
    def sell(self):
        # 1. Call Computer Constructor
        comp = Computer(self)

        # 2. Remove computer information into inventory
        self.inventory.remove(comp)

    # Print the inventory
    def print_inventory(self):
        return self.inventory
    
    # Refurbish the computer
    # Refurbish computer's price
    def refurbuish_price(self, price:int):
        # new_price = 
        self.inventory

    # Refurbish computer's system
    # def refurbuish_os(self):

    def main():
        print()

    main()