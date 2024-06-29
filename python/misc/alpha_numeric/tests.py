import unittest
import main

class TestBlahMethods(unittest.TestCase):
    def test_aplha_numeric(self):
        self.assertEqual(True, main.alpha_numeric("abs"))
        self.assertTrue(main.alpha_numeric("123asdf"))
        self.assertFalse(main.alpha_numeric("asdf@98"))
        self.assertFalse(main.alpha_numeric(""))
        self.assertFalse(main.alpha_numeric(123))
        self.assertFalse(main.alpha_numeric("!@#$"))
        self.assertFalse(main.alpha_numeric("!asdf"))
        self.assertFalse(main.alpha_numeric("jlkj#"))
        self.assertTrue(main.alpha_numeric("1"))


if __name__ == '__main__':
    unittest.main()