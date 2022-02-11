#!/usr/bin/env python
# -*- coding: utf-8 -*-
from OblivionSkills import OblSkill_SKILL_LIST, SKILLS

class Character:
    def __init__(self, name):
        self.name = name
        self.skills = OblSkill_SKILL_LIST
        self.skill_list = {s.name: s for s in SKILLS}
        self.attributes = None
        self.birthsign = None
        self.race = None

jerry = Character('Jerry')

# jerry.skills['Marksman'] += 10
# print(jerry.skills['Block'])
# print(jerry.skills['Marksman'])

jerry.skills.marksman += 10
print(jerry.skills.block)
print(jerry.skills.marksman)
