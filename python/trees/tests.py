import unittest
import main
from main import Node

class TestBlahMethods(unittest.TestCase):
    def test_return_false(self):
        self.assertFalse(main.return_false())

    def setUp(self):
        self.root = Node(1, left=Node(3), right=Node(10))
        self.root.left.left = Node(5)
        self.root.right.left = Node(7)
        self.root.right.right = Node(3)

    def test_max(self):
        self.assertEqual(10, main.traverse_max(self.root))

if __name__ == '__main__':
    unittest.main()