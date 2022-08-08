while True:
    string = input("Type in a string: ")
        
    if string == "":
        print(f"Total number of strings: {count}")
        print(f"The average length of the strings: {average_len(strings)}")
        print(f"The most common character in strings: {most_common_list(strings)}")
        break
    else:
        count += 1
        strings.append(string)
