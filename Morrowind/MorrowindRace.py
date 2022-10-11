#!/usr/bin/env python
# -*- coding: utf-8 -*-
from yaml import safe_load
from os import getcwd

try:
    race_data = safe_load(open('Morrowind/data/Race.yml', 'rt'))
except FileNotFoundError:
    race_data = safe_load(open(f'{getcwd()}\\data\\Race.yml', 'rt'))


class MW_Race:
    def __init__(self, race_name, race_data: dict):
        self.name = race_name
        self.male_attributes = race_data['Male']['Attributes']
        self.male_height = race_data['Male']['Height']
        self.male_weight = race_data['Male']['Weight']
        self.female_attributes = race_data['Female']['Attributes']
        self.female_height = race_data['Female']['Height']
        self.female_weight = race_data['Female']['Weight']
        self.skills = race_data['Skills']
        self.magicka_mult_bonus = race_data['Magicka Multiplier Bonus']
        if race_data['Resists']:
            self.resists = [race_data['Resists'][i] for i in race_data['Resists']] # Should catch the "no" clause in yml data
        else:
            self.resists = None

    def __repr__(self):
        return self.name

MWRace_Argonian = MW_Race('Argonian', race_data['Argonian'])
MWRace_Breton = MW_Race('Breton', race_data['Breton'])
MWRace_DarkElf = MW_Race('Dark Elf', race_data['DarkElf'])
MWRace_HighElf = MW_Race('High Elf', race_data['HighElf'])
MWRace_Imperial = MW_Race('Imperial', race_data['Imperial'])
MWRace_Khajiit = MW_Race('Khajiit', race_data['Khajiit'])
MWRace_Nord = MW_Race('Nord', race_data['Nord'])
MWRace_Orc = MW_Race('Ord', race_data['Orc'])
MWRace_Redguard = MW_Race('Redguard', race_data['Redguard'])
MWRace_WoodElf = MW_Race('Wood Elf', race_data['WoodElf'])

MW_RACES = [
    MWRace_Argonian,
    MWRace_Breton,
    MWRace_DarkElf,
    MWRace_HighElf,
    MWRace_Imperial,
    MWRace_Khajiit,
    MWRace_Nord,
    MWRace_Orc,
    MWRace_Redguard,
    MWRace_WoodElf
]
