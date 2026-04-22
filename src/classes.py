from dataclasses import dataclass, field, replace
from typing import Optional

@dataclass
class Weapon:
    name: str
    damage: int
    dmg_type: str
    value: int

@dataclass
class Item:
    name: str
    value: int

@dataclass
class CharacterClass:
    name: str
    description: str
    hp: int
    mp: int
    strength: int
    defense: int

    weapon: Optional[Weapon] = None
    inventory: list = field(default_factory=list)


@dataclass
class Character:
    name: str
    c_class: CharacterClass
    inventory: list = field(init=False)
    armor: dict = field(init=False)
    
    def __post_init__(self):
        self.weapon = replace(self.c_class.weapon)
        self.inventory = list(self.c_class.inventory)
        self.armor = {
            "head": None,
            "chest": None,
            "legs": None,
            "feet": None
        }