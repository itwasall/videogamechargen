from random import choice

from MorrowindRace import MW_RACES, MW_Race
from MorrowindSkill import MW_SKILLS, MW_Skill
from MorrowindClass import MW_CLASSES, MW_Class
from MorrowindAttributes import MW_ATTRIBUTES, MW_Attribute
from MorrowindBirthsigns import MW_BIRTHSIGNS, MWBirthsign_Steed

# An inbetween class for birthsigns. This will hold any relevant but non-attribute/skill alterating
#   birthsign properties
class CharacterBirthsign:
    def __init__(self, name, effects):
        self.name = name
        self.effects = effects

    def __repr__(self):
        return self.name

# Main character class. Holds all relevant information
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
        self.birthsign = ""
        self.max_health = 0
        self.max_magicka = 0
        self.max_fatigue = 0
        self.fatigue_regen_per_second = 0
        self.encumbrance = 0

    def char_info(self):
        print(f"Name - {self.name}")
        print(f"Race - {self.race}")
        print(f"Class - {self.char_class}")
        print(f"Birthsign - {self.birthsign}")
        print(f"Attributes - {[a for a in self.attributes]}")
        print(f"Skills - {[s for s in self.skills]}")
        print(f"Health - {self.max_health}")
        print(f"Magicka - {self.max_magicka}")
        print(f"Fatigue - {self.max_fatigue}")
        print(f"Fatigue Regen - {self.fatigue_regen_per_second}")
        print(f"Encumbrance - {self.encumbrance}")


def gen_race(c: Character):
    chosen_race = choice(MW_RACES)
    c.race = chosen_race
    # Choosing gender if one not specified
    if c.gender is None:
        c.gender = choice(['male', 'female'])
    # Setting attributes based on race + gender
    if c.gender.lower() == 'male':
        for it, a in enumerate(c.attributes):
            c.attributes[it] += chosen_race.male_attributes[a.name]
    elif c.gender.lower() == 'female':
        for it, a in enumerate(c.attributes):
            c.attributes[it] += chosen_race.female_attributes[a.name]
    # Setting skills based on race
    for it, s in enumerate(c.skills):
        if s.name in chosen_race.skills:
            c.skills[it] += chosen_race.skills[s.name]


def gen_class(c: Character, verbose: bool = False):
    chosen_class = choice(MW_CLASSES)
    c.char_class = chosen_class.name
    for it, skill in enumerate(c.skills):
        # Adding 10 points for each minor skill in class
        if skill.name in chosen_class.minor_skills:
            c.skills[it] += 10
        # Adding 25 points for each major skill in class
        elif skill.name in chosen_class.major_skills:
            c.skills[it] += 25
            if verbose:
                print(f'{skill.name} is major skill!')
        else:
            continue
    # Adding 10 points for each attribute in class
    for a in c.attributes:
        if a.name in chosen_class.mw_attributes:
            c.attributes[c.attributes.index(a)] += 10
    # Adding 5 points for each skill whose specialisation matches that of class
    for skill in c.skills:
        if skill.specialisation == chosen_class.specialisation:
            c.skills[c.skills.index(skill)] += 5

def gen_birthsign(c: Character, verbose: bool = False):
    chosen_birthsign = choice(MW_BIRTHSIGNS)
    c.birthsign = chosen_birthsign.name
    for item in chosen_birthsign.effect.keys():
        # Discarding all birthsign effects that don't have an immediate effect on character stats
        if item not in ['spell', 'power']:
            # Processing all fortify birthsign abilities
            if 'fortify' in chosen_birthsign.effect[item].keys():
                fort_keys = chosen_birthsign.effect[item]['fortify'].keys()
                # All but magicka multiplier are buffs to c.attributes items, so this edge-case is caught here
                if 'magicka_mult' in fort_keys:
                    c.race.magicka_mult_bonus += chosen_birthsign.effect[item]['fortify']['magicka_mult']
                for a in c.attributes:
                    if a.name in fort_keys:
                        c.attributes[c.attributes.index(a)] += chosen_birthsign.effect[item]['fortify'][a.name]
            # Processing all resistance birthsign abilitiies
            if 'resistance' in chosen_birthsign.effect[item].keys():
                res_keys = chosen_birthsign.effect[item]['resistance'].keys()
                for resist_type in c.race.resists:
                    if resist_type in res_keys:
                        resist_type += res_keys[resist_type]

def calc_derrived_stats(c: Character):
    # Health = (Strength + Endurance) / 2
    c.max_health = (c.attributes[0].value + c.attributes[5].value) / 2
    # Magicka = Intelligence x (1 + Racial Modifier + Birthsign modifier)
    c.max_magicka = c.attributes[1].value * (1 + c.race.magicka_mult_bonus)
    # Fatigue = Strength + Willpower + Agility + Endurance
    c.max_fatigue = c.attributes[0].value + c.attributes[2].value + c.attributes[3].value + c.attributes[5].value
    # Fatigue Regen/s = 2.5 + (0.02 * Endurance)
    c.fatigue_regen_per_second = 2.5 + (0.02 * c.attributes[5].value)
    # Encumbrance = Strength x 5
    c.encumbrance = c.attributes[0].value * 5


def gen_character(name: str, gender: str = None):
    character = Character(name=name, gender=gender)
    gen_race(character)
    gen_class(character)
    gen_birthsign(character)
    calc_derrived_stats(character)
    return character
    
c = gen_character('Jerry')
c.char_info()
