import trainer
import pokemon
import move

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
    
    #UNIT TESTS FOR POKEMON CLASS ****************************
    def test_get_name(self):
        test_pokemon = pokemon.Pokemon("", "Charmander", 39, [])
        self.assertEqual(test_pokemon.get_name(), "Charmander")

    def test_set_and_get_nickname(self):
        test_pokemon = pokemon.Pokemon("", "Charmander", 39, [])
        test_pokemon.set_nickname("Charrino")
        self.assertEqual(test_pokemon.get_nickname(), "Charrino")

if __name__ == '__main__':
    unittest.main()