def check_faint(pokemon):
    if pokemon.get_hp() <= 0:
        return True
    else:
        return False

def check_attack(p1_ace, p2_ace, move):
    if p1_ace.attack(p2_ace, move) != 0:
        return True
    else:
        return False