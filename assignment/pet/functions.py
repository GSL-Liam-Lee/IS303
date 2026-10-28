class pet:
    def __init__(self, pet_name, pet_type, hunger=0, happiness=100, bond=100):
        self.name = pet_name
        self.type = pet_type
        self.hunger = hunger
        self.happiness = happiness
        self.bond = bond
        
    max_hunger = 100
    max_happiness = 100
    max_bond = 100