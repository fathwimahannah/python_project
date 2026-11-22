import random
import json


print("==============================================")
print("          LEGENDS OF A FORGOTTEN REALM")
print("==============================================")
print(" ")
print("     Welcome to the kingdom of Eldoria!!!")
print(" ")



def character():
    print("\n =========CHARACTER CREATION=============")
    player_name = input("Enter your  name: ")
    print("Welcome,",player_name)

    while True:

        print("\n Choose your character class:")
        print(" ")
        print("1. Warrior")
        print("2. Mage")
        print("3. Archer")
        print("4. Assassin")
        print(" ")


        ch1=input("Enter your choice(1-4): ")
        if ch1=="1":
            character_class="Warrior"
            hp = 150
            mana = 30
            attack = 20
            defense = 15
            critical_chance = 5
        elif ch1=="2":
            character_class="Mage"
            hp = 90
            mana = 150
            attack = 25
            defense = 5
            critical_chance = 10
        elif ch1=="3":
            character_class="Archer"
            hp = 110
            mana = 70
            attack = 18
            defense =  10
            critical_chance = 15
        elif ch1=="4":
            character_class="Assassin"
            hp = 85
            mana = 60
            attack = 30
            defense = 5
            critical_chance = 25
        else:
            print(" ")
            print("Invalid character choice!!! ","\n")

            continue
        break

    player_data={
            "name":player_name,
            "class":character_class,
            "level":1,
            "exp":0,
            

            "hp":hp,
            "max_hp":hp,
            "mana":mana,
            "max_mana":mana,

            "attack":attack,
            "defense":defense,

            "critical_chance":critical_chance,
            "critical_damage":1.5,

            "weapon":None,
            "armor":None,

            "potions":["Small Health Potion", "Small Health Potion",
            "Large Health Potion","mana potion"],

            "inventory":[],

            "gold":100,
            "bosses_defeated":0,
            "enemies_defeated":0
        }

    print("\n====CHARACTER CREATED====")
    print("\n======= PLAYER INFORMATION =======")

    for key, value in player_data.items():
        print(key, ":", value)
    
    
    return player_data

def view_stats(player):

    print("\n================================")
    print("         PLAYER STATS")
    print("================================")

    print("Name:", player["name"])
    print("Class:", player["class"])
    print("Level:", player["level"])
    print("Experience:", player["exp"])

    print("\n------ HEALTH & MANA ------")
    print("HP:", player["hp"], "/", player["max_hp"])
    print("Mana:", player["mana"], "/", player["max_mana"])

    print("\n------ COMBAT STATS ------")
    print("Attack:", player["attack"])
    print("Defense:", player["defense"])
    print("Critical Chance:", player["critical_chance"], "%")
    print("Critical Damage:", player["critical_damage"])

    print("\n------ EQUIPMENT ------")
    print("Weapon:", player["weapon"])
    print("Armor:", player["armor"])

    print("\n------ GAME INFORMATION ------")
    print("Gold:", player["gold"])
    print("Bosses Defeated:", player["bosses_defeated"])
    print("Enemies Defeated:", player["enemies_defeated"])

    print("================================")
    
def create_enemy(player):

    enemy_names = [
        "Goblin",
        "Wolf",
        "Skeleton",
        "Orc",
        "Slime",
        "Bandit",
        "Zombie",
        "Spider",
        "Dark Knight",
        "Fire Imp",
        "Ice Wolf",
        "Stone Golem",
        "Ghost",
        "Troll",
        "Vampire",
        "Werewolf",
        "Dark Mage",
        "Demon",
        "Lava Beast",
        "Ice Demon",
        "Shadow Beast",
        "Death Knight",
        "Dragon",
        "Demon Warrior",
        "Ancient Monster"
    ]

    enemy = random.choice(enemy_names)

    enemy_number = enemy_names.index(enemy)

    level_bonus = player["level"] - 1

    enemy_data = {
        "name": enemy,
        "hp": 50 + (enemy_number * 10) + (level_bonus * 10),
        "attack": 10 + (enemy_number * 2) + (level_bonus * 2),
        "defense": 3 + enemy_number + level_bonus,
        "exp": 20 + (enemy_number * 5),
        "gold": 10 + (enemy_number * 3)
    }

    return enemy_data


