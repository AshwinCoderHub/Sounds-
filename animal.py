
class Animal:
    def __init__(self, legs, eating_type, habitat_type, sound):
        self.legs = legs
        self.eating_type = eating_type
        self.habitat_type = habitat_type
        self.sound = sound

    def make_sound(self):
        return self.sound

class Cow(Animal):
    def __init__(self):
        super().__init__(legs=4, eating_type="herbivorous", habitat_type="land", sound="Mowwwwwww")

class Monkey(Animal):
    def __init__(self):
        super().__init__(legs=2, eating_type="omnivorous", habitat_type="land", sound="Eeeee")

class Dog(Animal):
    def __init__(self):
        super().__init__(legs=4, eating_type="carnivorous", habitat_type="land", sound="Bhau Bhau")

class Cat(Animal):
    def __init__(self):
        super().__init__(legs=4, eating_type="carnivorous", habitat_type="land", sound="Meow")

class Crow(Animal):
    def __init__(self):
        super().__init__(legs=2, eating_type="omnivorous", habitat_type="land", sound="Caw Caw")

class Donkey(Animal):
    def __init__(self):
        super().__init__(legs=4, eating_type="herbivorous", habitat_type="land", sound="Hee-Haw")

class Horse(Animal):
    def __init__(self):
        super().__init__(legs=4, eating_type="herbivorous", habitat_type="land", sound="Neigh")

class Goat(Animal):
    def __init__(self):
        super().__init__(legs=4, eating_type="herbivorous", habitat_type="land", sound="Baa Baa")

class Sheep(Animal):
    def __init__(self):
        super().__init__(legs=4, eating_type="herbivorous", habitat_type="land", sound="Baa Baa")
