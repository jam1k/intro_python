# Write your solution here

my_str1 = input("Please type in string 1: ")
my_str2 = input("Please type in string 2: ")

if (len(my_str1) > len(my_str2)):
    print(f"{my_str1} is longer")

elif (len(my_str2) > len(my_str1)):
    print(f"{my_str2} is longer")
else:
    print("The strings are equally long")