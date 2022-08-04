# Please write a function named no_vowels, which takes a string argument. 
# The function returns a new string, which should be the same as the original but with all vowels removed.
# You can assume the string will contain only characters from the lowercase English alphabet a...z.
# Write your solution here

def no_vowels(string: str):
    vowels = "aeiou"
    result = [letter for letter in string if letter not in vowels]
    return ''.join(result)