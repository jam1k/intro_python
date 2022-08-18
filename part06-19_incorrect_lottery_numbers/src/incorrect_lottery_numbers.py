# Write your solution here
def reading_file():
    result = []
    with open("lottery_numbers.csv") as f:
        for line in f:
            line = line.replace("\n", "")
            line = line.split(";")
            result.append(line)
    f.close()
    return result

def create_empty_file():
    with open("correct_numbers.csv", "w+") as f:
        pass
    f.close

def writing_file(data: list):
    with open("correct_numbers.csv", "a") as f:
        string = ";".join(data)
        f.write(string)
        f.write("\n")
    f.close

def week_number(lst: list):   
    week = lst[0].split(" ")
    try:
        week_number = int(week[1])
        return True
    except: 
        ValueError("The week number is incorrect")
        return False

def numbers_are_correct(lst: list):
    numbers = lst[1].split(",")
    for i in range(len(numbers)):
            try:
                int(numbers[i])
            except:
                ValueError("One or more numbers are not correct")
                return False
    return True
        
def too_few_numbers(lottery_number: list):
    numbers = lottery_number[1].split(",")
    if len(numbers) < 7:
        return False
    else:
        return True

def numbers_between_limits(lottery_number: list):
    numbers = lottery_number[1].split(",")
    for i in range (len(numbers)):
        numbers[i] = int(numbers[i])
        if numbers[i] < 1 or numbers[i] > 39:
            return False
    return True

def number_appears_twice(lottery_number: list):
    numbers = lottery_number[1].split(",")
    if len(numbers) != len(set(numbers)):
        return False
    else:
        return True

def filter_incorrect():
    lottery_numbers = reading_file()
    create_empty_file()
    for lottery_number in lottery_numbers:
        if week_number(lottery_number) and numbers_are_correct(lottery_number) and too_few_numbers(lottery_number) and numbers_between_limits(lottery_number) and number_appears_twice(lottery_number):
            writing_file(lottery_number)

if __name__ == "__main__":
    numbers_between_limits(['week 31', '6,38,4,-26,32,24,34'])