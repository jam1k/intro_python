# Please write a function named most_common_character, which takes a string argument. 
# The function returns the character which has the most occurrences within the string. 
# If there are many characters with equally many occurrences, the one which appears first in the string should be returned.
# Write your solution here

def most_common_character(string: str):
    max_count = 0
    for letter in string:
        print (string.count(letter))
        if string.count(letter) > max_count:
            max_count = string.count(letter)
            result = letter
    return result
