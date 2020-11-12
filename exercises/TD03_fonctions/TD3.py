
##########################################################################################################################################
##########################################################################################################################################

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

    #Il faut maintenant que je retire les secondes de mon nombre de secondes totales
    nombre_total_de_secondes = nombre_total_de_secondes - (une_journee_en_secondes * nombre_de_journee)
    
    une_heure_en_secondes = 60 * 60
    nombre_d_heure = nombre_total_de_secondes // une_heure_en_secondes

    #On retire à nouveau le nombre de secondes
    nombre_total_de_secondes = nombre_total_de_secondes - (une_heure_en_secondes * nombre_d_heure)

    une_minute_en_secondes = 60
    nombre_de_minutes = nombre_total_de_secondes // une_minute_en_secondes

    nombre_total_de_secondes = nombre_total_de_secondes - (nombre_de_minutes * une_minute_en_secondes)
    return (nombre_de_journee,nombre_d_heure, nombre_de_minutes, nombre_total_de_secondes)


def mots_au_pluriel(mots): 
    a = mots + "s"
    return a

def afficheTemps(temps):
    """Affiche le temps"""
    if (temps[0] > 1 ):
        print(temps[0], mots_au_pluriel("jour"), end=" ")
    elif (temps[0] == 1 ):
        print(temps[0], "jour", end=" ")

    if (temps[1] > 1 ):
        print(temps[1], mots_au_pluriel("heure"), end=" ")
    elif (temps[1] == 1 ):
        print(temps[1], "heure", end=" ")

    if (temps[2] > 1 ):
        print(temps[2], mots_au_pluriel("minute"), end=" ")
    elif (temps[2] == 1 ):
        print(temps[2], "minute", end=" ")

    if (temps[3] > 1 ):
        print(temps[3], mots_au_pluriel("seconde"))
    elif (temps[3] == 1 ):
        print(temps[3], "seconde")
        
    pass

def demandeTemps():
    #Permet de renseigner à l'utilisateur l'usage de la fonction.
    """ Demande à l'utilisateur d'entrer des valeurs pour déterminer le nombre de jours, d'heures, de minutes
    et de secondes d'un tuple """
    
    ok = False
    while( ok == False):
        #L'UTILISATEUR RENTRE DES VALEURS
        a = int(input("Veuillez rentrer le nombre de jours : ") ) 
        b = int(input("Veuillez rentrer le nombre d'heures : ") )
        c = int(input("Veuillez rentrer le nombre de minutes : ") )
        d = int(input("Veuillez rentrer le nombre de secondes : ") )

        temps_tuple =(a,b,c,d) #Initialise un tuple des valeurs rentré par l'utilisateur.
    
        #ON VERIFIE QUE LES VALEURS DE L'UTILISATEURS SONT CORRECTS
        ok = True
        if( a < 0 or b < 0 or c < 0 or d <  0 ):
            ok = False
            if (ok == True): 
                if (b > 24 or c > 60 or d > 60):
                    ok = False
        if(ok == False):
            print("vous vous etes tromper re rentrer vos valeurs")
    return temps_tuple
    

############################################### ZONE DE MON PROGRAMME PRINCIPAL ###############################
############################################### TOUJOURS APRES ZONE DEFINTION FONCTIONS #######################

a = (0,1,0,1) #C'est mon tuple "temps"
#Un appel de fonction avec le tuple définit
c = conversion_temps_en_secondes( a )
e = conversion_secondes_en_tuples( c )
afficheTemps( e )

d = demandeTemps() #Appel de fonction
print("Le tuple crée par l'utilisateur est", d)