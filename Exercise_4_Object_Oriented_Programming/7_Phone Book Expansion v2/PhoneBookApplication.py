from phonebook import PhoneBook
from person import Person

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()
 
    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")
 
 
    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)
 
    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)
 
    def search(self):
        name = input("name: ")
        data = self.__phonebook.get_entry(name)
        if data==None:
            print("number unknown")
            print("address unknown")
            return
 
        numbers = data.numbers()
        if len(numbers)==0:
            print("number unknown") 
        else: 
            for number in numbers:
                print(number)
 
        address = data.address()
        if address!=None:
            print(address)
        else:
            print("address unknown")
 
    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()
 
 
# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()
 