class ResaleShop:

    # What attributes will it need?
    inventory = [] #Computer objects will go over there
    price: float
    


    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, computer_obj, original_price):
        self.inventory = computer_obj # You'll remove this when you fill out your constructor
        self.price = original_price

    # What methods will you need?
    # Buy a conputer --- add an inventory
    def add_inventory(self, computer_obj):
        self.inventory.append(computer_obj)

    # Sell a computer --- remove an inventory
    def remove_inventory(self, computer_obj):
        self.inventory.remove(computer_obj)

    # Change price of computers
    def price_change(self, changed_price):
        self.price = changed_price
