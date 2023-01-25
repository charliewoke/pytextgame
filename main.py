import random
from time import sleep

# Loading
loader_bar = 0

while loader_bar != 100:
    delay = random.uniform(0.03, 0.2)
    print(loader_bar)
    loader_bar += 1
    sleep(delay)

print("Complete")


# Game Info
classes = ["Warrior", "Mage", "Paladin", "Rogue", "Cleric", "Druid", "Hunter", "Bard", "Monk", "Summoner"]
skills = ["Swordsmanship", "Archery", "Magery", "Necromancy", "Healing", "Thievery", "Stealth", "Lockpicking", "Traps", "Survival", "Animal", "First Aid", "Alchemy", "Blacksmithing", "Tailoring", "Leatherworking", "Engineering", "Herbalism", "Mining", "Fishing", "Cooking", "Leadership", "Tactics", "Merchant", "Persuasion"]

# Towns
# Town 1
town_1_name = "Measic"
town_1_places = ["", ""]

# Character Info
char_name = ""
char_class = ""
char_skills = []

# Character Creation
print("It is time for you to create you great character! " + (f"Feel Free to pick and choose."))
print("Please give yourself a name:")
char_name = input("Name: " + "")
print("Next, you must choose a class for " + char_name + ".")
classListTxT = ' '.join(classes)
print("Classes: " + classListTxT)
char_class = input("Class: " + "")
sleep(2)
print("Finally, you must select 5 skills. First type 1 skill from the list, then enter, and do that for the 3 skills you select.")
skillListTxT = ' '.join(skills)
sleep(2)
print("Skills: " + skillListTxT)

sleep(2)

for i in range(5):
    user_input = input("Enter a skill: ")
    while user_input not in skills or user_input in char_skills:
        if user_input not in skills:
            print("This skill doesn't exist. Please try again.")
        else:
            print("You have already selected that skill, please enter a new one.")
        user_input = input("Enter a skill: ")
    print("You have selected the skill: ", user_input)
    char_skills.append(user_input)
    
print("Your character's skills: ",char_skills)

# Inventory
inventory = ["wooden_sword", "apple", "apple", "apple", "rusty_armor",]
armor_slots = ["empty", "rusty_armor", "empty", "empty"]
hotbar = inventory[0:4]

# Chest
loottable = ["stone_sword", "iron_sword", "apple", "stake", "gem", "pickaxe", "axe", "shovel", "cake", "coal", "gold", "dust", "crumbs", "bread", "7"]
lootselect = random.choices(loottable)

# Functions
 
# Hotbar Logic
hotbar_txt = ' '.join(hotbar)
print("Hotbar: " + hotbar_txt)

# Game Vars
diceroll = 1

# GamePlay
sleep(2)
print("You find yourself deep in a forest. You can see an object behind a bush.")
print("Do you wish to roll for investigation?")
choice_1 = input("Y/N? " + "")
if choice_1 == "Y":
    diceroll = random.uniform(1, 20)
    print(diceroll)
    if diceroll >= 12:
        sleep(1)
        print("Your roll sucseeds!")
        sleep(1)
        print("You see that the object is a statue.")
    else:
        print("The variable is less than 12.")
else:
    print("You start walking and find a path.")
print("Do you wish to investigate further?")
choice_2 = input("Y/N? " + "")
if choice_2 == "Y":
    print("You walk towards the statue and see a golden sign.")
    sleep(1)
    print("The sign says:")
    sleep(1)
    print("Here may Artemis, a great Wife, Friend, and God rest.")
else:
    print("You start walking and find a path.")
    print("You follow the path and find a small town.")

print("Do you wish to enter the town.")
choice_3 = input("Y/N? " + "")
if choice_3 == "Y":
    print("You enter the town and look around.")
    sleep(1)
    print("You see a sign that says: " + "Welcome to " + town_1_name)
    sleep(1)
    
else:
    print("You continue down the path and reach a river.")
    print("You can roll for your survival skill to get across the river.")
    print("Do you wish to roll?")
choice_4 = input("Y/N? " + "")
if choice_4 == "Y":
    diceroll = random.uniform
    skillneeded = "survival"
    if skillneeded in char_skills:
        diceroll = +2
    print("Rolled: " + diceroll)





input()