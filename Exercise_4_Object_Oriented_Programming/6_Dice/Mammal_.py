class Mammal:
    def __init__(self, mammal_id, species, name, size, weight):
        self.mammal_id = mammal_id
        self.species = species
        self.name = name
        self.size = size
        self.weight = weight

    def __str__(self):
        return f"ID: {self.mammal_id}, Species: {self.species}, Name: {self.name}, Size: {self.size}, Weight: {self.weight}"
