# Write your solution here

def print_many_times(string, number):
    i = 1
    while i <= number:
        print(string)
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print_many_times("python", 5)