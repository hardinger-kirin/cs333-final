import trainer

import unittest
class TestMethods(unittest.TestCase):
    #UNIT TESTS FOR TRAINER CLASS *************************
    def test_get_trainer_name(self):
        test_name = "Ash"
        test_trainer = trainer.Trainer(test_name)
        self.assertEqual(test_trainer.get_name(), test_name)

if __name__ == '__main__':
    unittest.main()