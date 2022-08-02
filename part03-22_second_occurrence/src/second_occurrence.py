# Write your solution here
input_string = input("Please type in a string: ")
input_substring = input("Please type in a substring: ")
count = 0

index = input_string.find(input_substring)
while index <= len(input_string):
    if input_string[index:index + len(input_substring)] == input_substring:
        count += 1
        if count <= 2:
            result = index
            index = index + len (input_substring) - 1

    index += 1
if count >= 2:
    print(f"The second occurrence of the substring is at index {result}.")

else:
    print ("The substring does not occur twice in the string.")