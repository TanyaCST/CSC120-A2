from computer import Computer,  __init__, computerInfo, price_change, system_update

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

        if new_price != self.price:
            self.price = price_change(new_price)

    # Refurbuish computer's system
    def refurbish_system(self, system:str):
        if system != self.operating_system:
            self.operating_system = system_update(system)



    def main():
        # Gather computer info
        computer_description = __init__("Mac Pro (Late 2013)",
                                         "3.5 GHc 6-Core Intel Xeon E5",
                                        1024, 
                                        64,
                                        "macOS Big Sur", 
                                        2013, 
                                        1500)
        
        # Store information into the inventory
        computer1 = computerInfo(computer_description)

        # Print out inventory
        print(computer1)

        # Change price of

    main()