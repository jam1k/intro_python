# Write your solution here
input_string = input ("Please type in a string: ")
index = 0
string_length = len(input_string)
while index <= string_length:
    if index != 0:
        print (input_string[0:index])
    index += 1