from dis import dis
from numpy import isin
from yaml import safe_load
import os

print(os.getcwd())

ab_data = safe_load(open('PillarsOfEternity/data/Abilities.yml', 'rt'))
ef_data = safe_load(open('PillarsOfEternity/data/EffectNames.yml', 'rt'))

class Pillars_ClassExtra:
    def __init__(self, name, effect=None):
        self.name = name
        if effect is not None:
            self.effect = self.get_effects(effect)
        else:
            self.effect = None

    def get_effects(self, effects):
        return_dict = {}
        for key in effects.keys():
            if key not in ["_conditional", "_effect"]:
                return_dict[ef_data[key]] = effects[key]
            elif key == "_effect":
                return_dict["_effect"] = {ef_data[k]: effects[key][k] for k in effects[key].keys()}
            elif key == "_conditional":
                if "_choice" in effects[key].keys():
                    return_dict["_conditional_choice"]= [i for i in effects[key]['_choice']]
                elif "_condition" in effects[key].keys():
                    return_dict["_conditional"] = effects[key]['_condition']
        return return_dict

class Pillars_ClassExtra_Spell(Pillars_ClassExtra):
    def __init__(self, name, area, effect, duration, desc, range = None, speed = None, condition = None):
        super().__init__(name, effect)
        self.name = name
        self.area = area
        self.duration = duration
        self.range = range
        self.speed = speed
        self.condition = condition
        self.description = desc

    def __repr__(self):
        return self.name


class Pillars_ChanterPhrase(Pillars_ClassExtra_Spell):
    def __init__(self, name, area, effect, duration, desc, linger):
        super().__init__(name, area, effect, duration , desc)
        self.linger = linger

class Pillars_ChanterInvocation(Pillars_ClassExtra_Spell):
    def __init__(self, name, area, effect, speed, duration, interrupt, range, desc):
        super().__init__(name, area, effect, duration, desc, range, speed)
        self.interrupt = interrupt

class Pillars_CipherSpells(Pillars_ClassExtra_Spell):
    def __init__(self, name, area, effect, focus_cost, speed, duration, range, desc):
        super().__init__(name, area, effect, duration, desc, range, speed)
        self.focus_cost = focus_cost

class Pillars_WizardSpells(Pillars_ClassExtra_Spell):
    def __init__(self, name, area, effect, duration, speed, range, condition = None):
        super().__init__(name, area, effect, duration, "", range, speed, condition)


class Pillars_DruidShapeshift(Pillars_ClassExtra):
    def __init__(self, name, form, damage_type, abilities, weapon, armour):
        super().__init__(name)
        self.form = form
        self.damage_type = damage_type
        self.abilities = [ab_data[i] for i in abilities]
        self.weapon = weapon
        self.armour = armour

    def __repr__(self):
        return f"{self.form}"


class Pillars_OrderDeity(Pillars_ClassExtra):
    def __init__(self, name, good_thing, bad_thing):
        super().__init__(name)
        self.good_thing = good_thing
        self.bad_thing = bad_thing

    def __repr__(self):
        return self.name

class Pillars_PriestDeity(Pillars_OrderDeity):
    def __init__(self, name, favoured_dispositions, condemed_dispositions, favoured_weapons, talent):
        super().__init__(name, favoured_dispositions, condemed_dispositions)
        self.favoured_weapon = favoured_weapons
        self.talent = talent

class Pillars_PaladinOrder(Pillars_OrderDeity):
    def __init__(self, name, favoured_behaviours, disfavoured_behaviours):
        super().__init__(name, favoured_behaviours, disfavoured_behaviours)


class Pillars_RangerAnimalCompanion(Pillars_ClassExtra):
    def __init__(self, name, stat_block, dr, abilities, effect=None):
        if effect is None or (isinstance(effect, bool) and not effect):
            super().__init__(name)
        else:
            super().__init__(name, effect)
        self.stat_block = stat_block
        self.damage_reduction = dr
        if isinstance(abilities, list):
            self.abilities = [ab_data[i] for i in abilities]

    def __repr__(self):
        return self.name