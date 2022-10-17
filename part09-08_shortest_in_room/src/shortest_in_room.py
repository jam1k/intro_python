# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return f"{self.name} ({self.height} cm)"

class Room:
    def __init__(self):
        self.list_of_persons = []

    def add(self, person: Person):
        self.list_of_persons.append(person)
    
    def is_empty(self):
        return len(self.list_of_persons)==0
    
    def print_contents(self):
        combined_hight = 0 
        for persn in self.list_of_persons:
            combined_hight += persn.height
        
        print(f"There are {len(self.list_of_persons)} persons in the room, and their combined height is {combined_hight} cm")
        for persn in self.list_of_persons:
            print (persn)

    def shortest(self):
        
        if not self.list_of_persons:
            return None
        else:
            shortest = self.list_of_persons[0].height
            result = self.list_of_persons[0]

            for prsn in self.list_of_persons:
                if prsn.height<shortest:
                    shortest = prsn.height
                    result = prsn
        return result


    def remove_shortest(self):
        

        if not self.list_of_persons:
            return None
        else: 
            shrtst_prsn = self.shortest()
            self.list_of_persons.remove(shrtst_prsn)
            return shrtst_prsn


if __name__=="__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()