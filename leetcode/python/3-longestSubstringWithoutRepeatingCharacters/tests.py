import unittest
import main

class TestBlahMethods(unittest.TestCase):

    def test_happy_path(self):
        string1 = "abcde"
        string2 = "ace"
        self.assertEqual(main.longestCommonSubsequence(string1, string2), 3)
        self.assertEqual(main.longestCommonSubsequence(string2, string2), 3)

    def test_no_overlap(self):
        string1 = "abc"
        string2 = "def"
        self.assertEqual(main.longestCommonSubsequence(string1, string2), 0)

    def test_short_happy_path(self):
        string1 = "bl"
        string2 = "yby"
        self.assertEqual(main.longestCommonSubsequence(string1, string2), 1)

    def test_happy_path_2(self):
        string1 = "ezupkr"
        string2 = "ubmrapg"
        self.assertEqual(main.longestCommonSubsequence(string1, string2), 2)

if __name__ == '__main__':
    unittest.main()