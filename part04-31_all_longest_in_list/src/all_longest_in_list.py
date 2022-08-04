# Please write a function named all_the_longest, which takes a list of strings as its argument. 
# The function should return a new list containing the longest string in the original list. 
# If more than one are equally long, the function should return all of the longest strings.
# The order of the strings in the returned list should be the same as in the original.
# Write your solution here

def all_the_longest(lst: list):
    max_str = ""
    for string in lst:
        if max_str == "" or len(string) > len(max_str):
            max_str = string
    return [string for string in lst if len(string) == len(max_str)]
