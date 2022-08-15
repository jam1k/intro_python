# This final exercise in this part is a relatively demanding problem solving task. 
# It can be solved in many different ways. Even though this current section in the material covers tuples, 
# tuples are not necessarily the best way to go about solving this.
# Please write a program which prints out a square of letters as specified in the examples below. 
# You may assume there will be at most 26 layers.
# Write your solution here
import string
alphabet = string.ascii_uppercase
result = []

layers = int(input("Layers: "))

for i in range(layers):
    for j, string in enumerate(result):
        result[j] = alphabet[i] + string + alphabet[i]
    result.append((2 * i + 1) * alphabet[i])
    if i != 0:
        result.insert(0, (2 * i + 1) * alphabet[i])

for line in result:
    print (line)
