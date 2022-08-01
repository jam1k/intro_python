# Copy here code of line function from previous exercise
def line(num: int, string: str):
    if (len(string) == 0):
        print(num * "*")
    else:
        print(num * string[0])

def square_of_hashes(size):
    # You should call function line here with proper parameters
    i = 1
    while (i <= size):
        line(size, "#")
        i+=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
