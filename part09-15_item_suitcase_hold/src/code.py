# Write your solution here:
#from sys import setrecursionlimit, settrace


class Item:
    def __init__(self, name: str, weight: int):
        self.names = name
        self.weights = weight

    def name(self):
        return self.names
    
    def weight(self):
        return self.weights
    
    def __str__(self):
        return f"{self.names} ({self.weights} kg)"


class Suitcase:
    def __init__(self, max_weights:int, item=None):
        self.max_weights = max_weights
        self.number_of_items = 0
        self.kilo = 0
        self.items = []
    
    def add_item(self, item:Item):

        if self.kilo + item.weight()<=self.max_weights:
            self.item = item
            self.items.append(item)
            self.number_of_items+=1
            self.kilo+= item.weight()
    def print_items(self):
        for itm in self.items:
            print (itm)

    def weight(self):
        return self.kilo


    
    def __str__(self):
        if self.number_of_items != 1:
            return f"{self.number_of_items} items ({self.kilo} kg)"
        else:
            return f"{self.number_of_items} item ({self.kilo} kg)"

    def heaviest_item(self):
        heaviest = self.items[0].weight()
        result = self.items[0]
        for itm in self.items:
            if itm.weight()> heaviest:
                heaviest = itm.weight()
                result = itm
        return result

class CargoHold:
    def __init__(self, max_weight: int, suitcase = None):
        self.max_weight = max_weight
        self.suitcases = []
        self.kilo = 0
    def add_suitcase(self, suitcase: Suitcase):
        if suitcase.weight()+self.kilo<=self.max_weight:
            self.suitcases.append(suitcase)
            self.kilo+=suitcase.weight()

    def __str__(self):
        if len(self.suitcases)!=1:
            return f"{len(self.suitcases)} suitcases, space for {self.max_weight-self.kilo} kg"
        else:
            return f"{len(self.suitcases)} suitcase, space for {self.max_weight-self.kilo} kg"

    def print_items(self):
        for stcase in self.suitcases:
            for itm in stcase.items:
                print (itm)
            

if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()