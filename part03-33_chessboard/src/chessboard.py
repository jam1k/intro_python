# Write your solution here
def first_part(size):
    i = 0
    result = ""
    while i < size:
        if i % 2 != 0:
            result += "0"
        else:
            result += "1"

        i += 1
    print(result)

def second_part(size):
    i = 0
    result = ""
    while i < size:
        if i % 2 != 0:
            result += "1"
        else:
            result += "0"
        i += 1
    print(result)

def chessboard(size):
    i = 0
    while i < size:
        if i % 2:
            second_part(size)
        else:
            first_part(size)
        i += 1

# Testing the function
if __name__ == "__main__":
    chessboard(4)
    chessboard(0)
    chessboard (3)