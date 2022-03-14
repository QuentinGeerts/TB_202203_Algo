# exo 21 
# Améliorez le "C'est plus, c'est moins, c'est gagné" pour qu'il tourne en boucle 
# tant que le justePrix n'a pas été trouvé

# L'ordinateur choisit un nombre aléatoirement entre 1 et 100

# L'utilisateur est invité à entrer un nombre et l'algorithme nous répond "C'est plus" ou "C'est moins" 

# Lorsqu'on a trouvé le bon nombre, l'algorithme affiche le nombre de tentatives effectuées pour trouver le résultat

from random import randint, random, randrange

# Générer un nombre aléatoire entre 1 et 100
justePrix = randint(1, 100)
proposition = 0
nb_tentatives = 0

while proposition != justePrix: 
  
  proposition = int(input("Entrez la proposition : "))
  nb_tentatives += 1

  if proposition != justePrix:
    if proposition < justePrix: 
      print("C'est plus")
    else: 
      print("C'est moins")
  

print("Vous avez trouvé le juste prix en", nb_tentatives, "tentatives.")
