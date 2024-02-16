import re

def est_palindrome(chaine):
    chaine = chaine.lower() # modification pour prendre en compte les majuscules
    chaine_inverse = chaine[::-1]
    print(chaine, chaine_inverse)
    return chaine == chaine_inverse
