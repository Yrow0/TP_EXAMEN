import unittest
from SommeList import somme_liste

class TestSommeListe(unittest.TestCase):
    def test_liste_non_vide(self):
        self.assertEqual(somme_liste([1, 2, 3, 4, 5]), 15)
        self.assertEqual(somme_liste([10, 20, 30]), 60)
        self.assertEqual(somme_liste([-1, -2, -3, -4, -5]), -15)
        self.assertEqual(somme_liste([-10, -20, -30]), -60)
        self.assertEqual(somme_liste([0, 0, 0, 0, 0]), 0)

    def test_liste_vide(self):
        self.assertEqual(somme_liste([]), 0)

if __name__ == '__main__':
    unittest.main()