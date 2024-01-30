'''
Bowen Niu
CS 5001 Fall 2023
Final Project
'''
import unittest
from mastermind_game import check_logic


class TestMastermind(unittest.TestCase):

    # following test cases test for how many black and red marbles for each simulated user input
    def test_cas_one(self):
        sim_input = ["black", "green", "yellow", "purple"]
        secret_input = ["yellow", "blue", "black", "purple"]
        # should have 1 black and 2 red with sequence black, red, red
        results = check_logic(sim_input, secret_input)
        self.assertEqual(len(results[2]), 3)
        self.assertEqual(results[0], 1)
        self.assertEqual(results[1], 2)
        self.assertEqual(results[2], ['black', 'red', 'red'])

    def test_cas_two(self):
        sim_input = ["yellow", "green", "blue", "black"]
        secret_input = ["purple", "red", "black", "blue"]
        # should have 0 black and 2 red with sequence red, red
        results = check_logic(sim_input, secret_input)
        self.assertEqual(len(results[2]), 2)
        self.assertEqual(results[0], 0)
        self.assertEqual(results[1], 2)
        self.assertEqual(results[2], ['red', 'red'])

    def test_cas_three(self):
        sim_input = ["purple", "blue", "red", "yellow"]
        secret_input = ["purple", "blue", "red", "yellow"]
        # should have 4 black and 0 red with sequence black, black, black, black
        results = check_logic(sim_input, secret_input)
        self.assertEqual(len(results[2]), 4)
        self.assertEqual(results[0], 4)
        self.assertEqual(results[1], 0)
        self.assertEqual(results[2], ['black', 'black', 'black', 'black'])

if __name__ == '__main__':
    unittest.main()