def create_boss(player):

    bosses = {
        10: "Goblin King",
        20: "Forest Guardian",
        30: "Ancient Golem",
        40: "Vampire Lord",
        50: "Dragon Rider",
        60: "Demon General",
        70: "Ice Titan",
        80: "Shadow Emperor",
        90: "Celestial Dragon",
        100: "Ancient Demon King"
    }

    boss_name = bosses.get(player["level"])

    if boss_name is None:
        print("No boss available at this level!")
        return None

    boss = {
        "name": boss_name,
        "hp": player["level"] * 50,
        "attack": player["level"] * 3,
        "defense": player["level"],
        "exp": player["level"] * 100,
        "gold": player["level"] * 50,
        "is_boss": True
    }

    return boss


def get_region(player):

    regions = {
        1: "Village",
        2: "Forest",
        3: "Cave",
        4: "Desert",
        5: "Ruins",
        6: "Castle",
        7: "Volcano",
        8: "Frozen Mountain",
        9: "Sky Temple",
        10: "Demon Realm"
    }

    region_number = (player["level"] - 1) // 10 + 1

    if region_number > 10:
        region_number = 10

    return regions[region_number]

    
def player_attack(player, enemy):

    weapon_bonus = 0

    if player["weapon"] is not None:
        weapon_bonus = player["weapon"]["damage"]

    damage = player["attack"] + weapon_bonus - enemy["defense"]

    if damage < 1:
        damage = 1

    chance = random.randint(1, 100)

    if chance <= player["critical_chance"]:

        damage = int(damage * player["critical_damage"])

        print("\n!!! CRITICAL HIT !!!")

    enemy["hp"] = enemy["hp"] - damage

    print("\nYou attacked", enemy["name"])
    print("Damage:", damage)
    print("Enemy remaining HP:", max(0, enemy["hp"]))

def enemy_attack(player, enemy, defending):

    enemy["turns"] = enemy.get("turns", 0) + 1

    armor_bonus = 0

    if player["armor"] is not None:
        armor_bonus = player["armor"]["defense"]

    damage = enemy["attack"] - player["defense"] - armor_bonus

    if enemy.get("is_boss", False) and enemy["turns"] % 3 == 0:

        print("\n!!! BOSS SPECIAL ATTACK !!!")
        print(enemy["name"], "uses a powerful special attack!")

        damage = int(enemy["attack"] * 1.5) - player["defense"] - armor_bonus

    if defending:
        damage = damage // 2

    if damage < 1:
        damage = 1

    player["hp"] -= damage

    print("\n", enemy["name"], "attacked you!")
    print("Damage received:", damage)
    print("Your remaining HP:", max(0, player["hp"]))



def heal_player(player):

    print("\n======= HEALING =======")

    heal_amount = 30

    if player["hp"] == player["max_hp"]:

        print("Your health is already full!")
        return

    player["hp"] = player["hp"] + heal_amount

    if player["hp"] > player["max_hp"]:
        player["hp"] = player["max_hp"]

    print("You recovered", heal_amount, "HP!")
    print("Your current HP:", player["hp"])


def level_up(player):

    while player["exp"] >= player["level"] * 100 and player["level"] < 100:

        required_exp = player["level"] * 100

        player["exp"] -= required_exp
        player["level"] += 1

        print("\n========== LEVEL UP! ==========")
        print("Congratulations!")
        print("Your new level:", player["level"])

        player["max_hp"] += 20
        player["hp"] = player["max_hp"]

        player["max_mana"] += 10
        player["mana"] = player["max_mana"]

        player["attack"] += 5
        player["defense"] += 3

        print("HP increased!")
        print("Mana increased!")
        print("Attack increased!")
        print("Defense increased!")

        if player["level"] % 5 == 0:

            print("\n===== CLASS PASSIVE BONUS =====")

            if player["class"] == "Warrior":
                player["defense"] += 5
                print("Warrior: Defense +5")

            elif player["class"] == "Mage":
                player["max_mana"] += 20
                player["mana"] += 20
                print("Mage: Maximum Mana +20")

            elif player["class"] == "Archer":
                player["critical_chance"] = min(
                    75, player["critical_chance"] + 5
                )
                print("Archer: Critical Chance +5")

            elif player["class"] == "Assassin":
                player["critical_chance"] = min(
                    75, player["critical_chance"] + 5
                )
                print("Assassin: Critical Chance +5")

        print("\nNew Region:", get_region(player))

    if player["level"] == 100:
        print("\nYOU HAVE REACHED MAXIMUM LEVEL 100!")

