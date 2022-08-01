# Write your solution here
def line(whitespaces, stars):
    print(whitespaces * " " + stars*"*" + whitespaces * " ")

def spruce(size: int):
    stars = 1
    whitespace = size-1
    print("a spruce!")
    i = 1
    while (i <= size):
        line (whitespace, stars)
        i += 1
        whitespace -= 1
        stars += 2

    whitespace = size-1
    stars = 1
    line (whitespace, stars) 
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)