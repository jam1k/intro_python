lim = int(input("Limit: "))

i = 1
sum = 0
result = ""
while (sum < lim):
    sum = sum + i
    if (i != 1):
        result += f" + {i}"
    else:
        result += f"{i}"
    i+=1

result += f" = {sum}"
print(f"The consecutive sum: {result}")