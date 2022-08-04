# Write your solution here

lst = []
while True:
    print(f"The list is now {lst}")
    action = input("a(d)d, (r)emove or e(x)it: ")
    if action == "x":
        print("Bye!")
        break
    elif action == "d":
        lst.append(len(lst) + 1)
    elif action == "r":
        lst.remove(len(lst))

   