def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    liste_valeurs_succesifs = []
    while (n != 1):
        if (n % 2 == 0):
            n // 2
        else :
            n = n * 3 + 1
        liste_valeurs_succesifs.append(n)
    return liste_valeurs_succesifs

def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """

######################################################

n_max = randint(500,10000)
print(testeConjecture(n_max))






