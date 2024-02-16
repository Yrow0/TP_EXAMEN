import pytest
from Palindrome import est_palindrome
@pytest.mark.parametrize("chaine, attendu", [
    ("radar", True),                    # Cas palindrome sans espaces
    ("Été", True),                      # Cas palindrome avec caractères spéciaux et casse
    ("été été", True),  # Cas palindrome avec espaces et caractères spéciaux
    ("python", False),                  # Cas non-palindrome
    ("", True)                          # Cas de chaîne vide
])
def test_est_palindrome(chaine, attendu):
    assert est_palindrome(chaine) == attendu


