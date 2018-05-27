"""
100 DAYS OF PROGRAMMING CHALLENGE
+++++++ DAY 10 ++++++++
Write a program that accepts a sequence of whitespace separated words
as input and prints the words after removing all duplicate words
and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
"""


def remove_duplicates(text, separator):
    return separator.join(sorted(set(text.split(separator))))


def main():
    userInput = input("Input whitespace separated words: ? ")
    print(remove_duplicates(userInput, " "))


if __name__ == "__main__":
    main()
