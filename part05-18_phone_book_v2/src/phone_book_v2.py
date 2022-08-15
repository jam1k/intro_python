# Please write an improved version of the phone book application. Each entry should now accommodate multiple phone numbers. 
# The application should work otherwise exactly as above, but this time all numbers attached to a name should be printed.
# Write your solution here
phone_book = {}
while True:
    command = input("command (1 search, 2 add, 3 quit): ")
    if command == "3":
        print("quitting...")
        break
    elif command == "1":
        search_name = input("name: ")
        if search_name in phone_book:
            for num in phone_book[search_name]:
                print (num)
        else:
            print("no number")
    elif command == "2":
        name = input("name: ")
        number = input("number: ")
        if name not in phone_book:
            phone_book[name] = [number]
        else:
            phone_book[name].append(number)
        print("ok!")