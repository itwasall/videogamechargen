#!/usr/bin/env python
# -*- coding: utf-8 -*-

from yaml import safe_load
from random import choice
from time import perf_counter

script_start = perf_counter()

data_dex = safe_load(open('Pokemon/pokedex.yml', 'rt'))

dex_no_special = {}
dex_all = {}
dex_all_compressed = {}
for idx, dex_entry_name in enumerate(data_dex):
    dex_entry = data_dex[dex_entry_name]
    dex_all[idx] = dex_entry
    if dex_entry["num"] in dex_all_compressed:
        entries = len(dex_all_compressed[dex_entry["num"]])
        dex_all_compressed[dex_entry["num"]][dex_entry["name"].split("-")[1]] = dex_entry
    else:
        dex_all_compressed[dex_entry["num"]] = {}
        dex_all_compressed[dex_entry["num"]][dex_entry["name"]] = dex_entry
    if dex_entry["num"] in dex_no_special:
        continue
    else:
        dex_no_special[dex_entry["num"]] = dex_entry 

def pick_dex(dex_list):
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

def demo_pick_dex():
    dex_no_special = pick_dex("no-special")
    dex_all = pick_dex("all")
    # dex_all_compressed = pick_dex("all-compressed")
    dex_all_compressed = None
    return dex_no_special, dex_all, dex_all_compressed

dex_just_special = {}
dex_no_special_names = [dex_no_special[mon]['name'] for mon in dex_no_special]
for dex_key in dex_all:
    if dex_all[dex_key]['name'] not in dex_no_special_names:
        dex_just_special[dex_key] = dex_all[dex_key]
    else:
        continue

print(len(dex_just_special))

files = {"Pokemon/dex_all.yml": dex_all,
         "Pokemon/dex_no_special.yml": dex_no_special,
         "Pokemon/dex_just_special.yml": dex_just_special,
         "Pokemon/dex_all_compressed.yml": dex_all_compressed,
         "Pokemon/dex_gmax.yml": {k:d for k, d in dex_just_special.items() if dex_just_special[k]['name'].endswith('-Gmax')},
         "Pokemon/dex_mega.yml": {k:d for k, d in dex_just_special.items() if dex_just_special[k]['name'].endswith('-Mega')},
         }

for filename in files:
    with open(filename, "w+") as output:
        data_to_output = files[filename]
        print(f"writing {filename}")
        for k, d in data_to_output.items():
            output.write(f"{k+1}: {data_to_output[k]}\n")

script_end = perf_counter()

print(f"exec time: {script_end - script_start:0.2f}")

