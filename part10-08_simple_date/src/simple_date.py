# TEE RATKAISUSI TÄHÄN:

class SimpleDate:
    def __init__(self, day:int, month:int, year:int):
        self.day = day
        self.month = month
        self.year = year
        
    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"


    def calculate(self, day, month, year):
        result = day+30*month+year*12*30
        print = result
        return result

    def __lt__(self, another):
        number1 = self.calculate(self.day, self.month, self.year)
        number2 = another.calculate(another.day, another.month, another.year)
        
        return number1<number2
    
    def __gt__(self, another):
        number1 = self.calculate(self.day, self.month, self.year)
        number2 = another.calculate(another.day, another.month, another.year)
        
        return number1>number2

    def __eq__(self, another):
        number1 = self.calculate(self.day, self.month, self.year)
        number2 = another.calculate(another.day, another.month, another.year)
        
        return number1==number2

    def __ne__(self, another):
        number1 = self.calculate(self.day, self.month, self.year)
        number2 = another.calculate(another.day, another.month, another.year)
        
        return number1!=number2
    
    def __add__(self, number_given):
        number1 = self.calculate(self.day, self.month, self.year)
        
        result = number1+number_given
        result_year = result//(12*30)
        result_month = (result%(12*30))//30
        result_day =(result%(12*30))%30
        return SimpleDate(result_day, result_month, result_year)


    def __sub__(self, another):
        number1 = self.calculate(self.day, self.month, self.year)
        number2 = another.calculate(another.day, another.month, another.year)
        result = number1-number2
        result_year = result//(12*30)
        result_month = (result%(12*30))//30
        result_day =(result%(12*30))%30
        return abs(result)

if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)