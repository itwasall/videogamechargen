class Race:
    def __init__(self, race_name, race_data: dict):
        self.name = race_name
        self.male_attributes = race_data['Male']['Attributes']
        self.male_height = race_data['Male']['Height']
        self.male_weight = race_data['Male']['Weight']
        self.female_attributes = race_data['Female']['Attributes']
        self.female_height = race_data['Female']['Height']
        self.female_weight = race_data['Female']['Weight']
        self.skills = race_data['Skills']
        self.magicka_mult_bonus = race_data['Magicka Multiplier Bonus']
        self.resists = [race_data['Resists'][i] for i in race_data['Resists']] # Should catch the "no" clause in yml data

class Character:
    def __init__(
        self,
        name: str,
        race: str,
        gender: str,
        char_class: str,
    ):
        self.name = name
        self.race = race
        self.gender = gender
        self.char_class = char_class