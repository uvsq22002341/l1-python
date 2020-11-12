"""Nous allons créer un petit logiciel de gestion du temps et des dates.
Pour cela nous aurons besoin de créer un certain nombre de fonctions utilitaires.

Un temps a le format suivant: (jour: int, heure: int, minute: int, seconde: int).
C'est un tuple de 4 éléments. Par exemple (4, 3, 13, 20) correspond à 4 jours, 3 heures, 13 minutes et 20 secondes.
Si on a une variable temps = (4, 3, 13, 20), pour accéder au premier élément on fait temps\[0\] ce qui donne 4,
le nombre de jours.

Créer la fonction qui prend comme argument le temps et renvoie le nombre de seconde total correspondant à ce temps.
Créer la fonction qui prend un nombre de secondes et renvoie le temps correspondant"""

#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    pass

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))   

def secondeEnTemps(seconde):
    """ Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    pass
    
temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")



#Les tuples. Un tuple est un type de donnée
#Pour récupérer le premier element de votre tuple, on écrit temps[0]
#0 est l'indice de départ de votre tuple.
#ATTENTION on ne peut pas modifier la valeur d'un tuple après qu'il ait été définit.

###################################### ZONE DE DEFINITION DE FONCTIONS #################

def conversion_temps_en_secondes(temps): #En argument on a une variable temps
    #Il faut convertir les jours,les heures et les minutes de notre tuple en secondes
    #1 minute : 60 secondes
    #1 heure : 60*60 secondes
    #1 jour : 60*60*24 secondes

    #Après conversion, il faut additionner toutes ces valeurs dans une variables
    nombre_total_secondes = temps[3]
    #On y ajoute les minutes du tuple converties en secondes
    nombre_total_secondes = nombre_total_secondes + (temps[2]*60) + (temps[1] * (60 ** 2)) + (temps[0] * (60 ** 2) * 24 )
    return nombre_total_secondes 


def conversion_secondes_en_tuples(nombre_total_de_secondes):
    #Pour convertir les secondes en un tuple : il faut savoir combien il y'a de secondes dans une journée, une heure , une minute 
    #et diviser SUCCESSIVEMENT mon nombre total de secondes par ces valeurs.
    une_journee_en_secondes = 60 * 60 * 24 
    nombre_de_journee = nombre_total_de_secondes // une_journee_en_secondes
    print("Le nombre de jour est :", nombre_de_journee)
    #Il faut maintenant que je retire les secondes de mon nombre de secondes totales
    nombre_total_de_secondes = nombre_total_de_secondes - (une_journee_en_secondes * nombre_de_journee)
    print("Il nous reste ", nombre_total_de_secondes)
    
    une_heure_en_secondes = 60 * 60
    nombre_d_heure = nombre_total_de_secondes // une_heure_en_secondes
    print("Le nombre d'heures est ", nombre_d_heure)

    #On retire à nouveau le nombre de secondes
    nombre_total_de_secondes = nombre_total_de_secondes - (une_heure_en_secondes * nombre_d_heure)

    une_minute_en_secondes = 60
    nombre_de_minutes = nombre_total_de_secondes // une_minute_en_secondes

    nombre_total_de_secondes = nombre_total_de_secondes - (nombre_de_minutes * une_minute_en_secondes)
    pass


############################################### ZONE DE MON PROGRAMME PRINCIPAL ###############################

a = (4,3,13,20)
#Un appel de fonction avec le tuple définit
c = conversion_temps_en_secondes( a )

print("On a ", c, "secondes")
conversion_secondes_en_tuples( c )
