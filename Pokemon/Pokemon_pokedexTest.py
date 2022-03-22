#!/usr/bin/env python
# -*- coding: utf-8 -*-

from yaml import safe_load
from random import choice

data_dex = safe_load(open('Pokemon/pokedex.yml', 'rt'))

dex_no_special = {}
dex_all = {}
dex_all_compressed = {}
for idx, dex_entry_name in enumerate(data_dex):
    dex_entry = data_dex[dex_entry_name]
    dex_all[idx] = dex_entry
    if dex_entry["num"] in dex_no_special:
        continue
    else:
        dex_no_special[dex_entry["num"]] = dex_entry 
    if dex_entry["num"] in dex_all_compressed:
        entries = len(dex_all_compressed[dex_entry["num"]])
        dex_all_compressed[dex_entry["num"]][entries + 1] = dex_entry
    else:
        dex_all_compressed[dex_entry["num"]] = {}
        dex_all_compressed[dex_entry["num"]][0] = dex_entry

def pick_monster(dex_list):
    match dex_list:
        case "no-special":
            return choice(dex_no_special)
        case "all":
            return choice(dex_all)
        case "all-compressed":
            pkmn_all_compressed = choice(dex_all_compressed)
            if len(pkmn_all_compressed) <= 1:
                return dex_all_compressed[pkmn_all_compressed["num"]][0]
            else:
                return dex_all_compressed[pkmn_all_compressed["num"]][choice(len(pkmn_all_compressed))]
        case _:
            raise ValueError

def demo_pick_monster():
    monster_no_special = pick_monster("no-special")
    monster_all = pick_monster("all")
    # monster_all_compressed = pick_monster("all-compressed")
    monster_all_compressed = None
    return monster_no_special, monster_all, monster_all_compressed

for i in range(10):
    print("\nnewrun")
    a, b, c = demo_pick_monster()
    print(a["name"])
    print(b["name"])
    # print(c["name"])