def equip_weapon(player):

    print("\n======= WEAPON SHOP =======")
    print("1. Iron Sword (+5 damage)")
    print("2. Steel Sword (+10 damage)")
    print("3. Magic Sword (+15 damage)")

    choice = input("Choose a weapon: ")

    if choice == "1":
        player["weapon"] = {"name": "Iron Sword", "damage": 5}

    elif choice == "2":
        player["weapon"] = {"name": "Steel Sword", "damage": 10}

    elif choice == "3":
        player["weapon"] = {"name": "Magic Sword", "damage": 15}

    else:
        print("Invalid weapon choice!")
        return

    print("\nYou equipped:", player["weapon"]["name"])
    print("Weapon damage bonus:", player["weapon"]["damage"])


def use_potion(player):

    print("\n======= POTION =======")
    print("1. Small Health Potion (+30 HP)")
    print("2. Large Health Potion (+60 HP)")
    print("3. Mana Potion (+30 Mana)")
    print("4. Back")

    choice = input("Choose a potion: ")

    if choice == "1":
        potion_name = "Small Health Potion"
        heal_amount = 30
        potion_type = "hp"

    elif choice == "2":
        potion_name = "Large Health Potion"
        heal_amount = 60
        potion_type = "hp"

    elif choice == "3":
        potion_name = "Mana Potion"
        heal_amount = 30
        potion_type = "mana"

    elif choice == "4":
        return

    else:
        print("Invalid choice!")
        return

    if potion_name not in player["potions"]:
        print("You don't have this potion!")
        return

    if potion_type == "hp":

        if player["hp"] == player["max_hp"]:
            print("Your HP is already full!")
            return

        player["hp"] = min(player["hp"] + heal_amount, player["max_hp"])
        print("HP restored!")

    else:

        if player["mana"] == player["max_mana"]:
            print("Your mana is already full!")
            return

        player["mana"] = min(player["mana"] + heal_amount, player["max_mana"])
        print("Mana restored!")

    player["potions"].remove(potion_name)

    print("You used:", potion_name)
    print("HP:", player["hp"], "/", player["max_hp"])
    print("Mana:", player["mana"], "/", player["max_mana"])


def use_skill(player, enemy):

    skills = {
        "Warrior": [
            ("Slash", 10, 25),
            ("Shield Bash", 15, 30),
            ("Rage", 20, 40),
            ("Earthquake", 30, 60)
        ],

        "Mage": [
            ("Fireball", 10, 30),
            ("Ice Blast", 15, 40),
            ("Thunder Strike", 20, 50),
            ("Meteor", 30, 70)
        ],

        "Archer": [
            ("Multi Shot", 10, 25),
            ("Poison Arrow", 15, 35),
            ("Explosive Arrow", 20, 50),
            ("Sniper Shot", 30, 65)
        ],

        "Assassin": [
            ("Backstab", 10, 30),
            ("Smoke Bomb", 15, 35),
            ("Shadow Strike", 20, 50),
            ("Instant Kill", 30, 70)
        ]
    }

    print("\n======= YOUR SKILLS =======")

    player_skills = skills[player["class"]]

    for i, skill in enumerate(player_skills, start=1):
        print(i, skill[0], "- Mana:", skill[1], "- Damage:", skill[2])

    choice = input("Choose a skill (1-4): ")

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid skill choice!")
        return

    skill = player_skills[int(choice) - 1]

    skill_name = skill[0]
    mana_cost = skill[1]
    skill_damage = skill[2]

    if player["mana"] < mana_cost:
        print("Not enough mana!")
        return

    player["mana"] -= mana_cost

    damage = skill_damage - enemy["defense"]

    if damage < 1:
        damage = 1

    enemy["hp"] -= damage

    print("\nYou used", skill_name + "!")
    print("Damage:", damage)
    print("Remaining mana:", player["mana"])
    print("Enemy remaining HP:", max(0, enemy["hp"]))


