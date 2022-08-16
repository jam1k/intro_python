# Write your solution here
def add_entry(filename, entry):
    with open(filename, "a") as my_file:
        my_file.write(f"{entry}\n")
    my_file.close()

def print_diary(filename):
    with open(filename) as f:
        for line in f:
            print(line)
    f.close()

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = int(input("Function: "))
    if function == 0:
        print("Bye now!")
        break
    elif function == 1:
        entry = input("Diary entry: ")
        add_entry("diary.txt", entry)
        print ("Diary saved")
    elif function == 2:
        print("Entries:")
        print_diary("diary.txt")

        