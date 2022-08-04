# Write your solution here

item_no = int(input("How many items: "))
i = 0
result = []
while (i < item_no):
    item = int(input(f"Item {i + 1}: "))
    result.append(item)
    i += 1
print (result)