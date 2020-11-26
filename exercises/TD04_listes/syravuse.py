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
    a = []
    for n in range(2, n_max):
        a = syracuse(n)
        if a[-1]== 1:
            print("le principe de syracuse pour" , n, "est vraie")

    pass

def tempsvols(n):
    """retourne le temps de vols de n """
    list_valeurs_n = syracuse(n)
    nombre_valeurs = len(list_valeurs_n)
    return nombre_valeurs

def tempsvolsliste(n_max):
    """retourne la liste de temps d vols de 1 a n_max"""
    print(n_max)
    a = []
    for i in range (1, n_max+1):
        a.append(tempsvols(n))
    return a

def leplusgrandnbr(n_max):
    a= tempsvolsliste(n_max)
    tempsvolsmax = 0
    indices_n = 0
    for i in range (0, n_max):
        if (tempsvolsmax > a[i]):
            tempsvolsmax = a[i]
            indices_n = i+1
    return (tempsvolsmax,indices_n)

def alltidue_max_n(n):
    a =syracuse(n)
    a.sort()
    return a[-1]



######################################################

n_max = randint(500,10000)
print(testeConjecture(n_max))
print(tempsvols(17))
n_max = 10
print(tempsvolsliste(n_max))





