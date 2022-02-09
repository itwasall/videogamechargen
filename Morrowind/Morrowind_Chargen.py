from random import choice

from MorrowindRace import MW_RACES, MW_Race
from MorrowindSkill import MW_SKILLS, MW_Skill
from MorrowindClass import MW_CLASSES, MW_Class
from MorrowindAttributes import MW_ATTRIBUTES, MW_Attribute


class Character:
    def __init__(
        self,
        name: str,
        gender: str = None,
        race: MW_Race = None,
        char_class: MW_Class = None,
    ):
        self.name = name
        self.race = race
        self.gender = gender
        self.char_class = char_class
        self.skills = [skill for skill in MW_SKILLS]
        self.attributes = [a for a in MW_ATTRIBUTES]

def gen_race(c: Character):
    chosen_race = choice(MW_RACES)
    c.race = chosen_race
    if c.gender is None:
        c.gender = choice(['male', 'female'])
    if c.gender.lower() == 'male':
        for it, a in enumerate(c.attributes):
            c.attributes[it] += chosen_race.male_attributes[a.name]
    elif c.gender.lower() == 'female':
        for it, a in enumerate(c.attributes):
            c.attributes[it] += chosen_race.female_attributes[a.name]
    for it, s in enumerate(c.skills):
        if s.name in chosen_race.skills:
            c.skills[it] += chosen_race.skills[s.name]


def gen_class(c: Character):
    chosen_class = choice(MW_CLASSES)
    c.char_class = chosen_class
    for it, skill in enumerate(c.skills):
        print(f'{skill.name} being evaluated...')
        if skill.name in chosen_class.minor_skills:
            c.skills[it] += 15
            print(f'{skill.name} is minor skill!')
        elif skill.name in chosen_class.major_skills:
            c.skills[it] += 30
            print(f'{skill.name} is major skill!')
        else:
            continue
    for a in c.attributes:
        if a.name in chosen_class.mw_attributes:
            a += 10

jerry = Character('a', 'male')
gen_race(jerry)
gen_class(jerry)