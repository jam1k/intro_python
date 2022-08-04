# Please use the isupper method to write a function named no_shouting, which takes a list of strings as an argument. 
# The function returns a new list, containing only those items from the original which do not consist of solely uppercase characters.
# Write your solution here
def no_shouting(lst: list):
    return [item for item in lst if not item.isupper()]