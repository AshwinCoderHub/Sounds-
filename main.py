from animal import Cow, Monkey, Dog, Cat, Crow, Donkey, Horse, Goat, Sheep

def main():
    while True:
        animals = {
            'a': [Cow(), Monkey(), Dog()],
            'b': [Cat(), Crow(), Donkey()],
            'c': [Horse(), Goat(), Sheep()]
        }

        user_input = input("Choose a set of animals (a/b/c): ")

        for animal in animals.get(user_input, []):
            print(f"{type(animal).__name__} says: {animal.make_sound()}, "
                  f"Eating Type: {animal.eating_type},"
                  f" Habitat Type: {animal.habitat_type}")

        user_choice = input("Do you want to choose another set? (yes/no): ").lower()
        if user_choice != 'yes':
            print("Thank you! Visit again! 😌👍🏻✨")
            break

# Directly call the main function
main()
