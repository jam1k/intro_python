# Write your solution here
a = [1, 2, 3, 4, 5]
while True:
    index = int(input("Index: "))
    if index == -1:
        break
    elif index < 0 or index >= len(list):
        print("Index is outside of the range of the list")
        continue
    new_value = int(input("New value: "))
    a[index] = new_value
    print (a)

