# Please write a function named factorials(n: int), which returns the factorials of the numbers 1 to n in a dictionary. 
# The number is the key, and the factorial of that number is the value mapped to it.
# A reminder: the factorial of the number n is written n! and is calculated by multiplying the number by each integer smaller than itself. 
# For example, the factorial of 4 is 4 * 3 * 2 * 1 = 24.
# Write your solution here

def calc_fact(n: int):
    if n == 1:
        result = 1
    else:
        result = n * calc_fact(n - 1)
    return result

def factorials(n: int):
    result  = {}
    i = 1
    while (i <= n):
        result[i] = calc_fact(i)
        i += 1

    return result

if __name__ == "__main__":
    print(factorials(2))