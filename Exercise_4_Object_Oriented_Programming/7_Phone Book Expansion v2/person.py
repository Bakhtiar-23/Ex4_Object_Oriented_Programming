class Person:
    def __init__(self, name):
        self._name = name
        self._numbers = []
        self._address = None

    def name(self):
        return self._name

    def numbers(self):
        return self._numbers

    def address(self):
        return self._address

    def add_number(self, number):
        self._numbers.append(number)

    def add_address(self, address):
        self._address = address

# Example usage:
person = Person("Eric")
print(person.name())  # Output: Eric
print(person.numbers())  # Output: []
print(person.address())  # Output: None
person.add_number("040-123456")
person.add_address("Mannerheimintie 10 Helsinki")
print(person.numbers())  # Output: ['040-123456']
print(person.address())  # Output: Mannerheimintie 10 Helsinki
