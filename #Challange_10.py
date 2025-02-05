#Challange_10

class PlayerCharacter:
    def __init__(self, health, armor_rating, attack_power):
        self.set_health(health)
        self.set_armor_rating(armor_rating)
        self.set_attack_power(attack_power)
        
    def set_health(self, health):
        if 1 <= health <= 100:
            self.health = health
        else:
            raise ValueError("Health has to be between 1 and 100")
        
    def set_armor_rating(self, armor_rating):
        if 1 <= armor_rating <= 20:
            self.armor_rating = armor_rating
        else:
            raise ValueError("Armor should be between 1 and 20.")

    def set_attack_power(self, attack_power):
        if 1 <= attack_power <= 20:
            self.attack_power = attack_power
        else:
            raise ValueError("Attack power has to be between 1 and 20.")

    def get_health(self):
        return self.health

    def get_armor_rating(self):
        return self.armor_rating

    def get_attack_power(self):
        return self.attack_power

def main():
    print("Make YOUR Wizard!!: ")
    
    try:
        health = int(input("Set your Wiz health (1-100): "))
        armor_rating = int(input("How strong is your armor (1-20): "))
        attack_power = int(input("How hard can you punch? (enter your attack power) (1-20): "))
        
        wizard = PlayerCharacter(health, armor_rating, attack_power)
        
        print("\nWizard's Attributes:")
        print(f"Health: {wizard.get_health()}")
        print(f"Armor Rating: {wizard.get_armor_rating()}")
        print(f"Attack Power: {wizard.get_attack_power()}")
        
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":            
       main() 