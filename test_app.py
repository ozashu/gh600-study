import unittest
from app import add

class AddTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        #self.assertEqual(add(2, 3), 6)

if __name__ == "__main__":
    unittest.main()
