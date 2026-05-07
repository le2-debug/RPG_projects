FULL_STAR = "★"
EMPTY_STAR = "☆"

def create_weapon(weapon_name,damage,speed,magic):
    
    #Weapon name validation
    if not isinstance(weapon_name,str):
        return "The weapon name should be a string"
    if weapon_name == "":
        return "The weapon should have a name"
    if len(weapon_name)>12:
        return "The weapon name is too long"
    if " " in weapon_name:
        return "The weapon name should not contain spaces"
    
    #Stats validation
    if not isinstance(damage,int) or not isinstance(speed,int) or not isinstance(magic,int):
        return "All stats should be intergers"
    if damage<1 or speed<1 or magic<1:
        return "All stats should be at least 1"
    if damage>5 or speed>5 or magic>5:
        return "All stats should be no more than 5"
    if damage+speed+magic!=10:
        return "The weapon should start with 10 points"
    
    #Bars
    damage_bar = FULL_STAR*damage+EMPTY_STAR*(10-damage)
    speed_bar = FULL_STAR*speed+EMPTY_STAR*(10-speed)
    magic_bar = FULL_STAR*magic+EMPTY_STAR*(10-magic)

    return f"{weapon_name} \nDamage:{damage_bar}\nSpeed:{speed_bar}\nMagic:{magic_bar}"
print(create_weapon("Gun",5,4,1))