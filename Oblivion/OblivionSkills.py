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
        self.blade = skill_list[0]
        self.blunt = skill_list[1]
        self.handtohand = skill_list[2]
        self.armorer = skill_list[3]
        self.block = skill_list[4]
        self.heavyarmor = skill_list[5]
        self.athletics = skill_list[6]
        self.acrobatics = skill_list[7]
        self.lightarmor = skill_list[8]
        self.security = skill_list[9]
        self.sneak = skill_list[10]
        self.marksman = skill_list[11]
        self.mercantile = skill_list[12]
        self.speechcraft = skill_list[13]
        self.illusion= skill_list[14]
        self.alchemy = skill_list[15]
        self.conjuration = skill_list[16]
        self.mysticism = skill_list[17]
        self.alteration = skill_list[18]
        self.destruction = skill_list[19]
        self.restoration = skill_list[20]
        

s = 'Combat'
# Strength
a = 'Stregnth'
OblSkill_Blade = Oblivion_Skill('Blade', a, s)
OblSkill_Blunt = Oblivion_Skill('Blunt', a, s)
OblSkill_HandtoHand = Oblivion_Skill('Hand to Hand', a, s)
# Endurance
a = 'Endurance'
OblSkill_Armorer = Oblivion_Skill('Armorer', a, s)
OblSkill_Block = Oblivion_Skill('Block', a, s)
OblSkill_HeavyArmor = Oblivion_Skill('Heavy Armor', a, s)
# Speed
a = 'Speed'
OblSkill_Athletics = Oblivion_Skill('Athletics', a, s)
s = 'Stealth'
OblSkill_Acrobatics = Oblivion_Skill('Acrobatics', a, s)
OblSkill_LightArmor = Oblivion_Skill('Light Armor', a, s)
# Agility
a = 'agility'
OblSkill_Security = Oblivion_Skill('Security', a, s)
OblSkill_Sneak = Oblivion_Skill('Sneak', a, s)
OblSkill_Marksman = Oblivion_Skill('Marksman', a, s)
# Personality
a = 'Personality'
OblSkill_Mercantile = Oblivion_Skill('Mercantile', a, s)
OblSkill_Speechcraft = Oblivion_Skill('Speechcraft', a, s)
s = 'Magic'
OblSkill_Illusion = Oblivion_Skill('Illusion', a, s)
# Intelligence
a = 'Intelligence'
OblSkill_Alchemy = Oblivion_Skill('Alchemy', a, s)
OblSkill_Conjuration = Oblivion_Skill('Conjuration', a, s)
OblSkill_Mysticism = Oblivion_Skill('Mysticism', a, s)
# Willpower
a = 'Willpower'
OblSkill_Alteration = Oblivion_Skill('Alteration', a, s)
OblSkill_Destruction = Oblivion_Skill('Destruction', a, s)
OblSkill_Restoration = Oblivion_Skill('Restoration', a, s)

SKILLS = [OblSkill_Blade, OblSkill_Blunt, OblSkill_HandtoHand, OblSkill_Armorer,
          OblSkill_Block, OblSkill_HeavyArmor, OblSkill_Athletics, OblSkill_Acrobatics,
          OblSkill_LightArmor, OblSkill_Security, OblSkill_Sneak, OblSkill_Marksman,
          OblSkill_Mercantile, OblSkill_Speechcraft, OblSkill_Illusion, OblSkill_Alchemy,
          OblSkill_Conjuration, OblSkill_Mysticism, OblSkill_Alteration,
          OblSkill_Destruction, OblSkill_Restoration]

OblSkill_SKILL_LIST = Oblivion_Skill_List(SKILLS)

