import trainer
import pokemon
import move
import battle_helper

# This test suite has 6 integration tests and 19 unit tests.

import unittest
class TestMethods(unittest.TestCase):
    #UNIT TESTS FOR TRAINER CLASS *************************
    def test_get_trainer_name(self):
        test_name = "Ash"
        test_trainer = trainer.Trainer(test_name)
        self.assertEqual(test_trainer.get_name(), test_name)
    
    def test_get_trainer_team(self):
        test_trainer = trainer.Trainer("Ash")
        test_team = [    
        pokemon.Pokemon("","Charmander",39, \
            [move.Move("Scratch", 4, 100), move.Move("Dragon Breath", 6, 92), \
            move.Move("Fire Fang", 6.5, 90)]),
        pokemon.Pokemon("","Scorbunny", 50, \
            [move.Move("Tackle", 4, 100), move.Move("Flame Charge", 5, 95), \
            move.Move("Bounce", 8.5, 80)]),
        pokemon.Pokemon("","Litten", 45, \
            [move.Move("Ember", 4, 100), move.Move("Bite", 6, 91), \
            move.Move("Flamethrower", 9, 75)])
        ]
        test_trainer.set_team(test_team)
        self.assertEqual(test_trainer.get_team(), test_team)
    
    def test_set_ace_valid(self):
        test_trainer = trainer.Trainer("Ash")
        test_team = [    
        pokemon.Pokemon("","Charmander",39, \
            [move.Move("Scratch", 4, 100), move.Move("Dragon Breath", 6, 92), \
            move.Move("Fire Fang", 6.5, 90)]),
        pokemon.Pokemon("","Scorbunny", 50, \
            [move.Move("Tackle", 4, 100), move.Move("Flame Charge", 5, 95), \
            move.Move("Bounce", 8.5, 80)]),
        pokemon.Pokemon("","Litten", 45, \
            [move.Move("Ember", 4, 100), move.Move("Bite", 6, 91), \
            move.Move("Flamethrower", 9, 75)])
        ]
        test_trainer.set_team(test_team)
        self.assertTrue(test_trainer.set_ace(test_team[0]))
    
    def test_set_ace_invalid(self):
        test_trainer = trainer.Trainer("Ash")
        test_team = [    
        pokemon.Pokemon("","Charmander",39, \
            [move.Move("Scratch", 4, 100), move.Move("Dragon Breath", 6, 92), \
            move.Move("Fire Fang", 6.5, 90)]),
        pokemon.Pokemon("","Scorbunny", 50, \
            [move.Move("Tackle", 4, 100), move.Move("Flame Charge", 5, 95), \
            move.Move("Bounce", 8.5, 80)]),
        pokemon.Pokemon("","Litten", 45, \
            [move.Move("Ember", 4, 100), move.Move("Bite", 6, 91), \
            move.Move("Flamethrower", 9, 75)])
        ]
        test_trainer.set_team(test_team)
        test_pokemon = pokemon.Pokemon("","Bulbasaur", 45, \
            [move.Move("Vine Whip", 4.5, 100), move.Move("Razor Leaf", 5.5, 93), move.Move("Seed Bomb", 8, 85)])
        self.assertFalse(test_trainer.set_ace(test_pokemon))
    
    def test_get_ace(self):
        test_trainer = trainer.Trainer("Ash")
        test_team = [    
        pokemon.Pokemon("","Charmander",39, \
            [move.Move("Scratch", 4, 100), move.Move("Dragon Breath", 6, 92), \
            move.Move("Fire Fang", 6.5, 90)]),
        pokemon.Pokemon("","Scorbunny", 50, \
            [move.Move("Tackle", 4, 100), move.Move("Flame Charge", 5, 95), \
            move.Move("Bounce", 8.5, 80)]),
        pokemon.Pokemon("","Litten", 45, \
            [move.Move("Ember", 4, 100), move.Move("Bite", 6, 91), \
            move.Move("Flamethrower", 9, 75)])
        ]
        test_trainer.set_team(test_team)
        test_trainer.set_ace(test_team[0])
        self.assertEqual(test_trainer.get_ace(), test_team[0])
    
    def test_replace_ace_true(self):
        test_trainer = trainer.Trainer("Ash")
        test_team = [    
        pokemon.Pokemon("","Charmander",39, \
            [move.Move("Scratch", 4, 100), move.Move("Dragon Breath", 6, 92), \
            move.Move("Fire Fang", 6.5, 90)]),
        pokemon.Pokemon("","Scorbunny", 50, \
            [move.Move("Tackle", 4, 100), move.Move("Flame Charge", 5, 95), \
            move.Move("Bounce", 8.5, 80)]),
        pokemon.Pokemon("","Litten", 45, \
            [move.Move("Ember", 4, 100), move.Move("Bite", 6, 91), \
            move.Move("Flamethrower", 9, 75)])
        ]
        test_trainer.set_team(test_team)
        test_trainer.set_ace(test_team[0])
        self.assertTrue(test_trainer.replace_ace())
    
    def test_replace_ace_false(self):
        test_trainer = trainer.Trainer("Ash")
        test_team = [    
        pokemon.Pokemon("","Charmander",39, \
            [move.Move("Scratch", 4, 100), move.Move("Dragon Breath", 6, 92), \
            move.Move("Fire Fang", 6.5, 90)])
        ]
        test_trainer.set_team(test_team)
        test_trainer.set_ace(test_team[0])
        self.assertFalse(test_trainer.replace_ace())
    
    def test_get_team_size(self):
        test_trainer = trainer.Trainer("Ash")
        test_team = [    
        pokemon.Pokemon("","Charmander",39, \
            [move.Move("Scratch", 4, 100), move.Move("Dragon Breath", 6, 92), \
            move.Move("Fire Fang", 6.5, 90)]),
        pokemon.Pokemon("","Scorbunny", 50, \
            [move.Move("Tackle", 4, 100), move.Move("Flame Charge", 5, 95), \
            move.Move("Bounce", 8.5, 80)]),
        pokemon.Pokemon("","Litten", 45, \
            [move.Move("Ember", 4, 100), move.Move("Bite", 6, 91), \
            move.Move("Flamethrower", 9, 75)])
        ]
        test_trainer.set_team(test_team)
        self.assertEqual(test_trainer.get_team_size(), 3)
    
    #UNIT TESTS FOR POKEMON CLASS ****************************
    def test_get_pokemon_name(self):
        test_pokemon = pokemon.Pokemon("", "Charmander", 39, [])
        self.assertEqual(test_pokemon.get_name(), "Charmander")

    def test_set_and_get_nickname(self):
        test_pokemon = pokemon.Pokemon("", "Charmander", 39, [])
        test_pokemon.set_nickname("Charrino")
        self.assertEqual(test_pokemon.get_nickname(), "Charrino")
    
    def test_set_hp(self):
        test_pokemon = pokemon.Pokemon("", "Charmander", 39, [])
        test_pokemon.set_hp(10)
        self.assertEqual(test_pokemon.hp, 29)
    
    def test_get_hp(self):
        test_pokemon = pokemon.Pokemon("", "Charmander", 39, [])
        self.assertEqual(test_pokemon.get_hp(), 39)

    #UNIT TESTS FOR MOVE CLASS ********************************
    def test_get_move_name(self):
        test_move = move.Move("Scratch", 4, 100)
        self.assertEqual(test_move.get_name(), "Scratch")
    
    def test_get_damage(self):
        test_move = move.Move("Scratch", 4, 100)
        self.assertEqual(test_move.get_damage(), 4)
    
    def test_get_accuracy(self):
        test_move = move.Move("Scratch", 4, 100)
        self.assertEqual(test_move.get_accuracy(), 100)
    
    #UNIT TESTS FOR BATTLE_HELPER CLASS ************************
    def test_check_faint_true(self):
        test_pokemon = pokemon.Pokemon("", "Charmander", 39, [])
        test_pokemon.set_hp(39)
        self.assertTrue(battle_helper.check_faint(test_pokemon))
    
    def test_check_faint_false(self):
        test_pokemon = pokemon.Pokemon("", "Charmander", 39, [])
        test_pokemon.set_hp(10)
        self.assertFalse(battle_helper.check_faint(test_pokemon))
    
    def test_check_attack_true(self):
        test_ace1 = pokemon.Pokemon("", "Charmander", 39, \
            [move.Move("Scratch", 4, 100)])
        test_ace2 = pokemon.Pokemon("", "Scorbunny", 50, [])
        self.assertTrue(battle_helper.check_attack(test_ace1, test_ace2, test_ace1.get_moves()[0]))
    
    def test_check_attack_false(self):
        test_ace1 = pokemon.Pokemon("", "Charmander", 39, \
            [move.Move("Scratch", 4, 0)])
        test_ace2 = pokemon.Pokemon("", "Scorbunny", 50, [])
        self.assertFalse(battle_helper.check_attack(test_ace1, test_ace2, test_ace1.get_moves()[0]))
    
    #INTEGRATION TESTS FOR TRAINER AND POKEMON CLASS***********
    def test_find_pokemon_by_name_valid(self):
        test_trainer = trainer.Trainer("Ash")
        test_team = [    
        pokemon.Pokemon("","Charmander",39, \
            [move.Move("Scratch", 4, 100), move.Move("Dragon Breath", 6, 92), \
            move.Move("Fire Fang", 6.5, 90)]),
        pokemon.Pokemon("","Scorbunny", 50, \
            [move.Move("Tackle", 4, 100), move.Move("Flame Charge", 5, 95), \
            move.Move("Bounce", 8.5, 80)]),
        pokemon.Pokemon("","Litten", 45, \
            [move.Move("Ember", 4, 100), move.Move("Bite", 6, 91), \
            move.Move("Flamethrower", 9, 75)])
        ]
        test_trainer.set_team(test_team)
        self.assertEqual(test_trainer.find_pokemon_by_name("Charmander"), test_team[0])
    
    def test_find_pokemon_by_name_invalid(self):
        test_trainer = trainer.Trainer("Ash")
        test_team = [    
        pokemon.Pokemon("","Charmander",39, \
            [move.Move("Scratch", 4, 100), move.Move("Dragon Breath", 6, 92), \
            move.Move("Fire Fang", 6.5, 90)]),
        pokemon.Pokemon("","Scorbunny", 50, \
            [move.Move("Tackle", 4, 100), move.Move("Flame Charge", 5, 95), \
            move.Move("Bounce", 8.5, 80)]),
        pokemon.Pokemon("","Litten", 45, \
            [move.Move("Ember", 4, 100), move.Move("Bite", 6, 91), \
            move.Move("Flamethrower", 9, 75)])
        ]
        test_trainer.set_team(test_team)
        self.assertEqual(test_trainer.find_pokemon_by_name("Bulbasaur"), None)
    
    #INTEGRATION TESTS FOR MOVE AND POKEMON CLASS**************
    def test_find_move_by_name_valid(self):
        test_pokemon = pokemon.Pokemon("", "Charmander", 39, \
            [move.Move("Scratch", 4, 100), move.Move("Dragon Breath", 6, 92), \
            move.Move("Fire Fang", 6.5, 90)])
        self.assertEqual(test_pokemon.find_move_by_name("Scratch"), test_pokemon.get_moves()[0])
    
    def test_find_move_by_name_invalid(self):
        test_pokemon = pokemon.Pokemon("", "Charmander", 39, \
            [move.Move("Scratch", 4, 100), move.Move("Dragon Breath", 6, 92), \
            move.Move("Fire Fang", 6.5, 90)])
        self.assertEqual(test_pokemon.find_move_by_name("Tackle"), None)
    
    def test_attack_miss(self):
        test_pokemon = pokemon.Pokemon("", "Charmander", 39, \
            [move.Move("Scratch", 4, 0), move.Move("Dragon Breath", 6, 92), \
            move.Move("Fire Fang", 6.5, 90)])
        test_target = pokemon.Pokemon("", "Scorbunny", 50, \
            [move.Move("Tackle", 4, 100), move.Move("Flame Charge", 5, 95), \
            move.Move("Bounce", 8.5, 80)])
        self.assertEqual(test_pokemon.attack(test_target, test_pokemon.get_moves()[0]), 0)
    
    def test_attack_hit(self):
        test_pokemon = pokemon.Pokemon("", "Charmander", 39, \
            [move.Move("Scratch", 4, 100), move.Move("Dragon Breath", 6, 92), \
            move.Move("Fire Fang", 6.5, 90)])
        test_target = pokemon.Pokemon("", "Scorbunny", 50, \
            [move.Move("Tackle", 4, 100), move.Move("Flame Charge", 5, 95), \
            move.Move("Bounce", 8.5, 80)])
        self.assertEqual(test_pokemon.attack(test_target, test_pokemon.get_moves()[0]), 4)

if __name__ == '__main__':
    unittest.main()