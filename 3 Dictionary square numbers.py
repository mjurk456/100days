"""
100 DAYS OF PROGRAMMING CHALLENGE
+++++++ DAY 3 ++++++++
With a given integral number n, write a program to generate
a dictionary that contains (i, i*i) such that is an integral number
between 1 and n (both included). And then the program should print
the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""

def up_to_x_dictionary(n):
    result = {}
    for i in range (1, n + 1):
        result[i] = i * i
    return result


def one_liner(n):
    return {i: i ** 2 for i in range(1, n + 1)}


def main():
    while True:
        userInput = input("Input a positive integer number " +
                        "or END to quit: ? ").strip().upper()
        if userInput == "END":
            print("Bye!")
            return
        elif not userInput.isdigit():
            print("Wrong input")
        else:
            print(up_to_x_dictionary(int(userInput)))
            print(one_liner(int(userInput)))


if __name__ == "__main__":
    main()
                         
    
