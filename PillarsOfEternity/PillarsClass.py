#!/usr/bin/env python
# -*- coding: utf-8 -*-
from yaml import safe_load

c_data = safe_load(open('PillarsOfEternity/data/Class.yml', 'rt'))['classes']

class Pillars_Class:
    def __init__(self, name, data):
        self.name = name
        self.endurance = data['endurance']
        self.health = data['health']
        self.accuracy = data['accuracy']
        self.defenses = data['defenses']
        self.skills = data['skills']
        self.resource = data['resource']

    def __repr__(self):
        return self.name

PClass_Barbarian = Pillars_Class('Barbarian', c_data['Barbarian'])
PClass_Chanter = Pillars_Class('Chanter', c_data['Chanter'])
PClass_Cipher = Pillars_Class('Cipher', c_data['Cipher'])
PClass_Druid = Pillars_Class('Druid', c_data['Druid'])
PClass_Fighter = Pillars_Class('Fighter', c_data['Fighter'])
PClass_Monk = Pillars_Class('Monk', c_data['Monk'])
PClass_Paladin = Pillars_Class('Paladin', c_data['Paladin'])
PClass_Priest = Pillars_Class('Priest', c_data['Priest'])
PClass_Ranger = Pillars_Class('Ranger', c_data['Ranger'])
PClass_Rogue = Pillars_Class('Rogue', c_data['Rogue'])
PClass_Wizard = Pillars_Class('Wizard', c_data['Wizard'])

def choice_class_exception_resolver(query):
    if query == 'chanter':
        # Choose two first level chant phrases and one first level invocation
        pass
    elif query == 'cipher':
        # Choose two first level powers
        pass
    elif query == 'druid':
        # Choose a spiritshift form
        pass
    elif query == 'paladin':
        # Choose an order
        pass
    elif query == 'priest':
        # Choose a deity
        pass
    elif query == 'ranger':
        # Choose an animal companion
        pass
    elif query == 'wizard':
        # Choose first four first level wizard spells