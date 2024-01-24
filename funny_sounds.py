# Define the base class 'Animal'
class Animal:
    def __init__(self, legs, hands, eating_type, habitat_type):
        # Initialize attributes
        self.legs = legs
        self.hands = hands
        self.eating_type = eating_type
        self.habitat_type = habitat_type

#  cow inheriting from Animal
class Cow(Animal):
    def __init__(self):
        # Call the constructor of the base class using 'super()'
        super().__init__(legs=4, hands=0, eating_type="herbivorous", habitat_type="land")

# monkey inheriting from Animal
class Monkey(Animal):
    def __init__(self):
        super().__init__(legs=2, hands=2, eating_type="omnivorous", habitat_type="land")

#  dog inheriting from Animal
class Dog(Animal):
    def __init__(self):
        super().__init__(legs=4, hands=0, eating_type="carnivorous", habitat_type="land")

# cat inheriting from Animal
class Cat(Animal):
    def __init__(self):
        super().__init__(legs=4, hands=0, eating_type="carnivorous", habitat_type="land")

# Crow inheriting from Animal
class Crow(Animal):
    def __init__(self):
        super().__init__(legs=2, hands=0, eating_type="omnivorous", habitat_type="land")

# Donkey inheriting from Animal
class Donkey(Animal):
    def __init__(self):
        super().__init__(legs=4, hands=0, eating_type="herbivorous", habitat_type="land")

# Horse inheriting from Animal
class Horse(Animal):
    def __init__(self):
        super().__init__(legs=4, hands=0, eating_type="herbivorous", habitat_type="land")

# Goat inheriting from Animal
class Goat(Animal):
    def __init__(self):
        super().__init__(legs=4, hands=0, eating_type="herbivorous", habitat_type="land")

# Sheep inheriting from Animal
class Sheep(Animal):
    def __init__(self):
        super().__init__(legs=4, hands=0, eating_type="herbivorous", habitat_type="land")

# User input
animal_set = input("Choose a set of animals (a/b/c): ")

# Creating instances
if animal_set == 'a':
    animals = [Cow(), Monkey(), Dog()]
elif animal_set == 'b':
    animals = [Cat(), Crow(), Donkey()]
elif animal_set == 'c':
    animals = [Horse(), Goat(), Sheep()]
else:
    print("Invalid input. Please choose a valid set.")


for animal in animals:
    if isinstance(animal, Dog):
        print("Dog says: Bhau Bhau")
    elif isinstance(animal, Monkey):
        print("Monkey says: Eeeee")
    elif isinstance(animal, Cow):
        print("Cow says: Mowwwwwww")
    elif isinstance(animal, Cat):
        print("Cat says: Meow")
    elif isinstance(animal, Crow):
        print("Crow says: Caw Caw")
    elif isinstance(animal, Donkey):
        print("Donkey says: Hee-Haw")
    elif isinstance(animal, Horse):
        print("Horse says: Neigh")
    elif isinstance(animal, Goat):
        print("Goat says: Baa Baa")
    elif isinstance(animal, Sheep):
        print("Sheep says: Baa Baa")
    else:
        print("Unknown animal.")