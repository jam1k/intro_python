# write your solution here
def reading_file(filename):
    with open(filename) as f:
        return [x.strip() for x in f]

text = input("Write text: ")
words = reading_file("wordlist.txt")
#print(words[0:10])
text = text.split(" ")
for word in text:
    if word == text[-1]:
        if word.lower() in words:
            print(f"{word}", end = "")
        else:
            print(f"*{word}*", end = "")
    else:
        if word.lower() in words:
            print(f"{word}", end = " ")
            
        else:
            print(f"*{word}*", end = " ")
print("\n")
    