from yaml import safe_load
from os import getcwd

try:
    cu_bg_data = safe_load(open('PillarsOfEternity/data/CultureBackground.yml', 'rt'))
except FileNotFoundError:
    cu_bg_data = safe_load(open(f'{getcwd()}/data/CultureBackground.yml', 'rt'))

cu_data = cu_bg_data['culture']
bg_data = cu_bg_data['background']

class Pillars_Culture:
    def __init__(self, name, data):
        self.name = name
        self.attribute_bonus = data['attribute_bonus']

    def __repr__(self):
        return self.name

class Pillars_Background:
    def __init__(self, name, data):
        self.name = name
        self.skill_bonus = data['skill_bonus']
        self.requirements = data['required_backgrounds']
        self.reqs_fulfilled = False

    def check_requirements(self, cul: Pillars_Culture):
        if cul.name in self.requirements:
            self.reqs_fulfilled = True

    def __repr__(self):
        return self.name

# Cultures
PCulture_Aedyr = Pillars_Culture('Aedyr', cu_data['Aedyr'])
PCulture_DeadfireArchipelago = Pillars_Culture('Deadfire Archipelago', cu_data['Deadfire Archipelago'])
PCulture_IxamitlPlains = Pillars_Culture('Ixamitl Plains', cu_data['Ixamitl Plains'])
PCulture_OldVailia = Pillars_Culture('Old Vailia', cu_data['Old Vailia'])
PCulture_Rauatai = Pillars_Culture('Rauatai', cu_data['Rauatai'])
PCulture_TheLivingLands = Pillars_Culture('The Living Lands', cu_data['The Living Lands'])
PCulture_TheWhiteThatWends = Pillars_Culture('The White that Wends', cu_data['The White that Wends'])

# Backgrounds
PBackground_Aristocrat = Pillars_Background('Aristocrat', bg_data['Aristocrat'])
PBackground_Artist = Pillars_Background('Artist', bg_data['Artist'])
PBackground_Clergy = Pillars_Background('Clergy', bg_data['Clergy'])
PBackground_Colonist = Pillars_Background('Colonist', bg_data['Colonist'])
PBackground_Dissident = Pillars_Background('Dissident', bg_data['Dissident'])
PBackground_Drifter = Pillars_Background('Drifter', bg_data['Drifter'])
PBackground_Explorer = Pillars_Background('Explorer', bg_data['Explorer'])
PBackground_Hunter = Pillars_Background('Hunter', bg_data['Hunter'])
PBackground_Laborer = Pillars_Background('Laborer', bg_data['Laborer'])
PBackground_Mercenary = Pillars_Background('Mercenary', bg_data['Mercenary'])
PBackground_Merchant = Pillars_Background('Merchant', bg_data['Merchant'])
PBackground_Mystic = Pillars_Background('Mystic', bg_data['Mystic'])
PBackground_Philosopher = Pillars_Background('Philosopher', bg_data['Philosopher'])
PBackground_Raider = Pillars_Background('Raider', bg_data['Raider'])
PBackground_Scholar = Pillars_Background('Scholar', bg_data['Scholar'])
PBackground_Scientist = Pillars_Background('Scientist', bg_data['Scientist'])
PBackground_Slave = Pillars_Background('Slave', bg_data['Slave'])

CULTURES = [PCulture_Aedyr, PCulture_DeadfireArchipelago, PCulture_IxamitlPlains, PCulture_OldVailia, PCulture_Rauatai,
            PCulture_TheLivingLands, PCulture_TheWhiteThatWends]
BACKGROUNDS = [PBackground_Aristocrat, PBackground_Artist, PBackground_Clergy, PBackground_Colonist, PBackground_Dissident,
               PBackground_Drifter, PBackground_Explorer, PBackground_Hunter, PBackground_Laborer, PBackground_Mercenary,
               PBackground_Merchant, PBackground_Mystic, PBackground_Philosopher, PBackground_Raider, PBackground_Scholar,
               PBackground_Scientist, PBackground_Slave]
