#!/usr/bin/env python
# -*- coding: utf-8 -*-

from yaml import safe_load

import Pokemon_Nature as Nat

pkmn = safe_load(open('Pokemon/dex_all.yml'))

bub = pkmn[1]

bub_base = bub['baseStats']

print({i:bub_base[i] for i in bub_base.keys()})

def other_stat_growth(base, iv, ev, level, nature):
    a = ((2*base)+iv+(ev/4))*level
    b = round(a/100)+5
    c = round(b*nature)
    return c

print(other_stat_growth(bub_base['atk'], 31, 252, 100, 1.1))

