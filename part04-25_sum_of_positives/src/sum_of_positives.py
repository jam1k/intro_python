# Please write a function named sum_of_positives, which takes a list of integers as its argument. 
# The function returns the sum of the positive values in the list.
# Write your solution here

def sum_of_positives(lst: list):
    return sum([num for num in lst if num > 0])