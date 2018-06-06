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


class WrongValueException(Exception):
    """ Custom defined exception.
        Returns a number of line where an exception appeared.
    """
    def __init__(self, lineNo, lineText):
        Exception.__init__(self)
        self.lineNo = lineNo
        self.lineText = lineText
        

class BankAccount:

    
    def __init__(self, transactionList = [], debit = "D", credit = "C"):
        self.transactionList = transactionList
        self.debit = debit
        self.credit = credit


    def upload_file(self, filePath):
        """File Format should be:
           Dt Cr
           Dt 16
           Cr 13
        """
        f = open(filePath)
        self.transactionList = f.readlines()
        try:
            self.debit, self.credit = self.transactionList[0].split()
            self.transactionList.pop(0)
        except ValueError:
            raise WrongValueException(0, self.transactionList[0].strip())
            return None
        finally:
            f.close()
        

    def set_transaction_list(self, array):
        self.transactionList = array
       

    def balance(self):
        total = 0
        for i in range(0, len(self.transactionList)):
            try:
                dc, amount = self.transactionList[i].strip().split()
                if dc == self.debit:
                    total = total + float(amount)
                elif dc == self.credit:
                    total = total - float(amount)
                else:
                    raise WrongValueException(i, self.transactionList[i].strip())
                    return None
            except ValueError:
                raise WrongValueException(i, self.transactionList[i].strip())
                return None
        return total


def multiline_input(msg):
    #allows to input several lines. Ctrl+D breaks the cycle.
    #returns input values as a list
    text = []
    while True:
        try:
            line = input(msg)
        except EOFError:
            break
        text.append(line)
    return text



def main():
    bank = BankAccount([],'', '')
    usrMode = input("Choose 1 for manual input, 2 for uploading a text file: ? ").strip()
    if usrMode == "1":
        usrDt = input("Input a symbol for a debit entry, e.g. D: ? ").strip()
        usrCr = input("Input a symbol for a credit entry, e.g. C: ? ").strip()
        
        print("Input your list in format 'Dt 150'. Ctrl+D to save it:")
        text = multiline_input("? ")
        bank.set_transaction_list(text)
        
    elif usrMode == "2":
        usrFile = input("Input a full path to TXT file: ? ")
        try:
            bank.upload_file(usrFile)
        except FileNotFoundError:
            print("The file was not found.")
        except WrongValueException as ex:
            print("Wrong values on line # {0}: {1}.".format(ex.lineNo, ex.lineText))
            return None
    else:
        print("Wrong choice")
        return None
    try:
        print("Your balance is: {0}".format(bank.balance()))
    except WrongValueException as ex:
        print("Wrong values on line # {0}: {1}.".format(ex.lineNo, ex.lineText))
        


if __name__ == "__main__":
    main()
