# Please write a function named length_of_longest, which takes a list of strings as its argument. 
# The function returns the length of the longest string.
# Write your solution here

def length_of_longest(lst: list):
    return max([len(string) for string in lst])