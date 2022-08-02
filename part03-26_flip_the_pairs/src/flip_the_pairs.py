# Write your solution here
number = int(input("Please type in a number: "))
i = 1
while i < number:
    j = i
    i += 1
    print (i)
    print (j)
    i += 1

if number % 2 != 0:
    print (number)
