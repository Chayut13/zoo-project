import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price_b1(self):
        self.assertEqual(self.zoo.get_ticket_price(-1),None)
    def test_child_ticket_price_b2(self):
        self.assertEqual(self.zoo.get_ticket_price(5),50)
    def test_child_ticket_price_b3(self):
        self.assertEqual(self.zoo.get_ticket_price(15),100)
    def test_child_ticket_price_b4(self):
        self.assertEqual(self.zoo.get_ticket_price(60),150)
    def test_child_ticket_price_b5(self):
        self.assertEqual(self.zoo.get_ticket_price(80),100)
    # Add your additional test cases here.

if __name__ == '__main__':
    unittest.main()
    TestZoo(unittest)