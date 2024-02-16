import pytest
from CalculerMoyenne import calculer_moyenne
@pytest.mark.parametrize("liste, attendu", [
    ([1, 2, 3, 4, 5], 3),
    ([10, 20, 30], 20),
    ([0, 0, 0, 0, 0], 0),
    ([], None)
])
def test_calculer_moyenne(liste, attendu):
    assert calculer_moyenne(liste) == attendu

# Run the test with the following command:
def main():
    pytest.main(['-v', '--tb=line', 'CalculerMoyenne_test.py'])

if __name__ == '__main__':
    main()