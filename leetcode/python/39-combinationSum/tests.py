import unittest
import main

class TestBlahMethods(unittest.TestCase):

    def test_happy_path(self):
        candidates = [2,3,6,7] 
        target = 7
        solution = main.Solution()
        self.assertEqual(solution.combinationSum(candidates, target), [[2, 2, 3], [7]])


if __name__ == '__main__':
    unittest.main()