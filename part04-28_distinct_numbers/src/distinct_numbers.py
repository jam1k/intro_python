# Please write a function named distinct_numbers, which takes a list of integers as its argument. 
# The function returns a new list containing the numbers from the original list in order of magnitude, 
# and so that each distinct number is present only once.
# Write your solution here
def distinct_numbers(lst: list):
    result = []
    for num in lst:
        if num not in result:
            result.append(num)
    return sorted(result)