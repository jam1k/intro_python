# WRITE YOUR SOLUTION HERE:

def most_common_words(filename: str, lower_limit: int):
    with open(filename) as fd:
        words = fd.read()
        words = words.split()
        my_dict = {word : words.count(word) for word in fd}
    return my_dict

result = most_common_words("/Users/jamilya/Library/Application Support/tmc/vscode/mooc-programming-22/part11-12_most_common_words/src/comprehensions.txt", 3)
print(result)