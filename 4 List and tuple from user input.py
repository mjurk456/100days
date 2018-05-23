"""
100 DAYS OF PROGRAMMING CHALLENGE
+++++++ DAY 4 ++++++++
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""

import re

class ListAndTupleFromInput:

    def __init__(self, text=""):
        #all symbols except numbers, comma, dot and minus
        #will be excluded
        self.text = re.sub("[^0-9,.-]", "", text)


    def text_to_list(self):
        return self.text.split(",")


    def text_to_tuple(self):
        return tuple(self.text.split(","))


def main():
    while True:
        userInput = input("Input a sequence of comma-separated numbers or END to exit: ? ")
        if userInput.upper().strip() == "END":
            print("Bye!")
            return
        elif userInput != "":
            sequence = ListAndTupleFromInput(userInput)
            print(sequence.text_to_list())
            print(sequence.text_to_tuple())


if __name__ == "__main__":
    main()
    
