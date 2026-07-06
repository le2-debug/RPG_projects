full_dot = '●'
empty_dot = '○'

class Character:
    def __init__(self, name, strength, intelligence, charisma):
        self.name = name
        self.strength = strength
        self.intelligence = intelligence
        self.charisma = charisma

#Name Validation
    def validate_name(self, name):
        if not isinstance(name, str):
            return "The character name should be a string"
        if name == "":
            return "The character should have a name"
        if len(name) > 10:
            return "The character name is too long"
        if " " in name:
            return "The character name should not contain spaces"

#Stats Validation
    def validate_stats(self):
        if not all(isinstance(stat, int) for stat in (self.strength,self.intelligence,self.charisma)):
            return "The character stats should be integers"
        if any(stat < 1 or stat > 4 for stat in (self.strength, self.intelligence, self.charisma)):
            return "The character stats should be between 1 and 10"
        if sum((self.strength, self.intelligence, self.charisma)) != 7:
            return "The character should have a total of 7 points in stats"

#Stats Bars
    def __str__(self):
        strength_bar = full_dot * self.strength + empty_dot * (10 - self.strength)
        intelligence_bar = full_dot * self.intelligence + empty_dot * (10 - self.intelligence)
        charisma_bar = full_dot * self.charisma + empty_dot * (10 - self.charisma)

        result = self.name
        result += "\nSTR " + strength_bar
        result += "\nINT " + intelligence_bar
        result += "\nCHA " + charisma_bar

        return result

print(Character("Ren",4,2,1))