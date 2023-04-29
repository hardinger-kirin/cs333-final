import random

class Pokemon():
    def __init__(self, nickname, species, hp, moveset):
        # nickname is simply the species name unless the trainer wishes to rename :)
        self.nickname = species 
        self.species = species
        self.hp = hp
        self.moveset = moveset
    
    def get_name(self):
        return self.species
    
    def get_nickname(self):
        return self.nickname

    def set_nickname(self, nickname):
        self.nickname = nickname
    
    def get_moves(self):
        return self.moveset
    
    def display_moves(self):
        i = 0
        for move in self.moveset:
            print(f'[{i}]  \"{move.get_name()}\" for {move.get_damage()} damage and {move.get_accuracy()}% accuracy')
            i += 1
    
    def find_move_by_name(self, name):
        for i in range(len(self.moveset)):
            if(str(self.moveset[i].name) == str(name)):
                return self.moveset[i]
        return None
    
    def attack(self, target, move):
        # run accuracy check
        if random.randint(1, 100) > int(move.get_accuracy()):
            return 0
        else:
            target.set_hp(move.get_damage())
            return move.get_damage()
    
    def set_hp(self, damage):
        self.hp -= damage
    
    def get_hp(self):
        return self.hp