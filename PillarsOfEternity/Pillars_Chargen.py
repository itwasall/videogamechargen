#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import choice

from PillarsRace import SUBRACES, ALL_SUBRACES, RACES
from PillarsAttribute import ATTRIBUTES, STAT_BLOCK 

class Character:
    def __init__(self, name):
        self.name = name
        self.gender = None
        self.race = None
        self.subrace = None
        self.char_class = None
        self.attributes = STAT_BLOCK


def gen_race(c: Character, race: str = None):
    if race is None or race not in ['Human', 'Aumauna', 'Dwarf', 'Elf', 'Orlan', 'Godlike']:
        r = choice(ALL_SUBRACES)
    else:
        r = choice(SUBRACES[race])
    print(r.subrace_name)

jerry = Character('Jerry')
print(jerry.attributes.might)
