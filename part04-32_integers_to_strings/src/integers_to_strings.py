# Please write a function named formatted, which takes a list of floating point numbers as its argument. 
# The function returns a new list, which contains each element of the original list in string format, rounded to two decimal points. 
# The order of the items in the list should remain unchanged.
# Write your solution here

def formatted(lst: list):
    return [f"{num:.2f}" for num in lst]