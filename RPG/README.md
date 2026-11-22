# Legends of a Forgotten Realm

### Python-Based Role-Playing Game (RPG)

## Project Overview

Legends of a Forgotten Realm is a console-based RPG developed using Python. Set in the fictional kingdom of Eldoria, the game allows players to create characters, engage in turn-based combat, explore different regions, and progress through increasingly challenging enemies.

The objective is to reach Level 100 and defeat the final boss, the Ancient Demon King.

## Game Rules

1. **Character Creation:** Players enter a character name and select one of four classes: Warrior, Mage, Archer, or Assassin. Each class has distinct starting attributes and critical hit probabilities.

2. **Combat:** Players fight randomly generated enemies using physical attacks, defensive actions, class-specific skills, and consumable items.

3. **Victory and Rewards:** Defeating enemies grants experience points (EXP) and gold. Additional rewards include randomly dropped potions. Boss victories provide bonus gold and a guaranteed potion.

4. **Defeat and Escape:** Players can escape from battles without receiving rewards. If player HP reaches zero, the game ends.

5. **Character Progression:** Players level up by accumulating EXP. Each level requires EXP equal to the current level multiplied by 100. Leveling up increases maximum HP, maximum mana, attack, and defense, while restoring HP and mana.

6. **Boss Battles:** Bosses appear at Levels 10, 20, 30, 40, 50, 60, 70, 80, 90, and 100. Each boss has unique attributes based on the player's level.

7. **Equipment and Inventory:** Players can purchase weapons, armor, and potions using gold. Equipment can be equipped, unequipped, or sold, and unused potions can be discarded.

8. **Game Progression:** The game features ten regions, with the player's region determined by their level. Enemy strength increases with player progression.

9. **Game Persistence:** Players can save their progress to a JSON file and continue from the saved character data in a later session.

## Character Classes

| Class | HP | Mana | Attack | Defense | Critical Chance |
|---|---:|---:|---:|---:|---:|
| Warrior | 150 | 30 | 20 | 15 | 5% |
| Mage | 90 | 150 | 25 | 5 | 10% |
| Archer | 110 | 70 | 18 | 10 | 15% |
| Assassin | 85 | 60 | 30 | 5 | 25% |

## Combat Mechanics

- Physical damage is calculated using player attack, weapon damage, and enemy defense.
- Critical hits deal 1.5 times the normal physical attack damage.
- Defensive actions reduce incoming damage by half.
- Skills consume mana and deal damage according to their assigned values, reduced by enemy defense.
- Enemy attacks are reduced by player defense and equipped armor.
- Bosses perform a special attack every third turn.
- Damage cannot fall below 1.

## Character Progression

The game has a maximum level of 100. Each level increases maximum HP by 20, maximum mana by 10, attack by 5, and defense by 3.

Every fifth level grants an additional class-specific passive bonus:

- Warrior: +5 defense.
- Mage: +20 maximum mana.
- Archer: +5% critical chance.
- Assassin: +5% critical chance.

The maximum critical hit chance for Archer and Assassin is 75%.

## Regions and Bosses

| Level | Region | Boss |
|---|---|---|
| 1–9 | Village | — |
| 10–19 | Forest | Goblin King |
| 20–29 | Cave | Forest Guardian |
| 30–39 | Desert | Ancient Golem |
| 40–49 | Ruins | Vampire Lord |
| 50–59 | Castle | Dragon Rider |
| 60–69 | Volcano | Demon General |
| 70–79 | Frozen Mountain | Ice Titan |
| 80–89 | Sky Temple | Shadow Emperor |
| 90–100 | Demon Realm | Celestial Dragon / Ancient Demon King |

## Project Structure

```text
Project/
│
├── RPG/
│   └── RPG.py
│
├── save_game.json
│
└── README.md
```

The main game logic is implemented in `RPG/RPG.py`. The `save_game.json` file stores the player's saved progress.

## Technologies Used

- Python 3
- JSON for game data persistence
- Random module for enemy generation, critical hits, and rewards

