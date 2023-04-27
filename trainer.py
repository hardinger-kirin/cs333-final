class Trainer():
    def __init__(self, name):
        self.name = name
        self.team = None # initially no team

    def get_name(self):
        return self.name
    
    def set_team(self, team):
        self.team = team
    
    def get_team(self):
        return self.team
    
    def list_team(self):
        for pokemon in self.team:
            print(f'\'{pokemon.get_nickname()}\' ({pokemon.get_name()}), ', end="")
    
    def find_pokemon_by_name(self, name):
        for i in range(len(self.team)):
            if(str(self.team[i].get_name()) == str(name)):
                return self.team[i]
        
        return None
