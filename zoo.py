class Animal:
    def __init__(self, name, age, health=50, happiness=50):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Health: {self.health}, Happiness: {self.happiness}")

    def feed(self):
        self.health += 10
        self.happiness += 10

class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health=70, happiness=60)

class Tiger(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health=80, happiness=70)

    def roar(self):
        print(f"{self.name} the tiger roars loudly!")

class Bear(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health=90, happiness=80)

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, animal):
        self.animals.append(animal)

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

# Create a zoo and add animals
zoo1 = Zoo("John's Zoo")
zoo1.add_animal(Lion("Nala", 3))
zoo1.add_animal(Lion("Simba", 4))
zoo1.add_animal(Tiger("Rajah", 5))
zoo1.add_animal(Tiger("Shere Khan", 6))
zoo1.add_animal(Bear("Baloo", 7))

# Print information about all animals in the zoo
zoo1.print_all_info()

# Feed an animal and check its status
print("\nFeeding Rajah...")
zoo1.animals[2].feed()
zoo1.animals[2].display_info()

# Make the tiger roar
print("\nRajah's reaction:")
zoo1.animals[2].roar()
