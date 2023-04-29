import pokemon
import trainer

def check_faint(pokemon):
    if pokemon.get_hp() <= 0:
        return True
    else:
        return False