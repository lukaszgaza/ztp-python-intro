import unittest

from person import Person

class TestPerson(unittest.TestCase):

    def test_init(self):
        p = Person("John", "Smith")
        self.assertNotEquals(p, None)

    def test_say_hello(self):
        p = Person("John", "Smith")
        self.assertEqual(p.say_hello(), "Hello! I am John Smith")

if __name__ == '__main__':
    unittest.main()
