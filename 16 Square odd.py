"""
100 DAYS OF PROGRAMMING CHALLENGE
+++++++ DAY 16 ++++++++
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
"""

def main():
    while True:
        usrList = input("Input a list of comma-separated numbers or press Enter to exit: ? ").split(",")
        if usrList == ['']:
            return
        try:
            numbers = [int(i) for i in usrList]
            break
        except ValueError:
            print("Supplied list is not correct. Try one more time")
    print(", ".join([str(i*i) for i in numbers if i%2 == 1]))


if __name__ == "__main__":
    main()
            
