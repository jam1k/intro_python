# Please write a function named list_sum which takes two lists of integers as arguments. 
# The function returns a new list which contains the sums of the items at each index in the two original lists. 
# You may assume both lists have the same number of items.

# Write your solution here
def list_sum (lst1: list, lst2: list):
    return [num1 + num2 for num1, num2 in zip(lst1, lst2)]