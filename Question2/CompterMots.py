def compter_mots(phrase):
    """
    Compte le nombre de mots dans une phrase.

    Args:
        phrase (str): La phrase à analyser.

    Returns:
        int: Le nombre de mots dans la phrase.
    """
    mots = phrase.split()
    return len(mots)