def view_inventory(player):

    print("\n========== INVENTORY ==========")

    print("Gold:", player["gold"])

    print("\nEquipped Weapon:")

    if player["weapon"] is not None:
        print(player["weapon"]["name"])
    else:
        print("No weapon equipped")

    print("\nEquipped Armor:")

    if player["armor"] is not None:
        print(player["armor"]["name"])
    else:
        print("No armor equipped")

    print("\nPotions:")

    if len(player["potions"]) == 0:
        print("No potions available")

    else:
        for potion in player["potions"]:
            print("-", potion)

    print("\n================================")
 
def enemy_loot(player, enemy):

    print("\n======= ENEMY REWARDS =======")

    bonus_gold = random.randint(5, 20)

    if enemy.get("is_boss", False):
        bonus_gold += 100

        potion = random.choice([
            "Small Health Potion",
            "Large Health Potion",
            "Mana Potion"
        ])

        player["potions"].append(potion)

        print("BOSS REWARD!")
        print("Guaranteed potion:", potion)
        print("Bonus gold:", bonus_gold)

    else:

        print("Bonus gold:", bonus_gold)

        chance = random.randint(1, 100)

        if chance <= 40:
            potion = random.choice([
                "Small Health Potion",
                "Large Health Potion",
                "Mana Potion"
            ])

            player["potions"].append(potion)
            print("You found:", potion)

        else:
            print("No potion dropped this time!")

    player["gold"] += bonus_gold

    print("Total gold:", player["gold"])
 
    


def shop(player):

    while True:

        print("\n========== ELDORIA SHOP ==========")
        print("Your Gold:", player["gold"])
        print("\n1. Iron Sword (+5 damage) - 50 Gold")
        print("2. Steel Sword (+10 damage) - 100 Gold")
        print("3. Small Health Potion (+30 HP) - 20 Gold")
        print("4. Large Health Potion (+60 HP) - 40 Gold")
        print("5. Mana Potion (+30 Mana) - 25 Gold")
        print("6. Leather Armor (+5 defense) - 40 Gold")
        print("7. Iron Armor (+10 defense) - 80 Gold")
        print("8. Exit Shop")

        choice = input("Choose an item: ")

        if choice == "1":
            item_name = "Iron Sword"
            price = 50
            item = {"name": "Iron Sword", "damage": 5}

        elif choice == "2":
            item_name = "Steel Sword"
            price = 100
            item = {"name": "Steel Sword", "damage": 10}

        elif choice == "3":
            item_name = "Small Health Potion"
            price = 20
            item = None

        elif choice == "4":
            item_name = "Large Health Potion"
            price = 40
            item = None

        elif choice == "5":
            item_name = "Mana Potion"
            price = 25
            item = None

        elif choice == "6":
            item_name = "Leather Armor"
            price = 40
            item = {"name": "Leather Armor", "defense": 5}

        elif choice == "7":
            item_name = "Iron Armor"
            price = 80
            item = {"name": "Iron Armor", "defense": 10}

        elif choice == "8":
            print("Leaving the shop...")
            break

      

        else:
            print("Invalid choice!")
            continue

        if player["gold"] < price:
            print("Not enough gold!")
            continue

        player["gold"] -= price

        
    if item is not None:

        if "damage" in item:
            player["weapon"] = item

        elif "defense" in item:
            player["armor"] = item

            print("You equipped:", item_name)
        else:
            player["potions"].append(item_name)
            print("You purchased:", item_name)

        print("Remaining gold:", player["gold"])



