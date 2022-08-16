# The file numbers.txt contains integer numbers, one number per line. Please write a function named largest, which reads the file and returns the largest number in the file.
# Notice that the function does not take any arguments. The file you are working with is always named numbers.txt.
# write your solution here

def read_integers(filename):
    with open(filename) as f:
        return [int(x) for x in f]
def largest():
    numbers = read_integers("numbers.txt")
    return max(numbers)
