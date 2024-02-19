class Animal:
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def display_info(self):
        print(f"Name: {self.name}, Health: {self.health}, Happiness: {self.happiness}")

    def feed(self):
        self.health = min(10, self.health + 10)
        self.happiness = min(10, self.happiness + 10)

class Lion(Animal):
    def __init__(self, name, age):
        super(). __init__(name, age, health=20, happiness=30)
        self.power = "King"

    def display_info(self):
        super().display_info()
        print(f"Special Attribute: His Power: {self.power}")

class Tiger(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health=40, happiness=50)
        self.color = "Orange and Brown"

    def display_info(self):
        super().display_info()
        print(f"Special Attribute: His Color: {self.color}")

class Bear(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health=60, happiness=70)
        self.volume = "Huge"
    
    def display_info(self):
        super().display_info()
        print(f"Special Attribute: His Volume: {self.volume}")

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.zoo_name = zoo_name
    
    def add_lion(self, name):
        self.animals.append( Lion(name) )
    
    def add_tiger(self, name):
        self.animals.append( Tiger(name) )

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

zoo1 = Zoo("John's Zoo")   
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.print_all_info()












        

        

    
        