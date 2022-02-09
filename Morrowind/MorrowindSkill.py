class MW_Skill:
    def __init__(self, name, specialisation, mw_attribute):
        self.name = name
        self.specialisation = specialisation
        self.mw_attribute = mw_attribute

# Endurance Attribute Skills
c,s,m,x = 'Combat', 'Stealth', 'Magic', 'Endurance'
MWSkill_HeavyArmor = MW_Skill('Heavy Armour', c, x)
MWSkill_MediumArmor = MW_Skill('Medium Armour', c, x)
MWSkill_Spear = MW_Skill('Spear', c, x)

# Strength Attribute Skills
x = 'Strength'
MWSkill_Acrobatics = MW_Skill('Acrobatics', s, x)
MWSkill_Armorer = MW_Skill('Armorer', c, x)
MWSkill_Axe = MW_Skill('Axe', c, x)
MWSkill_BluntWeapon = MW_Skill('Blunt Weapon', c, x)
MWSkill_LongBlade = MW_Skill('Long Blade', c, x)

# Agility Attribute Skills
x = 'Agility'
MWSkill_Block = MW_Skill('Block', c, x)
MWSkill_LightArmor = MW_Skill('Light Armor', s, x)
MWSkill_Marksman = MW_Skill('Marksman', s, x)
MWSkill_Sneak = MW_Skill('Sneak', s, x)

# Speed Attribute Skills
x = 'Speed'
MWSkill_Athletics = MW_Skill('Athletics', c, x)
MWSkill_HandtoHand = MW_Skill('Hand to Hand', s, x)
MWSkill_ShortBlade = MW_Skill('Short Blade', s, x) 
MWSkill_Unarmored = MW_Skill('Unarmored', m, x)

# Personality Attribute Skills
x = 'Personality'
MWSkill_Illusion = MW_Skill('Illusion', m, x)
MWSkill_Mercantile = MW_Skill('Mercantile', s, x)
MWSkill_Speechcraft = MW_Skill('Speechcraft', s, x)

# Intelligence Attribute Skills
x = 'Intelligence'
MWSkill_Alchemy = MW_Skill('Alchemy', m, x)
MWSkill_Conjuration = MW_Skill('Conjuration', m, x)
MWSkill_Enchant = MW_Skill('Enchant', m, x)
MWSkill_Security = MW_Skill('Security', s, x)

# Willpower Attribute Skills
x = 'Willpower'
MWSkill_Alteration = MW_Skill('Alteration', m, x)
MWSkill_Destruction = MW_Skill('Destruction', m, x)
MWSkill_Mysticism = MW_Skill('Mysticism', m, x)
MWSkill_Restoration = MW_Skill('Restoration', m, x)

# Luck Attribute Skills
# AHAHAHAAHAHAH

MW_SKILLS = [MWSkill_HeavyArmor, MWSkill_MediumArmor, MWSkill_Spear, MWSkill_Acrobatics, MWSkill_Armorer, MWSkill_Axe, MWSkill_BluntWeapon, MWSkill_LongBlade, MWSkill_Block, MWSkill_LightArmor,
             MWSkill_Marksman, MWSkill_Sneak, MWSkill_Athletics, MWSkill_HandtoHand, MWSkill_ShortBlade, MWSkill_Unarmored, MWSkill_Illusion, MWSkill_Mercantile, MWSkill_Speechcraft,
             MWSkill_Alchemy, MWSkill_Conjuration, MWSkill_Enchant, MWSkill_Security, MWSkill_Alteration, MWSkill_Destruction, MWSkill_Mysticism, MWSkill_Restoration]
