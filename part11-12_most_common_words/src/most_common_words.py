# WRITE YOUR SOLUTION HERE:

def most_common_words(filename: str, lower_limit: int):
    with open(filename) as fd:
        words = fd.read()
        words = words.replace(",", " ")
        words = words.replace(".", " ")
        words = words.split()
        my_dict = {word : words.count(word) for word in words}

    result = {}
    for word, num in my_dict.items():
        if num >= lower_limit:
            result[word] = num
    return result
    
if __name__ == "__main__":
    result = most_common_words("/Users/jamilya/Library/Application Support/tmc/vscode/mooc-programming-22/part11-12_most_common_words/src/comprehensions.txt", 3)
