# Write your solution here
number1 = float (input ("How many times a week do you eat at the student cafeteria? "))
number2 = float (input ("The price of a typical student lunch? "))
number3 = float (input ("How much money do you spend on groceries in a week? "))

weekly = number3 + number1 * number2
daily = weekly / 7
print (f"Average food expenditure:")
print (f"Daily: {daily} euros")
print (f"Weekly: {weekly} euros")