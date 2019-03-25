import unittest


class SkippingTestCase(unittest.TestCase):

    def setUp(self):
        self.minions = 20

    @unittest.skip('Just for fun')
    def test_minions_quantity(self):
        self.assertEqual(self.minions, 20, "Quantity of minions is not the expected.")

    @unittest.skipIf(1 != 1, 'skipif')
    def test_minions_power_2(self):
        self.assertEqual(self.minions ** 2, 400)
