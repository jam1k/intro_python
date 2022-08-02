# Write your solution here

input_string = input ("Word: ")


index = int ((28 - len(input_string)) / 2)
print ("*" * 30)
if len(input_string) % 2 != 0:
    print ("*" + index * " " + input_string + (index + 1) * " " + "*")
else: 
    print ("*" + index * " " + input_string + index * " " + "*")

print ("*" * 30)
