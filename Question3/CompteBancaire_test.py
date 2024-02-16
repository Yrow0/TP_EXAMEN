import pytest
from CompteBancaire import CompteBancaire

@pytest.fixture
def compte_bancaire():
    return CompteBancaire(100)

def test_deposer(compte_bancaire):
    compte_bancaire.deposer(50)
    assert compte_bancaire.obtenir_solde() == 150

def test_retirer(compte_bancaire):
    compte_bancaire.retirer(30)
    assert compte_bancaire.obtenir_solde() == 70

def test_retirer_avec_solde_insuffisant(compte_bancaire):
    with pytest.raises(ValueError):
        compte_bancaire.retirer(200)

def test_obtenir_solde(compte_bancaire):
    assert compte_bancaire.obtenir_solde() == 100

# Run the test

def main():
    pytest.main(['-v', '--tb=line', 'CompteBancaire_test.py'])

if __name__ == '__main__':
    main()