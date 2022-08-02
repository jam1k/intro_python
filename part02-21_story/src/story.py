# Write your solution here
story = ""
word = ""
attempts = 0
prev_word=""

while True:
    if word == prev_word and attempts != 0:
        break
    prev_word = word

    if word == "end":
        break

    elif attempts == 0:
        story = story + word
        word = input("Please type in a word: ")

    else:
        story = story + word + " "
        word = input("Please type in a word: ")

    attempts += 1
print(story)