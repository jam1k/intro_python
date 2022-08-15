# Please write a phone book application. 
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
            print (phone_book[search_name])
        else:
            print("no number")
    elif command == "2":
        name = input("name: ")
        number = input("number: ")
        phone_book[name] = number
        print("ok!")