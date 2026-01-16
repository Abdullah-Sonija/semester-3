class Account:
    def __init__(self):
        self.__accountNo = None
        self.__accountBal = None
        self.__securityCode = None

    def setData(self, accNo, accBal, secCode):
        self.__accountNo = accNo
        self.__accountBal = accBal
        self.__securityCode = secCode

    def displayData(self):
        print("Account Details:")
        print(f"Account Number: {self.__accountNo}")
        print(f"Account Balance: {self.__accountBal}")
        print(f"Security Code: {self.__securityCode}")


a1 = Account()
a1.setData(12345, 25000, "SonijaOM12")
a1.displayData()
