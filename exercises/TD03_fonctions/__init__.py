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
