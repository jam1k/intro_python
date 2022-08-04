# Please write a function named palindromes, which takes a string argument and returns True if the string is a palindrome. 
# Palindromes are words which are spelled exactly the same backwards and forwards.
# Please also write a main function which asks the user to type in words until they type in a palindrome:

# Write your solution here
def palindromes(my_str: str):
    if my_str == my_str[::-1]:
        return True
    else: 
        return False
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

while True:
    my_str = input("Please type in a palindrome: ")
    if palindromes(my_str) == True:
        print(f"{my_str} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")