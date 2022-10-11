from yaml import safe_load
from os import getcwd

try:
    class_data = safe_load(open('Morrowind/data/Classes.yml', 'rt'))
except FileNotFoundError:
    class_data = safe_load(open(f'{getcwd()}\\data\\Classes.yml', 'rt'))


class MW_Class:
    def __init__(self, name, class_data):
        self.name = name
        self.specialisation = class_data['spec']
        self.mw_attributes = class_data['attr']
        self.major_skills = class_data['major']
        self.minor_skills = class_data['minor']

    def __repr__(self):
        return self.name

MWClass_Acrobat = MW_Class('Acrobat', class_data['Acrobat'])
MWClass_Agent = MW_Class('Agent', class_data['Agent'])
MWClass_Archer = MW_Class('Archer', class_data['Archer'])
MWClass_Assassin = MW_Class('Assassin', class_data['Assassin'])
MWClass_Barbarian = MW_Class('Barbarian', class_data['Barbarian'])
MWClass_Bard = MW_Class('Bard', class_data['Bard'])
MWClass_Battlemage = MW_Class('Battlemage', class_data['Battlemage'])
MWClass_Crusader = MW_Class('Crusader', class_data['Crusader'])
MWClass_Healer = MW_Class('Healer', class_data['Healer'])
MWClass_Knight = MW_Class('Knight', class_data['Knight'])
MWClass_Mage = MW_Class('Mage', class_data['Mage'])
MWClass_Monk = MW_Class('Monk', class_data['Monk'])
MWClass_Nightblade = MW_Class('Nightblade', class_data['Nightblade'])
MWClass_Pilgrim = MW_Class('Pilgrim', class_data['Pilgrim'])
MWClass_Rogue = MW_Class('Rogue', class_data['Rogue'])
MWClass_Scout = MW_Class('Scout', class_data['Scout'])
MWClass_Sorcerer = MW_Class('Sorcerer', class_data['Sorcerer'])
MWClass_Spellsword = MW_Class('Spellsword', class_data['Spellsword'])
MWClass_Theif = MW_Class('Theif', class_data['Theif'])
MWClass_Warrior = MW_Class('Warrior', class_data['Warrior'])
MWClass_Witchhunter = MW_Class('Witchhunter', class_data['Witchhunter'])

MW_CLASSES = [
    MWClass_Acrobat,
    MWClass_Agent,
    MWClass_Archer,
    MWClass_Assassin,
    MWClass_Barbarian,
    MWClass_Bard,
    MWClass_Battlemage,
    MWClass_Crusader,
    MWClass_Healer,
    MWClass_Knight,
    MWClass_Mage,
    MWClass_Monk,
    MWClass_Nightblade,
    MWClass_Pilgrim,
    MWClass_Rogue,
    MWClass_Scout,
    MWClass_Sorcerer,
    MWClass_Spellsword,
    MWClass_Theif,
    MWClass_Warrior,
    MWClass_Witchhunter
]
