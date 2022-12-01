# Write your solution here
def prime_numbers():
    yield 2
    num = 3

    while True:
        i = 2
        state = True
        while (i < num):
            if num % i == 0:
                state = False
                break
            i += 1
        
        if state:
            yield num
        
        num += 1

    
if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))