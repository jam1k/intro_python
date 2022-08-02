# Write your solution here
sentence = input ("Please type in a sentence: ")
print (sentence[0])
index = 1
while index + 1 < len(sentence):
    if sentence [index] == " ":
        print (sentence[index + 1])
    index += 1
