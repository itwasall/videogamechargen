#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint, choice
from yaml import safe_load
from sys import getsizeof

POKEMON = safe_load(open('Pokemon/pokedex.yml', 'rt'))

# print(getsizeof(POKEMON))
class Pkmn:
    def __init__(self, name):
        self.name = name
        self.iv = {'HP': 0, 'Atk': 0, 'Sp. Atk': 0, 'Def': 0, 'Sp. Def': 0, 'Spd': 0}
        self.ev = {'HP': 0, 'Atk': 0, 'Sp. Atk': 0, 'Def': 0, 'Sp. Def': 0, 'Spd': 0}
        self.base_stats = {'HP': 0, 'Atk': 0, 'Sp. Atk': 0, 'Def': 0, 'Sp. Def': 0, 'Spd': 0}
        self.base_stats_sum = sum(self.base_stats.values())
        self.level = 1
        self.type = [None, None]

    def __repr__(self):
        return self.name

    def pkmn_info(self):
        print(self.iv)
        print(self.ev)

def gen_iv(p: Pkmn, gifted = 0):
    match gifted:
        case 0:
            for k in p.iv.keys():
                p.iv[k] = randint(1, 31)
        case 1:
            # A "gifted" argument value of 1 makes all of a pokemons IVs equal to 31
            for k in p.iv.keys():
                p.iv[k] = 31
        case 2:
            spk_atk_boost = randint(0, 1)
            # A "gifted" argument value of 2 does the same as 1, however if spk_atk_boost is 1,
            #   then the IV of 'Atk' will be set to 0. This is beneficial in some competitive
            #   scenarios as damaged inflicted via confusion is calculated using the 'Atk' stat,
            #   so a pokemon specialising in 'Sp. Atk' moves would ideally want to keep 'Atk' as 
            #   low as possible, as otherwise the 'Atk' isn't used.
            if spk_atk_boost:
                for k in p.iv.keys():
                    if k != 'Atk':
                        p.iv[k] = 31
                p.iv['Atk'] = 0
            else:
                for k in p.iv.keys():
                    p.iv[k] = 31




def gen_ev(p: Pkmn, min_max = True, smart = True):
    """
    Following gen 8 logic, it is possible to max a pokemons EVs at level one.
    This is done through a combination of vitamins + EV boosting poke jobs. As
        these EV-boosting poke jobs reward EVs in place of Exp, it's possible,
        through technically grueling, for a pokemon to achieve max EVs before
        attaining level 2
    """
    if not min_max:
        total_evs = randint(0, 510) # Max number of evs possible
    else:
        total_evs = 510
    stats = ['HP', 'Atk', 'Sp. Atk', 'Def', 'Sp. Def', 'Spd']
    used_stats = []
    while total_evs > 0 and len(stats):
        if min_max:
            if total_evs >= 252:
                # EVs max out at 252, with 510 available for a singular pokemon
                total_evs -= 252
                stat_to_boost = choice(stats)
                stats.pop(stats.index(stat_to_boost))
                p.ev[stat_to_boost] += 252
                # Typically one would only max out one of the two attack evs when
                #   ev-training a pokemon
                if smart:
                    if stat_to_boost == 'Atk':
                        stats.pop(stats.index('Sp. Atk'))
                    if stat_to_boost == 'Sp. Atk':
                        stats.pop(stats.index('Atk'))
            else:
                total_evs -= 6
                stat_to_boost = choice(stats)
                stats.pop(stats.index(stat_to_boost))
                p.ev[stat_to_boost] += 6
        else:
            print("fuck if I know")

P = Pkmn('test')
gen_iv(P, 2)
gen_ev(P, True)
P.pkmn_info()
