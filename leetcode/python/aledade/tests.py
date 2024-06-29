import unittest
import main

class TestBlahMethods(unittest.TestCase):

    def test_happy_path1(self):
        self.assertEqual(main.solution([1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7], 3), [0, 4, 6, 7])
    def test_happy_path2(self):
        self.assertEqual(main.solution([1, 2, 3], 3), [0])
    def test_happy_path3(self):
        self.assertEqual(main.solution([1, 2, 3, 4], 3), [0, 1])
    def test_happy_path4(self):
        self.assertEqual(main.solution([1, 2, 4], 3), [])
    def test_happy_path5(self):
        self.assertEqual(main.solution([1, 2, 2], 3), [])
    def test_happy_path6(self):
        self.assertEqual(main.solution([1, 2, 1], 3), [])
    def test_happy_path7(self):
        self.assertEqual(main.solution([1, 2], 1), [0])
    def test_happy_path8(self):
        self.assertEqual(main.solution([1, 2], 3), [])
    def test_happy_path9(self):
        self.assertEqual(main.solution([1], 1), [])
    def test_happy_path10(self):
        self.assertEqual(main.solution([1, 2, 4], 1), [0])
    def test_happy_path11(self):
        self.assertEqual(main.solution([1, 2, 3, 4, 5], 5), [0])
    def test_happy_path12(self):
        self.assertEqual(main.solution([1, 2, 3, 4, 5], 4), [0, 1])
    def test_happy_path13(self):
        self.assertEqual(main.solution([1, 2, 3, 4, 5, 6], 6), [0])


if __name__ == '__main__':
    unittest.main()