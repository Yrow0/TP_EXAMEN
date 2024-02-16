import pytest
def main():
    pytest.main(['-v', '--tb=line', 'Question1/EstPremier_test.py'])
    pytest.main(['-v', '--tb=line', 'Question2/CompterMots_test.py'])
    pytest.main(['-v', '--tb=line', 'Question3/CompteBancaire_test.py'])
    pytest.main(['-v', '--tb=line', 'Question4/SommeList_test.py'])
    pytest.main(['-v', '--tb=line', 'Question5/Rectangle_test.py'])
    pytest.main(['-v', '--tb=line', 'Question6/Palindrome_test.py'])
    pytest.main(['-v', '--tb=line', 'Question7/CalculerMoyenne_test.py'])

if __name__ == '__main__':
    main()