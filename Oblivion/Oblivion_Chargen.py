#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import choice

from OblivionSkills import OblSkill_SKILL_LIST, SKILLS
from OblivionRace import OBL_RACES
from OblivionClass import OBL_CLASSES

class Character:
    def __init__(self, name):
        self.name = name
        self.skills = OblSkill_SKILL_LIST
        self.attributes = None
        self.birthsign = None
        self.race = None
        self.char_class = None

    def get_skill(self, skill_name=None):
        if skill_name is not None:
            return list(i for i in jerry.skills.list if i.name == skill_name)[0]
        return self.skills.list

def get_class(c: Character):
    class_choice = choice(OBL_CLASSES)
    c.char_class = class_choice
    c.skills.list = [c.skills.list[it] + 10 if skill.name in class_choice.skills
                     else c.skills.list[it] for it, skill in enumerate(c.skills.list)]

    #for it, skill in enumerate(c.skills.list):
    #    if skill.name in class_choice.skills:
    #        c.skills.list[it] += 10

jerry = Character('Jerry')

get_class(jerry)

print(jerry.char_class)
for i in jerry.skills.list:
    if i.value != 0:
        print(i)
