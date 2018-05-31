"""
100 DAYS OF PROGRAMMING CHALLENGE
+++++++ DAY 12 ++++++++
Write a program, which will find all such numbers
between 1000 and 3000 (both included) such that each digit of the number
is an even number.
The numbers obtained should be printed in a comma-separated
sequence on a single line.
"""

import timeit

def in_set(lowerLimit, upperLimit, symbol):
    temp = []
    even = "02468"
    for i in range(lowerLimit, upperLimit + 1):
        a = str(i)
        if (a[0] in even) and (a[1] in even) \
           and (a[2] in even) and (a[3] in even):
            temp.append(str(i))
    return symbol.join(temp)


def dividing(lowerLimit, upperLimit, symbol):
    temp = []
    for i in range(lowerLimit, upperLimit + 1):
        if ((i // 1000) % 2 == 0) \
           and ((i % 1000 // 100) % 2 == 0) \
           and ((i % 1000 % 100 // 10) % 2 == 0) \
           and ((i % 1000 % 100 % 10) % 2 == 0):
            temp.append(str(i))
    return symbol.join(temp)


if __name__ == "__main__":
    print("Dividing approach: %f sec" % timeit.timeit(lambda: dividing(1000, 3000, ","), number=1000))
    print(dividing(1000, 3000, ","))
    print("In-set approach: %f sec" % timeit.timeit(in_set(1000, 3000, ","), number=1000))
    print(in_set(1000, 3000, ","))
