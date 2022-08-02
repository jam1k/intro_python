# Write your solution here

year = int(input ("Year: "))
modulo = year % 4
addition = 4 - modulo


if modulo != 0:
    if (year + addition) % 100 == 0:
        if (year + addition) % 400 == 0:
            print (f"The next leap year after {year} is {year + addition}")
        else:
            print (f"The next leap year after {year} is {year + addition + 4}")
    else:
        print (f"The next leap year after {year} is {year + addition}")
else:
    if (year + 4) % 100 != 0:
        print (f"The next leap year after {year} is {year + 4}")
    else:
        print (f"The next leap year after {year} is {year + 8}")

