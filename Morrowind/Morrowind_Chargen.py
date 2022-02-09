from MorrowindRace import MW_RACES
from MorrowindSkill import MW_SKILLS

print([skill.name for skill in MW_SKILLS])
print("====")
print([race.name for race in MW_RACES])

class Character:
    def __init__(
        self,
        name: str,
        race: str,
        gender: str,
        char_class: str,
    ):
        self.name = name
        self.race = race
        self.gender = gender
        self.char_class = char_class
