# Write your solution here

def hash_square (number):
    i = number
    while i > 0:
        print (number * "#")
        i -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)