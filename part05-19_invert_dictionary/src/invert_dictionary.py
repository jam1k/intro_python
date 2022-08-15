# Please write a function named invert(dictionary: dict), which takes a dictionary as its argument. 
# The dictionary should be inverted in place so that values become keys and keys become values.
# Write your solution here

def invert(dictionary: dict):
    for key in list(dictionary):
        value = dictionary.pop(key)
        dictionary[value] = key

if __name__ == "__main__":
    di = {1: 10, 2: 20}
    invert(di)
    print(di)