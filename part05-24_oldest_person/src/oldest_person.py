# Please write a function named oldest_person(people: list), which takes a list of tuples as its argument. 
# In each tuple, the first element is the name of a person, and the second element is their year of birth. 
# The function should find the oldest person on the list and return their name.
# Write your solution here

def oldest_person(people: list):
    def order_oldest(person: tuple):
        return person[1]
    return min(people, key = order_oldest)[0]