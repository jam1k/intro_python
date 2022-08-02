# Write your solution here

input_string = input ("Please type in a word: ")
char = input ("Please type in a character: ")

index = input_string.find (char)
if index + 3 < len(input_string):
    print(input_string[index:index + 3])