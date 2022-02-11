#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Pillars_Skill:
    def __init__(self, name, rank: int=0):
        self.name = name
        self.rank = rank

    def __repr__(self):
        return f"{self.name} rank: {self.rank}"

    def __add__(self, x: int):
        return Pillars_Skill(self.name, (self.rank + x))

class Pillars_SkillBlock:
    def __init__(
        self,
        ath: Pillars_Skill,
        lor: Pillars_Skill,
        mec: Pillars_Skill,
        ste: Pillars_Skill,
        sur: Pillars_Skill
    ):
        self.athletics = ath
        self.lore = lor
        self.mechanics = mec
        self.stealth = ste
        self.survival = sur
        self.skill_list = [self.athletics, self.lore,
                           self.mechanics, self.stealth,
                           self.survival]
    def __repr__(self):
        return "\n".join([i.__repr__() for i in self.skill_list])


PSkill_Athletics = Pillars_Skill('Athletics')
PSkill_Lore = Pillars_Skill('Lore')
PSkill_Mechanics = Pillars_Skill('Mechanics')
PSkill_Stealth = Pillars_Skill('Stealth')
PSkill_Survival = Pillars_Skill('Survival')

SKILLS = [PSkill_Athletics, PSkill_Lore, PSkill_Mechanics, PSkill_Stealth, PSkill_Survival]
SKILL_BLOCK = Pillars_SkillBlock(PSkill_Athletics, PSkill_Lore, PSkill_Mechanics, PSkill_Stealth, PSkill_Survival)
