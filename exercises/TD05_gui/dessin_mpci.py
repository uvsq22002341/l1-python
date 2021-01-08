import tkinter as tk


root = tk.Tk()

# Début de votre code

#4 boutons et 1 canvas

#CREATION DES BOUTONS
bouton_cercle = tk.Button(text = "Cercle")
bouton_carre = tk.Button(text= "Carre")
bouton_croix = tk.Button(text="Croix")
bouton_couleur = tk.Button(text="Choisir une couleur")


#PLACEMENT DES BOUTONS
bouton_cercle.grid(row = 1, column = 0)
bouton_carre.grid(row = 2, column = 0)
bouton_croix.grid(row = 3, column = 0)
bouton_couleur.grid(row = 0, column = 2)


#CREATION DU CANVAS
canvas = tk.Canvas(background = "#000000")

#POSITIONNE LE CANVAS
canvas.grid(row = 1, column = 1, rowspan = 3, columnspan = 3)

# Fin de votre code
root.mainloop()