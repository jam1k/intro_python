# Given a list of integers, let's decide that two consecutive items in the list are neighbours if their difference is 1. 
# So, items 1 and 2 would be neighbours, and so would items 56 and 55.
# Please write a function named longest_series_of_neighbours, which looks for the longest series of neighbours within the list, and returns its length.
# For example, in the list [1, 2, 5, 4, 3, 4] the longest list of neighbours would be [5, 4, 3, 4], with a length of 4.
# Write your solution here
def is_neigbours(a: int, b: int):
    if abs(a - b) == 1:
        return True
    else:
        return False

def get_sequence(lst: list, i: int):
    result = [lst[i]]
    while i < len(lst) - 1 and is_neigbours(lst[i], lst[i + 1]):
        result.append(lst[i + 1])
        i += 1
    return result

def longest_series_of_neighbours(lst: list):
    i = 0
    longest = []
    while (i < len(lst)):
        current = get_sequence(lst, i)
        if len(current) > len(longest):
            longest = current
        i+=1
    return len(longest)

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))