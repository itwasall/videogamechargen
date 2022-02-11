#!/usr/bin/env python
# -*- coding: utf-8 -*-
from yaml import safe_load
from random import choice

import PillarsClassExtra as PiCE

data = safe_load(open('PillarsOfEternity/data/Class.yml', 'rt'))
c_data = data['classes']

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

CLASSES = [PClass_Barbarian, PClass_Chanter, PClass_Cipher, PClass_Druid, PClass_Fighter,
           PClass_Monk, PClass_Paladin, PClass_Priest, PClass_Ranger, PClass_Rogue, PClass_Wizard]

def choice_class_exception_resolver(query, c):
    if query == 'Chanter':
        # Choose two first level chant phrases and one first level invocation
        phrases = [choice(data['chanter_phrases']) for _ in range(2)]
        while phrases[0] == phrases[1]:
            phrases[1] = choice(data['chanter_phrases'])
        phrases_out = [PiCE.Pillars_ChanterPhrase(i['name'], i['area'], i['effect'], i['duration'], i['desc'], i['linger']) for i in phrases]
        inv = choice(data['chanter_invocations'])
        return {'Phrases': phrases_out, 'Invocation': PiCE.Pillars_ChanterInvocation(inv['name'], inv['area'], inv['effect'], inv['speed'], inv['duration'], inv['interrupt'], inv['range'], inv['desc'])}
    elif query == 'Cipher':
        # Choose two first level powers
        powers = [choice(data['cipher_spells']) for _ in range(2)]
        while powers[0] == powers[1]:
            powers[1] = choice(data['cipher_spells'])
        powers_out = [PiCE.Pillars_CipherSpells(i['name'], i['area'], i['effect'], i['focus_cost'], i['speed'], i['duration'], i['range'], i['desc']) for i in powers]
        return {'Cipher Powers': powers_out}
    elif query == 'Druid':
        # Choose a spiritshift form
        druid_form = choice(data['druid_shapeshift'])
        return {'Shapeshift Form': PiCE.Pillars_DruidShapeshift(druid_form['name'], druid_form['form'], druid_form['damage_type'], druid_form['abilities'], druid_form['weapon'], druid_form['armour'])}
    elif query == 'Paladin':
        # Choose an order
        o = choice(data['paladin_order'])
        return {'Order': PiCE.Pillars_PaladinOrder(o['name'], o['favoured_behaviours'], o['disfavoured_behaviours'])}
    elif query == 'Priest':
        # Choose a deity
        o = choice(data['priest_deity'])
        return {'Deity': PiCE.Pillars_PriestDeity(o['name'], o['favoured_dispositions'], o['condemed_dispositions'], o['favoured_weapons'], o['talent'])}
    elif query == 'Ranger':
        # Choose an animal companion
        o = choice(data['ranger_animal_companion'])
        return {'Animal Companion': PiCE.Pillars_RangerAnimalCompanion(o['name'], o['stat_block'], o['DR'], o['abilities'], o['effect'])}
    elif query == 'Wizard':
        # Choose first four first level wizard spells
        spells = []
        for i in range(4):
            spell = (choice(data['wizard_spells']))
            while spell in spells:
                spell = (choice(data['wizard_spells']))
            spells.append(spell)
        spells_out = [PiCE.Pillars_WizardSpells(i['name'], i['area'], i['effect'], i['duration'], i['speed'], i['range']) for i in spells]
        return {'Spells': spells_out}
    return {}
