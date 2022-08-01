# Write your solution here
def longest(strings: list):
    longest_str = 0
    for string in strings:
        if len(string) > longest_str:
            longest_str = len(string)
            result = string
    return result

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))