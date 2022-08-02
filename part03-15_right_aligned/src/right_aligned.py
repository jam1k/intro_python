# Write your solution here

input_string = input ("Please type in a string: ")
length = len (input_string)

if length < 20:
    print ((20 - length) * "*" + input_string)