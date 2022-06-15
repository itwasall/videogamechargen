#!/usr/bin/env python
# -*- coding: utf-8 -*-
from yaml import safe_load
from os import getcwd

try:
    r_data = safe_load(open('/PillarsOfEternity/data/Race.yml', 'rt'))
    a_data = safe_load(open('./PillarsOfEternity/data/Abilities.yml', 'rt'))
except FileNotFoundError:
    r_data = safe_load(open(f'{getcwd()}/data/Race.yml', 'rt'))
    a_data = safe_load(open(f'{getcwd()}/data/Abilities.yml', 'rt'))

class Pillars_Race:
    def __init__(self, name, race_data = None, attribute_bonus = None):
        self.name = name
        if attribute_bonus is None:
            self.attribute_bonus = race_data['attribute_bonus']
        else:
            self.attribute_bonus = attribute_bonus

    def __repr__(self):
        return self.name

class Pillars_Subrace(Pillars_Race):
    def __init__(self, subrace, ability, parent_race: Pillars_Race):
        super().__init__(parent_race.name, attribute_bonus=parent_race.attribute_bonus)
        self.ability = {ability[0]: ability[1]}
        self.subrace_name = subrace
        self.parent = parent_race

    def __repr__(self):
        return f"{self.subrace_name}"

# Core Races
PRace_Aumauna = Pillars_Race('Aumauna', r_data['Aumauna'])
PRace_Dwarf = Pillars_Race('Dwarf', r_data['Dwarf'])
PRace_Elf = Pillars_Race('Elf', r_data['Elf'])
PRace_Godlike = Pillars_Race('Godlike', r_data['Godlike'])
PRace_Human = Pillars_Race('Human', r_data['Human'])
PRace_Orlan = Pillars_Race('Orlan', r_data['Orlan'])

# Aumauna Sub-Races
PSubRace_AumaunaCoastal = Pillars_Subrace('Coastal Aumauna', ('Towering Physique', a_data['Towering Physique']), PRace_Aumauna)
PSubRace_AumaunaIsland = Pillars_Subrace('Island Aumauna', ('Armed to the Teeth', a_data['Armed to the Teeth']), PRace_Aumauna)
# Dwarf Sub-Races
PSubRace_DwarfBoreal = Pillars_Subrace('Boreal Dwarf', ("Hunter's Instinct", a_data["Hunter's Instinct"]), PRace_Dwarf)
PSubRace_DwarfMountain = Pillars_Subrace('Mountain Dwarf', ("Hale and Hardy", a_data["Hale and Hardy"]), PRace_Dwarf)
# Elf Sub-Races
PSubRace_ElfPale = Pillars_Subrace('Pale Elf', ('Elemental Endurance', a_data['Elemental Endurance']), PRace_Elf)
PSubRace_ElfWood = Pillars_Subrace('Wood Elf', ('Distant Advantage', a_data['Distant Advantage']), PRace_Elf)
# Godlike Sub-Races
PSubRace_GodlikeDeath = Pillars_Subrace('Death Godlike', ("Death's Usher", a_data["Death's Usher"]), PRace_Godlike)
PSubRace_GodlikeFire = Pillars_Subrace('Fire Godlike', ("Battle-Forged", a_data["Battle-Forged"]), PRace_Godlike)
PSubRace_GodlikeNature = Pillars_Subrace('Nature Godlike', ("Wellspring of Life", a_data["Wellspring of Life"]), PRace_Godlike)
PSubRace_GodlikeMoon = Pillars_Subrace('Moon Godlike', ("Silver Tide", a_data["Silver Tide"]), PRace_Godlike)
# Human Sub-Races
PSubRace_HumanMeadow = Pillars_Subrace('Meadow Folk', ('Fighting Spirit', a_data['Fighting Spirit']), PRace_Human)
PSubRace_HumanOcean = Pillars_Subrace('Ocean Folk', ('Fighting Spirit', a_data['Fighting Spirit']), PRace_Human)
PSubRace_HumanSavannah = Pillars_Subrace('Savannah Folk', ('Fighting Spirit', a_data['Fighting Spirit']), PRace_Human)
# Orlan Sub-Races
PSubRace_OrlanHearth = Pillars_Subrace('Hearth Orlan', ("Minor Threat", a_data["Minor Threat"]), PRace_Orlan)
PSubRace_OrlanWild = Pillars_Subrace('Wild Orlan', ("Defiant Resolve", a_data["Defiant Resolve"]), PRace_Orlan)

RACES = [PRace_Aumauna, PRace_Dwarf, PRace_Elf, PRace_Godlike, PRace_Human, PRace_Orlan]
SUBRACES = {
    'Aumauna': [PSubRace_AumaunaIsland, PSubRace_AumaunaCoastal],
    'Dwarf': [PSubRace_DwarfBoreal, PSubRace_DwarfMountain],
    'Elf': [PSubRace_ElfWood, PSubRace_ElfPale],
    'Godlike': [PSubRace_GodlikeMoon, PSubRace_GodlikeNature, PSubRace_GodlikeFire, PSubRace_GodlikeDeath],
    'Human': [PSubRace_HumanSavannah, PSubRace_HumanOcean, PSubRace_HumanMeadow],
    'Orlan': [PSubRace_OrlanWild, PSubRace_OrlanHearth]
}
ALL_SUBRACES = [PSubRace_AumaunaCoastal, PSubRace_AumaunaIsland, PSubRace_DwarfBoreal, PSubRace_DwarfMountain,
                PSubRace_ElfPale, PSubRace_ElfWood, PSubRace_GodlikeDeath, PSubRace_GodlikeFire, PSubRace_GodlikeMoon,
                PSubRace_GodlikeNature, PSubRace_HumanMeadow, PSubRace_HumanOcean, PSubRace_HumanSavannah,
                PSubRace_OrlanHearth, PSubRace_OrlanWild]
