"""
100 DAYS OF PROGRAMMING CHALLENGE
+++++++ DAY 5 ++++++++
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
"""

class StupidClass:

    def __init__(self, inputMsg = ""):
        self.stringVar = ""
        self.inputMsg = inputMsg


    def get_string(self, inputMsg = None):
        if inputMsg: self.inputMsg = inputMsg
        self.stringVar = input(self.inputMsg)


    def print_string(self):
        print(self.stringVar.upper())


def main():
    stuff = StupidClass()
    stuff.get_string("? ")
    stuff.print_string()


if __name__ == "__main__":
    main()
