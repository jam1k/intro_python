# Write your solution here
sentence = []
while True:
    word = input("Word: ")
    if word in sentence:
        break
    sentence.append(word)
print (f"You typed in {len(sentence)} different words")
