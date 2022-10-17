# WRITE YOUR SOLUTION HERE:
class PhoneBook:
    def __init__(self):
        self.__persons = {}
 
    def add_number(self, name: str, number: str):
        
        if not name in self.__persons:
            # add a new dictionary entry with an empty list for the numbers
            p = Person(name)
            p.add_number(number)
            self.__persons[name] = p
        else:
            self.__persons[name].add_number(number)
 
    def get_entry(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name].numbers()
 
    def search_with_number(self, number: str):
        
        for name, persons_item in self.__persons.items():
            if number in persons_item.numbers():
                return name
 
        return None
 
    def all_entries(self):
        return self.__persons
    
    def add_address(self, name:str, address: str):
        if not name in self.__persons:
            p = Person(name)
            p.add_address(address)
            self.__persons[name] = p
        
        else:
            self.__persons[name].add_address(address)

    def get_address(self, name):
        if not name in self.__persons:
            return None
        return self.__persons[name].address()
 
class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add entry")
        print("2 search")
        print("3 add address")
 
    def add_entry(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)
 
    def search(self):
        name = input("name: ")
        numbers = self.__phonebook.get_entry(name)
        address = self.__phonebook.get_address(name)
        if numbers == None or len(numbers) == 0:
            print("number unknown")
        
        else:
            for number in numbers:
                print(number)
        if address == None:
            print("address unknown")
        else:
            print(address)
    
    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)
 
    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_entry()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()
# Write your solution here:
class Person:
    def __init__(self, name) -> None:
        self.__name = name
        self.__numbers = []
        self.__address = None
    
    def name(self):
        return self.__name
    
    def numbers(self):
        return self.__numbers
    
    def address(self):
        return self.__address

    def add_number(self, number):
        self.__numbers.append(number)
    
    def add_address(self, new_address):
        self.__address = new_address
    def __str__(self) -> str:
        return f"{self.__name} address {self.__address} and numbers are {self.__numbers}"

application = PhoneBookApplication()
application.execute()
