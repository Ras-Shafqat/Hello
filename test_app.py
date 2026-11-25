import unittest
from app import hello, add

class TestApp(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello from Jenkins CI/CD Pipeline!")

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

if __name__ == "__main__":
    unittest.main()