def manage_inventory(player):

    while True:

        print("\n======= MANAGE INVENTORY =======")
        print("1. Unequip Weapon")
        print("2. Unequip Armor")
        print("3. Sell Weapon")
        print("4. Sell Armor")
        print("5. Drop a Potion")
        print("6. Back")

        choice = input("Choose an option: ")

        if choice == "1":

            if player["weapon"] is None:
                print("No weapon equipped!")
            else:
                print("Unequipped:", player["weapon"]["name"])
                player["weapon"] = None

        elif choice == "2":

            if player["armor"] is None:
                print("No armor equipped!")
            else:
                print("Unequipped:", player["armor"]["name"])
                player["armor"] = None

        elif choice == "3":

            if player["weapon"] is None:
                print("No weapon to sell!")
            else:
                print("Sold:", player["weapon"]["name"])
                player["gold"] += 25
                player["weapon"] = None
                print("You received 25 gold!")

        elif choice == "4":

            if player["armor"] is None:
                print("No armor to sell!")
            else:
                print("Sold:", player["armor"]["name"])
                player["gold"] += 20
                player["armor"] = None
                print("You received 20 gold!")

        elif choice == "5":

            if len(player["potions"]) == 0:
                print("No potions to drop!")
            else:
                for i, potion in enumerate(player["potions"], start=1):
                    print(i, potion)

                try:
                    number = int(input("Enter potion number to drop: "))

                    if 1 <= number <= len(player["potions"]):
                        dropped = player["potions"].pop(number - 1)
                        print("Dropped:", dropped)
                    else:
                        print("Invalid potion number!")

                except ValueError:
                    print("Please enter a number!")

        elif choice == "6":
            break

        else:
            print("Invalid choice!")

        print("Current gold:", player["gold"])

def save_game(player):

    try:
        with open("save_game.json", "w") as file:
            json.dump(player, file, indent=4)

        print("\nGame saved successfully!")

    except Exception as error:
        print("Error saving game:", error)

def load_game():

    try:
        with open("save_game.json", "r") as file:
            player = json.load(file)

        print("\nGame loaded successfully!")
        print("Welcome back,", player["name"])

        return player

    except FileNotFoundError:
        print("\nNo saved game found.")
        return None

    except Exception as error:
        print("Error loading game:", error)
        return None


def instructions():

    print("\n========== GAME INSTRUCTIONS ==========")

    print("\n1. Create your character.")
    print("2. Choose a character class.")
    print("3. Fight enemies to earn EXP and gold.")
    print("4. Use skills and potions during battles.")
    print("5. Buy weapons and armor from the shop.")
    print("6. Level up to become stronger.")
    print("7. Fight powerful bosses every 10 levels.")
    print("8. Save your progress using Save Game.")
    print("9. Reach level 100 to defeat the final boss.")

    print("\n=======================================")

