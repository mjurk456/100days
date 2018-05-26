"""
100 DAYS OF PROGRAMMING CHALLENGE
+++++++ DAY 7 ++++++++
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
"""


def main():
    while True:
        try:
            row, col = map(int, input("Input comma-separated " + \
                     "numbers of rows and columns for an array, e.g. 5,3: ? ").split(","))
            array = [[x*y for x in range(col)] for y in range(row)]
            print(array)
            return
        except ValueError:
            print("Wrong input.")
            

if __name__ == "__main__":
    main()
