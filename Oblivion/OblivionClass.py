from yaml import safe_load

class_data = safe_load(open('Oblivion/data/Classes.yml', 'rt'))

class Oblivion_Class:
    def __init__(self, name, data):
        self.name = name
        self.specialisation = data['specialisation']
        self.attributes = data['attributes']
        self.skills = data['skills']

    def __repr__(self):
        return self.name

OblClass_Acrobat = Oblivion_Class('Acrobat', class_data['Acrobat'])
OblClass_Agent = Oblivion_Class('Agent', class_data['Agent'])
OblClass_Archer = Oblivion_Class('Archer', class_data['Archer'])
OblClass_Assassin = Oblivion_Class('Assassin', class_data['Assassin'])
OblClass_Barbarian = Oblivion_Class('Barbarian', class_data['Barbarian'])
OblClass_Bard = Oblivion_Class('Bard', class_data['Bard'])
OblClass_Battlemage = Oblivion_Class('Battlemage', class_data['Battlemage'])
OblClass_Crusader = Oblivion_Class('Crusader', class_data['Crusader'])
OblClass_Healer = Oblivion_Class('Healer', class_data['Healer'])
OblClass_Knight = Oblivion_Class('Knight', class_data['Knight'])
OblClass_Mage = Oblivion_Class('Mage', class_data['Mage'])
OblClass_Monk = Oblivion_Class('Monk', class_data['Monk'])
OblClass_Nightblade = Oblivion_Class('Nightblade', class_data['Nightblade'])
OblClass_Pilgrim = Oblivion_Class('Pilgrim', class_data['Pilgrim'])
OblClass_Rogue = Oblivion_Class('Rogue', class_data['Rogue'])
OblClass_Scout = Oblivion_Class('Scout', class_data['Scout'])
OblClass_Sorcerer = Oblivion_Class('Sorcerer', class_data['Sorcerer'])
OblClass_Spellsword = Oblivion_Class('Spellsword', class_data['Spellsword'])
OblClass_Thief = Oblivion_Class('Thief', class_data['Thief'])
OblClass_Warrior = Oblivion_Class('Warrior', class_data['Warrior'])
OblClass_Witchhunter = Oblivion_Class('Witchhunter', class_data['Witchhunter'])

OBL_CLASSES = [OblClass_Acrobat, OblClass_Agent, OblClass_Archer, OblClass_Assassin, OblClass_Barbarian, OblClass_Bard,
              OblClass_Battlemage, OblClass_Crusader, OblClass_Healer, OblClass_Knight, OblClass_Mage, OblClass_Monk,
              OblClass_Nightblade, OblClass_Pilgrim, OblClass_Rogue, OblClass_Scout, OblClass_Sorcerer, OblClass_Spellsword,
              OblClass_Thief, OblClass_Warrior, OblClass_Witchhunter]

