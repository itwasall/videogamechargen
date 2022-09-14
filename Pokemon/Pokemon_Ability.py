#!/usr/bin/env python
# -*- coding: utf-8 -*-

LEVELING_RATES = ["Erratic", "Fast", "Medium Fast", "Medium Slow", "Slow", "Fluctuating"]
NATURES = [["Hardy", "Lonely", "Brave", "Adamant", "Naughty"],
           ["Bold", "Docile", "Relaxed", "Impish", "Lax"], 
           ["Timid", "Hasty", "Serious", "Jolly", "Naive"],
           ["Modest", "Mild", "Quiet", "Bashful", "Rash"],
           ["Calm", "Gentle", "Sassy", "Careful", "Quirky"]]
# Nature Stat Pattern. Fuck you, you come up with a better name
NSP = ["Attack", "Defense", "Speed", "Special Attack", "Special Defence"]


class LevelingRate:
    def __init__(self, rate):
        self.rate = rate

LvlRateErratic, LvlRateFast, LvlRateMedF, LvlRateMedS, LvlRateSlow, LvlRateFluc = [LevelingRate(i) for i in LEVELING_RATES]


class Nature:
    def __init__(self, name, bonus_stat, nerf_stat):
        self.name = name
        self.bonus_stat = bonus_stat
        self.nerf_stat = nerf_stat

NatHardy, NatLonely, NatBrave, NatAdamant, NatNaughty = [Nature(i, "Attack", NPS[it]) for it, i in LEVELING_RATES[0]]
NatBold, NatDocile, NatRelaxed, NatImpish, NatLax = [Nature(i, "Defense", NPS[it]) for it, i in LEVELING_RATES[1]]
NatTimid, NatHasty, NatSerious, NatJolly, NatNaive = [Nature(i, "Speed", NPS[it]) for it, i in LEVELING_RATES[2]]
NatModest, NatMild, NatQuiet, NatBashful, NatRash = [Nature(i, "Special Attack", NPS[it]) for it, i in LEVELING_RATES[3]]
NatCalm, NatGentle, NatSassy, NatCareful, NatQuirky = [Nature(i, "Special Defense", NPS[it]) for it, i in LEVELING_RATES[4]]


