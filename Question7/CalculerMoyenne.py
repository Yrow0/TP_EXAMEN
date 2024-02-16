def calculer_moyenne(liste):
    if not liste:
        return None
    return sum(liste) / len(liste)