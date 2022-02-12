class MW_Attribute:
    def __init__(self, name, value=0):
        self.name = name
        self.value = value

    def __add__(self, x):
        return MW_Attribute(self.name, self.value + x)

    def __iadd__(self, x):
        return self.__add__(x)

    def __repr__(self):
        return f"{self.name}: {self.value}"

MWAttribute_Strength = MW_Attribute('Strength')
MWAttribute_Intelligence = MW_Attribute('Intelligence')
MWAttribute_Willpower = MW_Attribute('Willpower')
MWAttribute_Agility = MW_Attribute('Agility')
MWAttribute_Speed = MW_Attribute('Speed')
MWAttribute_Endurance = MW_Attribute('Endurance')
MWAttribute_Personality = MW_Attribute('Personality')
MWAttribute_Luck = MW_Attribute('Luck')

MW_ATTRIBUTES = [MWAttribute_Strength, MWAttribute_Intelligence, MWAttribute_Willpower, MWAttribute_Agility, MWAttribute_Speed, MWAttribute_Endurance, MWAttribute_Personality, MWAttribute_Luck]
