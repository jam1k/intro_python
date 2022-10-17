# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.count = 0
        self.even = 0
        self.odd = 0

    def add_number(self, number:int):
        self.numbers += number
        self.count+=1
        if number%2==0:
            self.even +=number
        else: 
            self.odd +=number
        

    def count_numbers(self):
        return self.count

    def get_sum(self):

        return self.numbers
    
    def average(self):
        if self.count == 0:
            return 0
        else:
            result = self.numbers/self.count
            return result

print ("Please type in integer numbers: ")
number_stats = NumberStats()
while True:
    my_number = int(input ())
    if my_number == -1:
        break
    number_stats.add_number(my_number)

    
print("Sum of numbers:", number_stats.get_sum())
print("Mean of numbers:", number_stats.average())
print("Sum of even numbers:", number_stats.even)
print("Sum of odd numbers:", number_stats.odd)
