import random
from colorama import Fore

fileHeroes = "heroes.txt"
fileVillains = "villains.txt"
fileweapons = "weapons.txt"

def load_data(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = file.readlines()
    return random.choice(data).strip()

Hero = load_data(fileHeroes)
Villain = load_data(fileVillains)
Weaponhero = load_data(fileweapons)
Weaponvillain = load_data(fileweapons)
herohealth = 20
villainhealth = 20

print(Fore.CYAN + f"A battle has begun! {Hero} with {herohealth}HP vs {Villain} with {villainhealth}HP")
print(Fore.WHITE + f"{Hero} has a {Weaponhero}, with attack damage of {len(Weaponhero)}")
print(f"{Villain} has a {Weaponvillain}, with attack damage of {len(Weaponvillain)}")

def calculate_attack(Weaponhero, Weaponvillain):
    return len(Weaponhero), len(Weaponvillain)
hero_attack, villain_attack = calculate_attack(Weaponhero, Weaponvillain)

while herohealth > 0 and villainhealth > 0:

    villainhealth = villainhealth - hero_attack
    if villainhealth > 0:
        print(f"{Hero} hits with {Weaponhero}, {Villain} has {villainhealth}HP")
    else:
        print(f"{Hero} hits with {Weaponhero} with the final blow, {Villain} has 0 HP left")
        print(Fore.GREEN + f"{Villain} is defeated, {Hero} wins!")
        break

    herohealth = herohealth - villain_attack
    if herohealth > 0:
        print(f"{Villain} hits with {Weaponvillain}, {Hero} has {herohealth}HP")
    else:
        print(f"{Villain} hits with {Weaponvillain} with the final blow, {Hero} has 0 HP left")
        print(Fore.RED + f"{Hero} is defeated, {Villain} wins!")
        break