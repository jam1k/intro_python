# write your solution here
def reading_file(filename):
    with open(filename) as f:
        return [x.strip() for x in f]

text = input("Write text: ")
text = text.split(" ")
words = reading_file("wordlist.txt")

for word in text:
    if word.lower() in words:
        print(f"{word} ", end = "")
    else:
        print(f"*{word}* ", end = "")
print()