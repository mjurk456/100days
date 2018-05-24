"""
100 DAYS OF PROGRAMMING CHALLENGE
+++++++ DAY 6 ++++++++

Write a program that calculates and prints the value according
to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H: C is 50. H is 30.
D is the variable whose values should be input to your program
in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence
is given to the program:
100,150,180
The output of the program should be:
18,22,24
"""

import math, importlib
module_list = importlib.import_module("4 List and tuple from user input")


class FormulaFromInput(module_list.ListAndTupleFromInput):
    def __init__(self, sequence = ""):
        self.C = 50
        self.H = 30
        self.text = sequence


    def count_formula(self):
        temp = []
        for item in self.text_to_list():
            try:
                item = float(item)
                result = int(math.sqrt((2 * self.C * item) / self.H))
                temp.append(str(result))
            except ValueError:
                pass
        return ", ".join(temp)

    
def main():
    while True:
        usrInput = input("Input a comma-separated number sequence or END to quit: \n? ")
        if usrInput.strip().upper() == "END":
            print("Bye!")
            return
        else:
            a = FormulaFromInput(usrInput)
            print(a.count_formula())


if __name__ == "__main__":
    main()
