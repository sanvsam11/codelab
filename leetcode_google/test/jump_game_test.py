#import jump_game.py and add unit tests
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))
from jump_game import Solution
class TestJumpGame(unittest.TestCase):
    def test_jump_game(self):
        test = Solution()
        self.assertEqual(test.canJump([2,3,1,1,4]), True)
        self.assertEqual(test.canJump([3,2,1,0,4]), False)
        self.assertEqual(test.canJump([0]), True)
        self.assertEqual(test.canJump([1,0,1,0]), False)
        self.assertEqual(test.canJump([1,0,1,0,0]), False)
        self.assertEqual(test.canJump([1,0,1,0,0,1]), False)
        self.assertEqual(test.canJump([1,0,1,0,0,1,0]), False)
        self.assertEqual(test.canJump([1,0,1,0,0,1,0,1]), True)
        self.assertEqual(test.canJump([1,0,1,0,0,1,0,1,0]), False)
        self.assertEqual(test.canJump([1,0,1,0,0,1,0,1,0,1]), True)
        self.assertEqual(test.canJump([1,0,1,0,0,1,0,1,0,1,0]), False)
        self.assertEqual(test.canJump([1,0,1,0,0,1,0,1,0,1,0,1]), True)
        self.assertEqual(test.canJump([1,0,1,0,0,1,0,1,0,1,0,1,0]), False)
        self.assertEqual(test.canJump([1,0,1,0,0,1,0,1,0,1,0,1,0,1]), True)
        self.assertEqual(test.canJump([1,0,1,0,0,1,0,1,0,1,0,1,0,1,0]), False)
        self.assertEqual(test.canJump([1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1]), True)
        self.assertEqual(test.canJump([1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0]), False)