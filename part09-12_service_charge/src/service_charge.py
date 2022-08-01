# WRITE YOUR SOLUTION HERE:
class BankAccount:
    def __init__(self, owner_name:str, account_number:str, balance:float):
        self.__owner_name = owner_name
        self.__accountnum = account_number
        self.__balance = balance

        @property
        def owner_name(self):
            return self.__owner_name
        
        @owner_name.setter
        def owner_name(self, owner_name):
            self.__owner_name=owner_name
        

        @property
        def accountnum(self):
            return self.__accountnum

        @accountnum.setter
        def accountnum (self, account_number):
            self.__accountnum = account_number

    def deposit(self, amount: float):
        if amount>0:
            
            self.__balance += amount
            self.__balance = self.__service_charge()
        else:
            raise ValueError ("Cannot deposit negative amount")
        

    def withdraw(self, amount:float):
        if amount<0:
            raise ValueError("Cannout withdraw negative amount")
        else:
            if amount<=self.__balance:
                self.__balance-=amount
                self.__balance = self.__service_charge()
                

    @property
    def balance (self):
        return self.__balance
    
    @balance.setter
    def balance (self, amount):
        self.__balance = amount
    
    def __service_charge(self):
        return self.__balance*0.99


if __name__=="__main__":
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)