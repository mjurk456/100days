"""
100 DAYS OF PROGRAMMING CHALLENGE
+++++++ DAY 2 ++++++++
Write a program which can compute the factorial
of a given numbers.
The results should be printed in a comma-separated sequence
on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question,
it should be assumed to be a console input.
"""

import math

def cheating_factorial(startNumber):
    return math.factorial(startNumber)


def non_recursion_factorial(startNumber):
    if startNumber == 0:
        return 1
    f = 1
    for i in range(startNumber, 1, -1):
        f = f * i
    return f


def recursion_factorial(startNumber):
    if startNumber == 0:
        return 1
    else:
        return recursion_factorial(startNumber - 1) * startNumber


def check_input(n):
    if not n.isdigit():
        return False
    else:
        #getting non-negative integer number
        return round(abs(int(n)), 0)


def main():
    while True:
        userInput = input("Input an integer non-negative number or END to quit: ? ").lower().strip()
        if userInput == "end":
            print("Bye!")
            return
        else:
            if check_input(userInput) == False:
                print("Wrong input!")
            else:
                n = check_input(userInput)
                print("Non-recursive factorial: %d" % non_recursion_factorial(n))
                print("Recursive factorial: %d" % recursion_factorial(n))
                print("Cheating factorial: %d" % cheating_factorial(n))


if __name__ == "__main__":
    main()
