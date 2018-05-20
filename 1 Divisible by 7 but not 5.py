""" 100 DAYS OF PROGRAMMING CHALLENGE
+++++++ DAY 1 ++++++++
Write a program which will find
all such numbers which are divisible by 7
but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed
in a comma-separated sequence on a single line.
"""

def main():
    sequence = []
    startRange = 2000
    endRange = 3200
    numMultiplier = 7
    numNotMultiplier = 5
    for i in range (startRange, endRange + 1):
        if (i % numMultiplier == 0) \
           and (i % numNotMultiplier != 0):
            sequence.append(str(i))
    print(",".join(sequence))


if __name__ == "__main__":
    main()
    
           
