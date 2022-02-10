from yaml import safe_load

bs_data = safe_load(open('Morrowind/data/Birthsigns.yml', 'rt'))

def birthsign_param_resolver(birth):
    effects = {}
    for key in birth.keys():
        if key == 'spell':
            effects['spell'] = birth[key]
        elif key == 'power':
            effects['power'] = birth[key]
        else:
            effects[key] = birth[key]
    return effects

class MW_Birthsign:
    def __init__(self, name, data):
        self.name = name
        self.effect = birthsign_param_resolver(data)

MWBirthsign_Warrior = MW_Birthsign('Warrior', bs_data['Warrior'])
MWBirthsign_Mage = MW_Birthsign('Mage', bs_data['Mage'])
MWBirthsign_Thief = MW_Birthsign('Thief', bs_data['Thief'])
MWBirthsign_Serpant = MW_Birthsign('Serpant', bs_data['Serpant'])
MWBirthsign_Lady = MW_Birthsign('Lady', bs_data['Lady'])
MWBirthsign_Steed = MW_Birthsign('Steed', bs_data['Steed'])
MWBirthsign_Lord = MW_Birthsign('Lord', bs_data['Lord'])
MWBirthsign_Apprentice = MW_Birthsign('Apprentice', bs_data['Apprentice'])
MWBirthsign_Atronach = MW_Birthsign('Atronach', bs_data['Atronach'])
MWBirthsign_Ritual = MW_Birthsign('Ritual', bs_data['Ritual'])
MWBirthsign_Lover = MW_Birthsign('Lover', bs_data['Lover'])
MWBirthsign_Shadow = MW_Birthsign('Shadow', bs_data['Shadow'])
MWBirthsign_Tower = MW_Birthsign('Tower', bs_data['Tower'])

MW_BIRTHSIGNS = [MWBirthsign_Warrior, MWBirthsign_Mage, MWBirthsign_Thief, MWBirthsign_Serpant, MWBirthsign_Lady, MWBirthsign_Steed, MWBirthsign_Lord,
                 MWBirthsign_Apprentice, MWBirthsign_Atronach, MWBirthsign_Ritual, MWBirthsign_Lover, MWBirthsign_Shadow, MWBirthsign_Tower]
