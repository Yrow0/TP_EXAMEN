import unittest
from CompterMots import compter_mots

class TestCompterMots(unittest.TestCase):
    def test_phrase_non_vide(self):
        self.assertEqual(compter_mots("Bonjour le monde"), 3)
        self.assertEqual(compter_mots("Cette phrase a cinq mots."), 5)
        self.assertIsNot(compter_mots("Ceci est une autre phrase."), 4) # Test non valide

    def test_phrase_vide(self):
        self.assertEqual(compter_mots(""), 0)

    def test_phrase_avec_espaces_supplementaires(self):
        self.assertEqual(compter_mots("  Mot1  Mot2  Mot3  "), 3)
        self.assertEqual(compter_mots("     "), 0)


if __name__ == '__main__':
    unittest.main()