"""
100 DAYS OF PROGRAMMING CHALLENGE
+++++++ DAY 9 ++++++++
Write a program that accepts sequence of lines as input and prints
the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
"""

def main():
    print("Input text. Ctrl+D to save it")
    text = []
    while True:
        try:
            line = input("? ")
        except EOFError:
            break
        text.append(line.upper())
    print("\n".join(text))


if __name__ == "__main__":
    main()
        
