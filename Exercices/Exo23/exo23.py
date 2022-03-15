# exo 23 BONUS 
# Initialisez un tableau de 10 entiers avec les valeurs 2 4 8 16 32 64 128 256 512 1024 à l’aide d’une boucle 

# Ensuite, à l’aide d’une boucle affichez la valeur de chaque cellule du tableau avec l’opération Ecrire()

# TODO Initialisation du tableau

tab = []

for i in range(10):
  tab.append(2 ** (i + 1)) # Exposant : **

# TODO Affichage du tableau

for number in tab:
  print(number)
