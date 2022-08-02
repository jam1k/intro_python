# Copy here code of line function from previous exercise and use it in your solution
def line(num: int, string: str):
    if (len(string) == 0):
        print(num * "*")
    else:
        print(num * string[0])

def triangle(size, char):
    # You should call function line here with proper parameters
    i = 1
    while (i <= size):
        line(i, char)
        i += 1

def shape(size: int, char: str, height: int, char_rect: str):
    triangle(size, char)
    i = 1
    while (i <= height):
        line(size, char_rect)
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")