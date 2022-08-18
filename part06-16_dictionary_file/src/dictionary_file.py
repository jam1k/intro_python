# Please write a program which functions as a dictionary. The user can type in new entries or look for existing entries.
# Write your solution here
def writing_to_dict(finnish: str, english: str):
    with open("dictionary.txt", "a") as f:
        f.write(f"{finnish}:{english}\n")
        print("Dictionary entry added")
    f.close()

def reading_from_dict():
    dictionary = []
    with open("dictionary.txt") as f:
        for line in f:
            line = line.replace("\n", "")
            line = line.split(":")
            dictionary.append(line)
    f.close()
    return dictionary

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    funct = int(input("Function: "))
    if funct == 3:
        print("Bye!")
        break
    elif funct == 1:
        finnish = input("The word in Finnish: ")
        english = input("The word in English: ")
        writing_to_dict(finnish, english)
        
    elif funct == 2:
        search_term = input("Search term: ")
        dictionary = reading_from_dict()
        result = []
        for word_pairs in dictionary:
            for word in word_pairs:
                if search_term in word:
                    result.append(word_pairs)
        for item in result:
            print(f"{item[0]} - {item[1]}")