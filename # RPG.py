# RPG 

import random

class Humanoids:
    def __init__(self, height, weight, hair_color, eye_color, strength, 
                 dexterity, constitution, intelligence, wisdom, charisma):
        self.height = height
        self.weight = weight
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
    
    def display_attributes(self):
        print(f"Height: {self.height}ft")
        print(f"Weight: {self.weight}lbs")
        print(f"Hair Color: {self.hair_color}")
        print(f"Eye Color: {self.eye_color}")
        print(f"Strength: {self.strength}")
        print(f"Dexterity: {self.dexterity}")
        print(f"Constitution: {self.constitution}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Wisdom: {self.wisdom}")
        print(f"Charisma: {self.charisma}")

class Human(Humanoids):
    def __init__(self, height, weight, hair_color, eye_color, strength, 
                 dexterity, constitution, intelligence, wisdom, charisma):
        super().__init__(height, weight, hair_color, eye_color, strength, 
                         dexterity, constitution, intelligence, wisdom, charisma)
        attribute = input("As a Human, you can add +2 bonus points to a single skill/attribute: strength, dexterity, constitution, intelligence, wisdom, charisma: ").lower()
        if attribute == "strength":
            self.strength += 2
        elif attribute == "dexterity":
            self.dexterity += 2
        elif attribute == "constitution":
            self.constitution += 2
        elif attribute == "intelligence":
            self.intelligence += 2
        elif attribute == "wisdom":
            self.wisdom += 2
        elif attribute == "charisma":
            self.charisma += 2

class Elves(Humanoids):
    def __init__(self, height, weight, hair_color, eye_color, strength, 
                 dexterity, constitution, intelligence, wisdom, charisma):
        super().__init__(height, weight, hair_color, eye_color, strength, 
                         dexterity, constitution, intelligence, wisdom, charisma)
        self.dexterity += 2
        self.charisma += 2
        print("As an Elf, you are immune to Sleep and gain +2 to Dexterity and Charisma.")

class Dwarves(Humanoids):
    def __init__(self, height, weight, hair_color, eye_color, strength, 
                 dexterity, constitution, intelligence, wisdom, charisma):
        super().__init__(height, weight, hair_color, eye_color, strength, 
                         dexterity, constitution, intelligence, wisdom, charisma)
        self.strength += 2
        self.constitution += 2
        self.charisma -= 2
        print("As a Dwarf, you have 20% Resistance to Magic, gain +2 to Strength and Constitution, and -2 to Charisma.")

def characterCreation():
    print("Welcome to the game! Choose your race:")
    print("1. Human")
    print("2. Elf")
    print("3. Dwarf")
    
    choice = input("Enter the number that matches your choice: ").strip()
    height = input("height (in feet): ")
    weight = input("weight (in lbs): ")
    hair_color = input("hair color: ")
    eye_color = input("eye color: ")
    
    strength = random.randint(1, 18)
    dexterity = random.randint(1, 18)
    constitution = random.randint(1, 18)
    intelligence = random.randint(1, 18)
    wisdom = random.randint(1, 18)
    charisma = random.randint(1, 18)
    
    if choice == "1":
        character = Human(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
    elif choice == "2":
        character = Elves(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
    elif choice == "3":
        character = Dwarves(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
    else:
        print("wrong choice. Try again.")
        return
    
    print("\nYour character's final STATS are:")
    character.display_attributes()

if __name__ == "__main__":
    characterCreation()
