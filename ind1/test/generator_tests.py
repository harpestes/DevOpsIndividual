import unittest
from ..generator import even_odd_generator

class GeneratorTests(unittest.TestCase):
    def test_even_odd_generator(self):
        generator = even_odd_generator()
        self.assertEqual(next(generator), "Парне")
        self.assertEqual(next(generator), "Непарне")
        self.assertEqual(next(generator), "Парне")
        self.assertEqual(next(generator), "Непарне")