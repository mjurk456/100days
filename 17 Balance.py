"""
100 DAYS OF PROGRAMMING CHALLENGE
+++++++ DAY 17 ++++++++
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
"""

class BankAccount:

    
    def __init__(self, transactionList = [], debit = "D", credit = "C"):
        self.transactionList = transactionList
        self.debit = debit
        self.credit = credit


    def upload_file(self, filePath):
        try:
            f = open(filePath)
            self.transactionList = f.readlines()
            f.close()
        except FileNotFoundError:
            print("Wrong file name")


    def set_transaction_list(self, array):
        self.transactionList = array
       

    def balance(self):
        total = 0
        for i in range(0, len(self.transactionList)):
            try:
                dc, amount = self.transactionList[i].split(" ")
                if dc == self.debit:
                    total = total + float(amount)
                elif dc == self.credit:
                    total = total - float(amount)
                else:
                    raise ValueError
            except ValueError:
                print("Errors on line #{0} {1}, it will be ignored".format(i, self.transactionList[i]))
                continue
        return total


def main():
    usrDt = input("Input a symbol for a debit entry, e.g. D: ? ").strip()
    usrCr = input("Input a symbol for a credit entry, e.g. C: ? ").strip()
    bank = BankAccount([],usrDt, usrCr)
    usrMode = input("Choose 1 for manual input, 2 for uploading a text file: ? ").strip()
    if usrMode == "1":
        print("Input text. Ctrl+D to save it:")
        text = []
        while True:
            try:
                line = input("? ")
            except EOFError:
                break
            text.append(line)
        bank.set_transaction_list(text)
        print("Your balance is: {0}".format(bank.balance()))
    elif usrMode == "2":
        usrFile = input("Input a full path to TXT file: ? ")
        bank.upload_file(usrFile)
        print("Your balance is: {0}".format(bank.balance()))
    else:
        print("Wrong choice")
        return


if __name__ == "__main__":
    main()
