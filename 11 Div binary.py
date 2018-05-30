"""
100 DAYS OF PROGRAMMING CHALLENGE
+++++++ DAY 11 ++++++++
Question:
Write a program which accepts a sequence of comma separated 4 digit
binary numbers as its input and then check whether they are divisible by 5
or not. The numbers that are divisible by 5 are to be printed
in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
"""

def check_div(sequence, div):
    result = []
    for item in sequence:
        
        if item % div == 0:
            result.append(bin(item)[2:])
    return result


def check_bin(sequence):
    result = []
    for item in sequence:
        if len(item) == 4:
            try:
                result.append(int(item, 2))
            except ValueError:
                pass
    return result


def main():
    numbers = input("Input binary numbers divided by comma: ? ").split(",")
    numbers = check_bin(numbers)
    if len(numbers) == 0:
        print("Wrong input")
        return
    else:
        a = check_div(numbers, 5)
        if len(a) == 0:
            print("There are no numbers dvisible by 5")
        elif len(a) == 1:
            print(a[0])
        else:
            print(", ".join(a))
        

if __name__ == "__main__":
    main()

    
