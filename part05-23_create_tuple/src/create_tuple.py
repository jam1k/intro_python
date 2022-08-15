# Please write a function named create_tuple(x: int, y: int, z: int), which takes three integers as its arguments, and creates and returns a tuple based on the following criteria:
# 1. The first element in the tuple is the smallest of the argument.
# 2. The second element in the tuple is the greatest of the arguments
# 3. The third element in the tuple is the sum of the arguments
# Write your solution here

def create_tuple(x: int, y: int, z: int):
    return (min(x, y, z), max(x, y, z), x + y + z)

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))