
word = input("Please type in a word: ")
character = input("Please type in a character: ")

index = word.find(character)
while index != -1 and len(word) >= index + 3:
    if word[index] == character:
        print(word[index:index + 3])
    index += 1