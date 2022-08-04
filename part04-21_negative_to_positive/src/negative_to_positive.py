# Write your solution here
number = int (input("Please type in a positive integer: "))
neg = (-1) * number

while (neg <= number):
    if (neg != 0):
        print (neg)
    neg += 1