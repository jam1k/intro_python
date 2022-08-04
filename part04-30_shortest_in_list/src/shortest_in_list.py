# Please write a function named shortest, which takes a list of strings as its argument.
# The function returns whichever of the strings is the shortest. 
# If more than one are equally short, the function can return any of the shortest strings 
# (there will be no such situation in the tests). 
# You may assume there will be no empty strings in the list.
# Write your solution here
def shortest(lst: list):
    min_len = len(lst[0])
    result = lst[0]
    len_of_list = len(lst)
    i = 1
    while (i < len_of_list):
        if len(lst[i]) < min_len:
            min_len = len(lst[i])
            result = lst[i]
        i += 1
    return result

if __name__ == "__main__":
    print(shortest(['Alan', 'Susan', 'Seymour', 'Kim', 'Susan']))