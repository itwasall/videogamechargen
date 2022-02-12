class Oblivion_Attribute:
    def __init__(self, name, value=0):
        self.name = name
        self.value = value

    def __add__(self, x):
        return Oblivion_Attribute(self.name, self.value + x)

    def __iadd__(self, x):
        return self.__add__(x)

    def __repr__(self):
        return f"{self.name}: {self.value}"

OblAttribute_Strength = Oblivion_Attribute('Strength')
OblAttribute_Intelligence = Oblivion_Attribute('Intelligence')
OblAttribute_Willpower = Oblivion_Attribute('Willpower')
OblAttribute_Agility = Oblivion_Attribute('Agility')
OblAttribute_Speed = Oblivion_Attribute('Speed')
OblAttribute_Endurance = Oblivion_Attribute('Endurance')
OblAttribute_Personality = Oblivion_Attribute('Personality')
OblAttribute_Luck = Oblivion_Attribute('Luck')

MW_ATTRIBUTES = [OblAttribute_Strength, OblAttribute_Intelligence, OblAttribute_Willpower, OblAttribute_Agility, OblAttribute_Speed, OblAttribute_Endurance, OblAttribute_Personality, OblAttribute_Luck]
