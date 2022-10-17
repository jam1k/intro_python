# WRITE YOUR SOLUTION HERE:

from collections import Counter

class ListHelper:
    def __init__(self) -> None:
        pass

    @classmethod
    def greatest_frequency(cls, my_list: list):
        return max(set(my_list), key=my_list.count)

    @classmethod
    def doubles(cls, my_list: list):
        cnt = Counter(my_list)
        result = [k for k, v in cnt.items() if v > 1]
        
        return len(result)

if __name__ == "__main__":

    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))