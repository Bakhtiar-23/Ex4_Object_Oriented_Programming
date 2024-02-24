class Person:
    def __init__(self, name: str):
        self.__name = name
        self.__numbers = []
        self.__address = None
 
    def name(self):
        return self.__name
 
    def numbers(self):
        return self.__numbers
 
    def add_number(self, number: str):
        self.__numbers.append(number)
 
    def address(self):
        return self.__address
 
    def add_address(self, address: str):
        self.__address = address
 
class PhoneBook:
    def __init__(self):
        self.__persons = {}
 
    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_number(number)
 
    def add_address(self, name: str, address: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_address(address)
 
    def get_entry(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name]
 
    def all_entries(self):
        return self.__persons
    
    
# Test the PhoneBook class
phonebook = PhoneBook()
phonebook.add_number("Eric", "02-123456")
print(phonebook.get_entry("Eric"))
print(phonebook.get_entry("Emily"))
