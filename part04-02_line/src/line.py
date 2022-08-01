# Write your solution here

def line(num: int, string: str):
    if (len(string) == 0):
        print(num * "*")
    else:
        print(num * string[0])

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")