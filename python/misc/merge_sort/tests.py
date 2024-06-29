import unittest
import main

class TestBlahMethods(unittest.TestCase):
    def test_merge_sort(self):
        arr = [3,2,1,4,5]
        main.merge_sort(arr)
        self.assertEquals([1,2,3,4,5], arr)
        arr_short = []
        main.merge_sort(arr_short)
        self.assertEquals([], arr_short)


if __name__ == '__main__':
    unittest.main()