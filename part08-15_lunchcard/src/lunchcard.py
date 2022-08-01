# Write your solution here:

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"

    def eat_lunch(self):
        if self.balance >=2.60:
            self.balance-=2.60
    
    def eat_special(self):
        if self.balance>=4.60:
            self.balance-=4.60
    
    def deposit_money(self, deposit:float):
        if deposit<0:
            raise ValueError("You cannot deposit an amount of money less than zero")
                    
        self.balance+=deposit


peter_card = LunchCard(20)
grace_card = LunchCard(30)

peter_card.eat_special()
grace_card.eat_lunch()

print (f"Peter: {peter_card}")
print (f"Grace: {grace_card}")

peter_card.deposit_money(20)
grace_card.eat_special()

print (f"Peter: {peter_card}")
print (f"Grace: {grace_card}")

peter_card.eat_lunch()
peter_card.eat_lunch()
grace_card.deposit_money(50)

print (f"Peter: {peter_card}")
print (f"Grace: {grace_card}")
