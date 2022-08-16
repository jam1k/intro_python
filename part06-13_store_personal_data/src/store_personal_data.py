# Please write a function named store_personal_data(person: tuple), which takes a tuple containing some identifying information 
# as its argument.
# The tuple contains the following elements:
# Name (string)
# Age (integer)
# Height (float)
# This should be processed and written into the file people.csv. The file may already contain some data; 
# the new entry goes to the end of the file. The data should be written in the format: name;age;height
# Write your solution here
def store_personal_data(person: tuple):
    with open("people.csv", "a") as f:
        string =  string = ";".join(map(str, person))
        f.write(string + "\n")
    f.close()
