import pytest
from Question5.Rectangle import Rectangle

@pytest.fixture
def rectangle():
    return Rectangle(5, 10)

def test_calculer_perimetre(rectangle):
    assert rectangle.calculer_perimetre() == 30

def test_calculer_surface(rectangle):
    assert rectangle.calculer_surface() == 50


def main():
    pytest.main(['-v', '--tb=line', 'Rectangle_test.py'])

if __name__ == '__main__':
    main()
# Run the test
