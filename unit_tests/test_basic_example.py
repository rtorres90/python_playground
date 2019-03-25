import unittest


class ExampleTestCase(unittest.TestCase):
    def setUp(self):
        self.title = "The title"

    def test_title_text(self):
        self.assertEqual(self.title, "The title", "The title does not match")

    def test_title_size(self):
        self.assertEqual(len(self.title), 9, "Title size is not the expected")

    def tearDown(self):
        print('Bye!')
