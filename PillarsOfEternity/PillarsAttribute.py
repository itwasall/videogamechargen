#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Pillars_Attribute:
    def __init__(self, name, value: int = 0):
        self.name = name
        self.value = value

    def __add__(self, x: int):
        return Pillars_Attribute(self.name, (self.value + x))

    def __repr__(self):
        return f"{self.name}: {self.value}"

class Pillars_AttributeBlock:
    def __init__(
        self,
        mig: Pillars_Attribute,
        con: Pillars_Attribute,
        dex: Pillars_Attribute,
        per: Pillars_Attribute,
        inte: Pillars_Attribute,
        res: Pillars_Attribute
    ):
        self.might = mig
        self.constitution = con
        self.dexterity = dex
        self.personality = per
        self.intelligence = inte
        self.resolve = res
        self.attribute_list = [self.might, self.constitution, self.dexterity, self.personality,
                               self.intelligence, self.resolve]

    def __repr__(self):
        return "\n".join([i.__repr__() for i in self.attribute_list])


PAttribute_MIG = Pillars_Attribute('Might')
PAttribute_CON = Pillars_Attribute('Constitution')
PAttribute_DEX = Pillars_Attribute('Dexterity')
PAttribute_PER = Pillars_Attribute('Personality')
PAttribute_INT = Pillars_Attribute('Intelligence')
PAttribute_RES = Pillars_Attribute('Resolve')

ATTRIBUTES = [PAttribute_MIG, PAttribute_CON, PAttribute_DEX, PAttribute_PER, PAttribute_INT, PAttribute_RES]

STAT_BLOCK = Pillars_AttributeBlock(PAttribute_MIG, PAttribute_CON, PAttribute_DEX, PAttribute_PER, PAttribute_INT, PAttribute_RES)
