#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Oblivion_Skill:
    def __init__(self, name, attribute, specialisation, value=0):
        self.name = name
        self.attribute = attribute
        self.specialisation = specialisation
        self.value = value

    def __add__(self, x):
        return Oblivion_Skill(self.name, self.attribute, self.specialisation, (self.value + x))

    def __repr__(self):
        return f"{self.name}: {self.value}"

    def show_value(self):
        return self.value

class Oblivion_Skill_List:
    def __init__(self, skill_list):
        self._init_skill_list = skill_list
        self.make_skill_list()

    def make_skill_list(self):
        """self._skill_list = [self.blade, self.blunt, self.handtohand, self.armorer, self.block,
                            self.heavyarmor, self.athletics, self.acrobatics, self.lightarmor,
                            self.security, self.sneak, self.marksman, self.speechcraft,
                            self.illusion, self.alchemy, self.conjuration, self.mysticism,
                            self.alteration, self.destruction, self.restoration]
        """
        self.list = [i for i in self._init_skill_list]
    def __iter__(self):
        # Any time iter is called, the skill list gets remade. Horribly inefficent I'd imagine,
        #   but in this context it's an okay enough solution to having the skills represent
        #   their most up to date values
        self.make_skill_list()
        return self.list.__iter__()

    def __repr__(self):
        # I also couldn't figure out how to interface repr with iter so fuck it, compromises
        #   will be taken
        return "Use <character>.skills.list"

# Strength
OblSkill_Blade = Oblivion_Skill('Blade', 'Stregnth','Combat')
OblSkill_Blunt = Oblivion_Skill('Blunt', 'Stregnth', 'Combat')
OblSkill_HandtoHand = Oblivion_Skill('Hand to Hand', 'Stregnth','Combat')
# Endurance
OblSkill_Armorer = Oblivion_Skill('Armorer', 'Endurance', 'Combat')
OblSkill_Block = Oblivion_Skill('Block', 'Endurance','Combat')
OblSkill_HeavyArmor = Oblivion_Skill('Heavy Armor', 'Endurance','Combat')
# Speed
OblSkill_Athletics = Oblivion_Skill('Athletics', 'Speed','Combat')
OblSkill_Acrobatics = Oblivion_Skill('Acrobatics', 'Speed','Stealth')
OblSkill_LightArmor = Oblivion_Skill('Light Armor', 'Speed','Stealth')
# Agility
OblSkill_Security = Oblivion_Skill('Security', 'Agility','Stealth')
OblSkill_Sneak = Oblivion_Skill('Sneak', 'Agility','Stealth')
OblSkill_Marksman = Oblivion_Skill('Marksman', 'Agility','Stealth')
# Personality
OblSkill_Mercantile = Oblivion_Skill('Mercantile', 'Personality','Stealth')
OblSkill_Speechcraft = Oblivion_Skill('Speechcraft', 'Personality','Stealth')
OblSkill_Illusion = Oblivion_Skill('Illusion', 'Personality','Magic')
# Intelligence
OblSkill_Alchemy = Oblivion_Skill('Alchemy', 'Intelligence','Magic')
OblSkill_Conjuration = Oblivion_Skill('Conjuration', 'Intelligence','Magic')
OblSkill_Mysticism = Oblivion_Skill('Mysticism', 'Intelligence','Magic')
# Willpower
OblSkill_Alteration = Oblivion_Skill('Alteration', 'Willpower','Magic')
OblSkill_Destruction = Oblivion_Skill('Destruction', 'Willpower','Magic')
OblSkill_Restoration = Oblivion_Skill('Restoration', 'Willpower','Magic')

SKILLS = [OblSkill_Blade, OblSkill_Blunt, OblSkill_HandtoHand, OblSkill_Armorer,
          OblSkill_Block, OblSkill_HeavyArmor, OblSkill_Athletics, OblSkill_Acrobatics,
          OblSkill_LightArmor, OblSkill_Security, OblSkill_Sneak, OblSkill_Marksman,
          OblSkill_Mercantile, OblSkill_Speechcraft, OblSkill_Illusion, OblSkill_Alchemy,
          OblSkill_Conjuration, OblSkill_Mysticism, OblSkill_Alteration,
          OblSkill_Destruction, OblSkill_Restoration]

OblSkill_SKILL_LIST = Oblivion_Skill_List(SKILLS)

