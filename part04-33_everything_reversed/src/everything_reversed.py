# Please write a function named everything_reversed, which takes a list of strings as its argument. 
# The function returns a new list with all of the items on the original list reversed. 
# Also the order of items should be reversed on the new list.
# Write your solution here

from unittest import result


def everything_reversed(lst:list):
    result = [string[::-1] for string in lst]
    return result[::-1]