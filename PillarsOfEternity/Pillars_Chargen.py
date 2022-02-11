#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import choice

from PillarsRace import SUBRACES, ALL_SUBRACES, RACES
from PillarsAttribute import ATTRIBUTES, STAT_BLOCK
from PillarsSkill import SKILLS
from PillarsClass import choice_class_exception_resolver, CLASSES, PClass_Wizard
from PillarsCulture import CULTURES, BACKGROUNDS, Pillars_Background

class Character:
    def __init__(self, name):
        # Initing a bunch of stuff to be overwritten later by each gen_x function
        self.name = name
        self.gender = None
        self.race = None
        self.subrace = None
        self.char_class = None
        self.char_class_extra = {}
        self.culture = None
        self.background = None
        # Technically creates redundancy as it'll produce
        # self.attributes['NameofThing'].name = 'NameofThing'
        # but I get to utilise the __add__ method in the attribute class this way
        self.attributes = {i.name: i for i in ATTRIBUTES}
        # Same deal for skills
        self.skills = {i.name: i for i in SKILLS}
        self.abilities = []

    def character_info(self):
        print(self.name)
        print(self.subrace)
        print(f"{self.culture}, {self.background}")
        # e.g.
        # Might: 1,  Constitution: -1
        # Athletics: 0,  Lore: 1
        print(",  ".join([f"{a}: {b}" for a, b in zip([i for i in self.attributes.keys()], [self.attributes[i].value for i in self.attributes])]))
        print(",  ".join([f"{a}: {b}" for a, b in zip([i for i in self.skills.keys()], [self.skills[i].rank for i in self.skills])]))


def gen_race(c: Character, race: str = None):
    if race is None or race not in ['Human', 'Aumauna', 'Dwarf', 'Elf', 'Orlan', 'Godlike']:
        r = choice(ALL_SUBRACES)
    else:
        r = choice(SUBRACES[race])
    c.subrace = r
    c.race = r.parent
    c.abilities.append(r.ability)
    # For each attribute in characters attributes, check if in race attribute and add bonus
    for attrib in c.attributes.keys():
        if attrib in r.attribute_bonus.keys():
            c.attributes[attrib] += r.attribute_bonus[attrib]

def gen_class(c: Character):
    cl = choice(CLASSES)
    c.char_class = cl
    # Lol
    c.char_class_extra = choice_class_exception_resolver(cl.name, c)

def gen_culture_background(c: Character):
    cul = choice(CULTURES)
    back = None
    while back is None or (isinstance(back, Pillars_Background) and not back.reqs_fulfilled):
        back = choice(BACKGROUNDS)
        back.check_requirements(cul)
    c.culture = cul
    c.background = back
    # Same as when genning a race
    for attrib in c.attributes.keys():
        if attrib in cul.attribute_bonus.keys():
            c.attributes[attrib] += cul.attribute_bonus[attrib]
    # Same as above, but for skills
    for skill in c.skills.keys():
        if skill in back.skill_bonus.keys():
            c.skills[skill] += back.skill_bonus[skill]


jerry = Character('Jerry')

gen_class(jerry)
gen_race(jerry)
gen_culture_background(jerry)
jerry.character_info()