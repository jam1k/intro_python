# The file fruits.csv contains names of fruits, and their prices. Please write a function named read_fruits, 
# which reads the file and returns a dictionary based on the contents. 
# In the dictionary, the name of the fruit should be the key, and the value should be its price.
# Prices should be of type float.
# NB: the function does not take any arguments. The file you are working with is always named fruits.csv.
# write your solution here:

def read_fruits():
    result = {}
    with open("fruits.csv") as my_file:
        for line in my_file:
            line = line.replace('\n', '')
            line = line.split(";")
            result[line[0]] = float(line[1])
    return result