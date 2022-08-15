# Please write a function named dict_of_numbers(), which returns a new dictionary. 
# The dictionary should have the numbers from 0 to 99 as its keys. 
# The value attached to each key should be the number spelled out in words. 
# Write your solution here
def dict_of_numbers():
    result = {}
    result[0] = "zero"
    result[1] = "one"
    result[2] = "two"
    result[3] = "three"
    result[4] = "four"
    result[5] = "five"
    result[6] = "six"
    result[7] = "seven"
    result[8] = "eight"
    result[9] = "nine"
    result[10] = "ten"
    result[11] = "eleven"
    result[12] = "twelve"
    result[13] = "thirteen"
    result[14] = "fourteen"
    result[15] = "fifteen"
    result[16] = "sixteen"
    result[17] = "seventeen"
    result[18] = "eighteen"
    result[19] = "nineteen"


    for i in range(20, 100):
        if i == 20:
            result[i] = "twenty"
        elif i == 30:
            result[i] = "thirty"
        elif i == 40:
            result[i] = "forty"
        elif i == 50:
            result[i] = "fifty"
        elif i == 60:
            result[i] = "sixty"
        elif i == 70:
            result[i] = "seventy"
        elif i == 80:
            result[i] = "eighty"
        elif i == 90:
            result[i] = "ninety"
        else:
            mod = i % 10
            result[i] = f"{result[i - mod]}-{result[mod]}"
    return result

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])