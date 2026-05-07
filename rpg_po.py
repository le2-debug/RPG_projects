full_heart = "♥"
empty_heart = "♡"
full_dot = '●'
empty_dot = '○'

def create_potion(name,healing,duration):
    #Name validation
    if not isinstance(name,str):
        return "Potion name should be a string"
    if name == "":
        return "Potion should have a name"
    if len(name)>12:
        return "Potion name too long"
    
    #Stats Validation
    if not isinstance(healing,int) or not isinstance(duration,int):
        return "All stats should be integers"
    if healing<1 or duration<1:
        return "All stats should be from 1"
    if healing>5 or duration>5:
        return "All stats should not exceed 5"
    if healing+duration< 4:
        return "Potion should start with 4 points"
    #Rarity Function
    def rarity():
        if healing + duration <= 3:
            return "Common"
        if healing + duration <=4:
            return "Rare"
        else:
            return "Legendary"

    #Bars
    healing_bar = full_heart*healing + empty_heart*(10-healing)
    duration_bar = full_dot*duration + empty_dot*(10-duration)
    return f"Name:{name}\nHealing:{healing_bar}\nDuration:{duration_bar}\nRarity:{rarity()}"
print(create_potion("Earth",2,4))