# write your solution here
def read_integers(filename):
    with open(filename) as f:
        return [int(x) for x in f]
def largest():
    numbers = read_integers("numbers.txt")
    
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max

if __name__ == "__main__":
    largest()