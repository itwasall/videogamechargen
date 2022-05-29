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
    """
    'gifted' refers to the IV distribution of a Pokemon.
    If 0, then IV's are randomly assigned
    If 1, then IV's are all 31
    If 2, then a roll is made to see if the IV for Sp. Atk is 31,
        if the roll is True then Atk's IV will be 0, the rest 31,
        otherwise all IV's are 31, the same result as gifted = 1.
      This is done to minimise confusion damage taken from Pokemon that only
        uses special attacks. Since their Atk stat isn't being used for combat,
        it is therefore ideal to have ATK be as low as possible, as damage taken
        due to confusion is always calculated off ATK.
    """
    match gifted:
        case 0:
            for k in p.iv.keys():
                p.iv[k] = randint(1, 31)
        case 1:
            for k in p.iv.keys():
                p.iv[k] = 31
        case 2:
            spk_atk_boost = randint(0, 1)
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
    A pokemon's total EVs max out at 510, and a single stat maxes out at 252.
        This allows for two stats to be fully maxed out, with 6 left over to
        put into a teriary stat.
    When the 'smart' argument is 'True', only one of the two attacking stats
        will be chosen, should either be randomly selected first.
        If 'Atk' is rolled first, then 'Sp. Atk' won't be chosen, and visa versa.
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
