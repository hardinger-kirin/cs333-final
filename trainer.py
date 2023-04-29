class Trainer():
    def __init__(self, name):
        self.name = name
        self.team = None # initially no team
        self.ace = None # initially no ace Pokémon

    def get_name(self):
        return self.name
    
    def set_team(self, team):
        self.team = team
    
    def get_team(self):
        return self.team
    
    def replace_ace(self):
        # remove original ace from team
        self.team.remove(self.ace)

        if(len(self.team) == 0):
            self.ace = None
            return False
            
        # set new ace as next Pokémon in team
        self.ace = self.team[0]
        return True
    
    def get_team_size(self):
        return len(self.team)
    
    def list_team(self):
        for pokemon in self.team:
            print(f'\'{pokemon.get_nickname()}\' ({pokemon.get_name()}), ', end="")
    
    def find_pokemon_by_name(self, name):
        for i in range(len(self.team)):
            if(str(self.team[i].get_name()) == str(name)):
                return self.team[i]
        
        return None
    
    def get_ace(self):
        return self.ace
    
    def set_ace(self, Pokemon):
        if Pokemon in self.team:
            self.ace = Pokemon
            return True
        else:
            return False
