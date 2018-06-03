"""
100 DAYS OF PROGRAMMING CHALLENGE
+++++++ DAY 13 - 14 ++++++++
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
"""

import re

class sentence:
    def __init__(self, text = ""):
        self.text = text

    def calc_digits(self):
        return len(re.sub("\D", "", self.text))

    def calc_letters(self):
        return len(re.sub("\W", "", self.text)) - self.calc_digits()

    def calc_symbols(self):
        return len(self.text) - self.calc_letters() - self.calc_digits()

    def calc_upper(self):
        a = re.sub("\W", "", self.text)
        a = re.sub("\d", "", a)
        i = 0
        for letter in a:
            if letter.isupper():
                i = i + 1
        return i
        
    def calc_lower(self):
        a = re.sub("\W", "", self.text)
        a = re.sub("\d", "", a)
        i = 0
        for letter in a:
            if letter.islower():
                i = i + 1
        return i


def main():
    usrInput = input("Input a text: ? ")
    if len(usrInput) != "":
        a = sentence(usrInput)
        print("Digits: {0}".format(a.calc_digits()))
        print("Letters: {0}".format(a.calc_letters()))
        print("Other symbols: {0}".format(a.calc_symbols()))
        print("Uppercase symbols: {0}".format(a.calc_upper()))
        print("Lowercase symbols: {0}".format(a.calc_lower()))
    else:
        print("Wrong input")


if __name__ == "__main__":
    main()
