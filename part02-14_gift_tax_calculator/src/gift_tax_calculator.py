# Write your solution here# Write your solution here

gift = int (input("Value of gift: "))
tax = 0

if gift >= 1000000:
    tax= 142100 + (gift - 1000000) * 0.17

elif gift >= 200000:
    tax = 22100 + (gift - 200000) * 0.15

elif gift >= 55000:
    tax = 4700 + (gift - 55000) * 0.12

elif gift >= 25000:
    tax = 1700 + (gift - 25000) * 0.1

elif gift >= 5000:
    tax = 100 + (gift - 5000) * 0.08

if tax == 0:
    print ("No tax!")

else:
    print (f"Amount of tax: {tax} euros")