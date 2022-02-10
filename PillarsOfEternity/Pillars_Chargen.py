#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import choice

from Pillars_Race import SUBRACES, ALL_SUBRACES, RACES

class Character:
    def __init__(self, name):
        self.name = name
        self.gender = None
        self.race = None
        self.subrace = None
        self.char_class = None
        self.attributes = None


def gen_race(c: Character, race: str = None):
    if race is None or race not in ['Human', 'Aumauna', 'Dwarf', 'Elf', 'Orlan', 'Godlike']:
        r = choice(ALL_SUBRACES)
    else:
        r = choice(SUBRACES[race])

