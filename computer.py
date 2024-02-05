class Computer:

    # What attributes will it need?
    # Description of computers.
    description: str

    # Operating System of computers.
    operating_system: str

    # How will you set up your constructor?
    # Type self in the parenthesis and assign the parameters info and os into description and operating_system.

    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, info, os):
        self.description = info
        self.operating_system = os

    # What methods will you need?
    # Chaning the Operating System of computer.
    def refurbish_os(self, os):
        self.operating_system = os