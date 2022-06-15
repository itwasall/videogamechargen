#!/usr/bin/env python
# -*- coding: utf-8 -*-
from yaml import safe_load
from os import getcwd

try:
    race_data = safe_load(open('Oblivion/data/Race.yml', 'rt'))
except FileNotFoundError:
    race_data = safe_load(open(f'{getcwd()}\\data\\Race.yml','rt'))

class Oblivion_Race:
    def __init__(self, race_name, race_data):
        self.name = race_name
        self.male_attributes = race_data['Male']['Attributes']
        self.male_height = race_data['Male']['Height']
        self.male_weight = race_data['Male']['Weight']
        self.female_attributes = race_data['Female']['Attributes']
        self.female_height = race_data['Female']['Height']
        self.female_weight = race_data['Female']['Weight']
        self.skills = race_data['Skills']
        self.magicka_bonus = race_data['Magicka Bonus']
        if race_data['Resists']:
            self.resists = [race_data['Resists'][i] for i in race_data['Resists']]
        else:
            self.resists = None

    def __repr__(self):
        return self.name


OblRace_Argonian = Oblivion_Race('Argonian', race_data['Argonian'])
OblRace_Breton = Oblivion_Race('Breton', race_data['Breton'])
OblRace_DarkElf = Oblivion_Race('Dark Elf', race_data['Dunmer'])
OblRace_HighElf = Oblivion_Race('High Elf', race_data['Altmer'])
OblRace_Imperial = Oblivion_Race('Imperial', race_data['Imperial'])
OblRace_Khajiit = Oblivion_Race('Khajiit', race_data['Khajiit'])
OblRace_Nord = Oblivion_Race('Nord', race_data['Nord'])
OblRace_Orc = Oblivion_Race('Ord', race_data['Orc'])
OblRace_Redguard = Oblivion_Race('Redguard', race_data['Redguard'])
OblRace_WoodElf = Oblivion_Race('Wood Elf', race_data['Bosmer'])

OBL_RACES = [OblRace_Argonian, OblRace_Breton, OblRace_DarkElf, OblRace_HighElf, OblRace_Imperial, OblRace_Khajiit, OblRace_Nord, OblRace_Orc, OblRace_Redguard, OblRace_WoodElf]
