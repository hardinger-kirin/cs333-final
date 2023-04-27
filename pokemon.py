class Pokemon():
    def __init__(self, nickname, species, hp, moveset):
        self.nickname = species # nickname is simply the species name unless the trainer wishes to rename :)
        self.species = species
        self.hp = hp
        self.moveset = moveset
    
    def get_name(self):
        return self.species
    
    def get_nickname(self):
        return self.nickname

    def set_nickname(self, nickname):
        self.nickname = nickname