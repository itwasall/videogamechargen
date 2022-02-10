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

PAttribute_MIG = Pillars_Attribute('Might')
PAttribute_CON = Pillars_Attribute('Constitution')
PAttribute_DEX = Pillars_Attribute('Dexterity')
PAttribute_PER = Pillars_Attribute('Personality')
PAttribute_INT = Pillars_Attribute('Intelligence')
PAttribute_RES = Pillars_Attribute('Resolve')

ATTRIBUTES = [PAttribute_MIG, PAttribute_CON, PAttribute_DEX, PAttribute_PER, PAttribute_INT, PAttribute_RES]
