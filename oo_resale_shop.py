from computer import Computer,  __init__, priceChange, systemUpdate

class ResaleShop:

    # What attributes will it need?
    inventory: list

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self,
                 inventory: list):
        self.inventory = []

    # What methods will you need?
    # Buy computers
    def buy(self, c:Computer):
        self.inventory.append(c)

    # Sell Computers
    def sell(self, c:Computer):
        self.inventory.remove(c)

    # Print the inventory
    def printInventory(self):
        return self.inventory
    
    # Refurbish computer's price
    def refurbuishPrice(self, new_price:int):

        if new_price != self.price:
            self.price = priceChange(new_price)

    # Refurbuish computer's system
    def refurbishSystem(self, system:str):
        if system != self.operating_system:
            self.operating_system = systemUpdate(system)



    def main():
        # Gather computer info
        computerDescription = __init__("Mac Pro (Late 2013)",
                                         "3.5 GHc 6-Core Intel Xeon E5",
                                        1024, 
                                        64,
                                        "macOS Big Sur", 
                                        2013, 
                                        1500)
        
        # Store information into the inventory
        computer1 = computerDescription

        # Print out inventory
        print(computer1)

        # Change price of

    main()