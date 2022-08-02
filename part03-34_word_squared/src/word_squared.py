# Write your solution here
def squared(word, size):
    new_word = 10000 * word
    print(new_word[0:size])

    i = 1
    while i < size:
        new_word = new_word[size:]
        print(new_word[0:size])
        i += 1

# Testing the function
if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)