class Move():
    def __init__(self, name, damage, accuracy):
        self.name = name
        self.damage = damage
        self.accuracy = accuracy
    
    def get_name(self):
        return self.name
    
    def get_damage(self):
        return self.damage
    
    def get_accuracy(self):
        return self.accuracy