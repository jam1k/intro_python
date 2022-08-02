# Write your solution here

input_string = input ("Please type in a string: ")

string_length = len(input_string)
start = string_length - 1
end = string_length

while start >= 0:
    print(input_string[start:end])
    start -= 1