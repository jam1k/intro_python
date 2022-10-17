# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"
    
    def __eq__(self, another):
        return 100*self.__euros+self.__cents == 100*another.__euros+another.__cents
    
    def __lt__(self, another):
        return 100*self.__euros+self.__cents<100*another.__euros+another.__cents
    
    def __gt__(self, another):
        return 100*self.__euros+self.__cents>100*another.__euros+another.__cents

    def __ne__(self, another):
        return 100*self.__euros+self.__cents!=100*another.__euros+another.__cents

    def __add__(self, another):
        euro_cent = 100*self.__euros+self.__cents+100*another.__euros+another.__cents
        result_eur = euro_cent//100
        result_cent = euro_cent%100
        result  = Money(result_eur, result_cent)
        return result
    
    def __sub__(self, another):
        if 100*self.__euros+self.__cents-100*another.__euros-another.__cents>0:
            euro_cent= 100*self.__euros+self.__cents-100*another.__euros-another.__cents
            result_eur = euro_cent//100
            result_cent = euro_cent%100
            result = Money(result_eur, result_cent)
            return result
        else:
            raise ValueError("a negative result is not allowed")
if __name__=="__main__":
    e1 = Money(4, 5)
    e2 = Money(4, 6)
    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)
