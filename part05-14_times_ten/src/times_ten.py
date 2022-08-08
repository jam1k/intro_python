# Please write a function named times_ten(start_index: int, end_index: int), which creates and returns a new dictionary. 
# The keys of the dictionary should be the numbers between start_index and end_index inclusive
# The value mapped to each key should be the key times ten.
# Write your solution here
def times_ten(start_index: int, end_index: int):
    result = {}
    while (start_index <= end_index):
        result[start_index] = 10 * start_index
        start_index += 1
    return result