import pytest
from EstPremier import est_premier

@pytest.mark.parametrize("nombre, attendu", [
    (2, True),
    (3, True),
    (5, True),
    (7, True),
    (11, True),
    (13, True),
    (17, True),
    (0, False),
    (1, False),
    (4, False),
    (6, False),
    (8, False),
    (9, False),
    (15, False),
    (104729, True),  # Nombre premier (10 000ème nombre premier)
    (104730, False)  # Nombre non premier (10 001ème nombre premier + 1)
])
def test_est_premier(nombre, attendu):
    assert est_premier(nombre) == attendu
