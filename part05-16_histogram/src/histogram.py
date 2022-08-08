# Please write a function named histogram, which takes a string as its argument. 
# The function should print out a histogram representing the number of times each letter occurs in the string. 
# Each occurrence of a letter should be represented by a star on the specific line for that letter.
# Write your solution here

def histogram(string: str):
    result = {}
    for char in string:
        result[char] = string.count(char)
    
    for key, value in result.items():
        print(f"{key} {value * '*'}")
        
if __name__ == "__main__":
    histogram("abba")