# Write your solution here
hourly_wage = float (input("Hourly wage: "))
hours = float (input("Hours worked: "))
week_day = input("Day of the week: ")

if week_day == "Sunday":
    result = 2 * hours * hourly_wage
else:
    result = hours * hourly_wage

print (f"Daily wages: {result} euros")