#!/usr/bin/env python
# -*- coding: utf-8 -*-

from yaml import safe_load

data_gmax = safe_load(open('Pokemon/dex_gmax.yml', 'rt'))
data_mega = safe_load(open('Pokemon/dex_mega.yml', 'rt'))

for idx, i in enumerate(data_gmax):
    print(idx, data_gmax[i])
    if idx >= 0:
        break

class Pokemon_Form:
    def __init__(
        self,
        num: int,
        name: str,
        baseSpecies: str,
        forme: str,
        types: list,
        genderRatio: dict = None,
        baseStats: dict = None,
        abilities: dict = None,
        heightm: int = None,
        weightkg: int = None,
        color: str  = None,
        eggGroups: list = None,
    ):
        self.num = num
        self.name = name
        self.baseSpecies = baseSpecies
        self.forme = forme
        self.types = types
        self.genderRatio = genderRatio
        self.baseStats = baseStats
        self.abilities = abilities
        self.heightm = heightm
        self.weightkg = weightkg
        self.color = color
        self.eggGroups = eggGroups

    def __repr__(self):
        return f"{self.name} - {self.num}"

class Mega_Evolution(Pokemon_Form):
    def __init__(
        self,
        num: int,
        name: str,
        baseSpecies: str,
        forme: str,
        types: list,
        genderRatio: dict = None,
        baseStats: dict = None,
        abilities: dict = None,
        heightm: int = None,
        weightkg: int = None,
        color: str  = None,
        eggGroups: list = None,
        requiredItem: str = None,
    ):
        super().__init__(self, num, name, baseSpecies, forme, types, genderRatio,
                         baseStats, abilities, heightm, weightkg, color, eggGroups)
        self.requiredItem = requiredItem

class Gmax_Pokemon(Pokemon_Form):
    def __init__(
        self,
        num: int,
        name: str,
        baseSpecies: str,
        forme: str,
        types: list,
        genderRatio: dict = None,
        baseStats: dict = None,
        abilities: dict = None,
        heightm: int = None,
        weightkg: int = None,
        color: str  = None,
        eggGroups: list = None,
        changesFrom: str = None,
    ):
        super().__init__(num, name, baseSpecies, forme, types, genderRatio,
                         baseStats, abilities, heightm, weightkg, color, eggGroups)
        self.changesFrom = changesFrom

gmax_pokemon = {}
mega_pokemon = {}

for k in data_gmax:
    p = data_gmax[k]
    if 'genderRatio' in p:
        gmax_pokemon[k] = Gmax_Pokemon(
            p['num'], p['name'], p['baseSpecies'], p['forme'], p['types'],
            p['genderRatio'], p['baseStats'], p['abilities'], p['heightm'], p['weightkg'], 
            p['color'], p['eggGroups'], p['changesFrom'])
    else:
        gmax_pokemon[k] = Gmax_Pokemon(
            p['num'], p['name'], p['baseSpecies'], p['forme'], p['types'],
            None, p['baseStats'], p['abilities'], p['heightm'], p['weightkg'], 
            p['color'], p['eggGroups'], p['changesFrom'])
    print(gmax_pokemon[k])

# for k in data_mega:
#     p = data_mega[k]
#     mega_pokemon[k] = Mega_Evolution(
#         p['num'], p['name'], p['baseSpecies'], p['forme'], p['types'],
#         p['genderRatio'], p['baseStats'], p['abilities'], p['heightm'], p['weightkg'], 
#         p['color'], p['eggGroups'], p['requiredItem'])
#     print(mega_pokemon[k])

print(f"len gmax_pokemon: {len(gmax_pokemon)}\nlen mega_pokemon: {len(mega_pokemon)}")