def battle(player, enemy):

    print("\n========== BATTLE START ==========")
    print(player["name"], "vs", enemy["name"])
    if enemy.get("is_boss", False):
        print("\n!!! BOSS BATTLE !!!")
        print("A powerful boss has appeared!")

    while player["hp"] > 0 and enemy["hp"] > 0:

        print("\n------ BATTLE MENU ------")
        print("1. Attack")
        print("2. Defend")
        print("3. Run")
        print("4. View Stats")
        print("5. Heal")
        print("6. Use Potion")
        print("7. View Inventory")
        print("8. Use Skills")
        print("9. Visit Shop")
        print("10. Manage Inventory")
        print("11. Save Game")

        choice = input("Choose your action: ")

        defending = False

        if choice == "1":
            player_attack(player, enemy)
            

        elif choice == "2":

            defending = True
            print("\nYou are defending!")

        elif choice == "3":

            print("\nYou escaped from the battle!")
            return

        elif choice == "4":

            view_stats(player)
            
        elif choice == "5":
            heal_player(player)

        elif choice == "6":
            use_potion(player)
        elif choice == "7":
            view_inventory(player)
    
        elif choice == "8":
            use_skill(player, enemy)

        elif choice == "9":
            shop(player)

        elif choice == "10":
            manage_inventory(player)

        elif choice == "11":
            save_game(player)
            continue
            

          

        else:

            print("\nInvalid choice!")
            continue

       

        if enemy["hp"] <= 0:
            print("\n===== ENEMY DEFEATED! =====")

            print("You defeated:", enemy["name"])

            player["exp"] += enemy["exp"]
            player["gold"] += enemy["gold"]
            player["enemies_defeated"] += 1

            if enemy.get("is_boss", False):

                player["bosses_defeated"] += 1

                print("\n===== BOSS DEFEATED! =====")
                print("Congratulations! You defeated a powerful boss!")

                bonus_gold = 500
                player["gold"] += bonus_gold

                print("Boss bonus gold:", bonus_gold)
                print("Total bosses defeated:", player["bosses_defeated"])

            print("EXP gained:", enemy["exp"])
            print("Gold earned:", enemy["gold"])

            enemy_loot(player, enemy)

            level_up(player)

            return

        # -------Enemy attack------

        enemy_attack(player, enemy, defending)

    # -------Battle------

    if player["hp"] <= 0:

        player["hp"] = 0
        print("\nGAME OVER! You were defeated.")
        return

    else:

        print("\nCongratulations! You defeated", enemy["name"])

        player["exp"] += enemy["exp"]
        player["gold"] += enemy["gold"]
        player["enemies_defeated"] += 1
        if enemy.get("is_boss", False):
            player["bosses_defeated"] += 1

        enemy_loot(player, enemy)

        level_up(player)


        print("EXP earned:", enemy["exp"])
        print("Gold earned:", enemy["gold"])

    if player["level"] in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] and not enemy.get("is_boss", False):

        boss = create_boss(player)

        if boss is not None:
            print("\nA BOSS IS APPROACHING!")
            print("Boss:", boss["name"])
            battle(player, boss)


def main_menu():
    while True:
        print("\n=====================================")
        print("     LEGENDS OF A FORGOTTEN REALM")
        print("=======================================")
        print("1.   NEW GAME")
        print("2.   CONTINUE")
        print("3.   INSTRUCTION")
        print("4.   EXIT")


        ch=input("Enter your choice: ")
        print(" ")

        if ch=="1":
            print("Starting a new game... ")
            player = character()
            print("\n Welcome to your adventure,",player["name"])
            equip_weapon(player)
            view_stats(player)

            print("\n======= CURRENT REGION =======")
            print("You are exploring:", get_region(player))
            enemy = create_enemy(player)
            
            print("\n====== ENEMY APPEARED ======")
            print("Enemy:", enemy["name"])
            print("HP:", enemy["hp"])
            print("Attack:", enemy["attack"])
            while player["hp"] > 0:

                print("\n========== NEW ADVENTURE ==========")
                print("Region:", get_region(player))

                enemy = create_enemy(player)

                print("\nEnemy appeared:", enemy["name"])
                print("Enemy HP:", enemy["hp"])

                battle(player, enemy)

                if player["hp"] <= 0:
                    print("\nGAME OVER!")
                    break

                choice = input("\nContinue your adventure? (yes/no): ").lower()

                if choice != "yes":
                    save_game(player)
                    break
            
            


        elif ch == "2":
            player = load_game()

            if player is not None:
                view_stats(player)

                print("\nYou are exploring:", get_region(player))
                
                while player["hp"] > 0:

                    print("\n========== NEW ADVENTURE ==========")
                    print("Region:", get_region(player))

                    enemy = create_enemy(player)

                    print("\nEnemy appeared:", enemy["name"])
                    print("Enemy HP:", enemy["hp"])

                    battle(player, enemy)

                    if player["hp"] <= 0:
                        print("\nGAME OVER!")
                        break

                    choice = input("\nContinue your adventure? (yes/no): ").lower()

                    if choice != "yes":
                        save_game(player)
                        break

        elif ch=="3":
            instructions()

        elif ch=="4":
            print("Thankyou for playing! ")
            break
        else:
            print("Invalid choice ! Try again !!")


main_menu()