"""100 DAYS OF PROGRAMMING CHALLENGE
+++++++ DAY 15 ++++++++
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
"""

try:
    a = int(input("Input a random integer number: ? "))
    print(eval('{0}+{0}{0}+{0}{0}{0}+{0}{0}{0}{0}'.format(a)))
except ValueError:
    print("Given value was incorrect")
    
