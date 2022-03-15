# Améliorez encore le justePrix : l'utilisateur a droit à 10 essais après ces 10 essais, 
# il a perdu et l'ordinateur affiche le justePrix

# Ajouter un niveau :
# ○ facile    : entre 1 et 10
# ○ moyen     : entre 1 et 100
# ○ difficile : entre 1 et 1000

# Tant que la personne veut rejouer, redemandez le niveau et générez un nombre.

# Vérifiez que tout caractère entré est correct, c'est à dire pour que le programme ne plante jamais.

# Imports
from random import randint
from os import system

# Déclaration et initialisation
rejouer = True

# Play again
while rejouer:
  # Effacer l'écran
  system("cls")
  # Rejouer
  choix = 0
  nb_tentatives = 0
  TENTATIVES_MAX = 10

  
  # -- Menu --
  while choix != "1" and choix != "2" and choix != "3":
    print("~ Juste prix ~")
    print("1. Facile : Entre 1 et 10")
    print("2. Moyen : Entre 1 et 100")
    print("3. Difficile : Entre 1 et 1000")

    choix = input("Choisissez un niveau : ")

  system("cls")

  if choix == "1":
    print("Facile")
    niveau = 10
  elif choix == "2":
    print("Moyen")
    niveau = 100
  elif choix == "3":
    print("Difficile")
    niveau = 1000

  juste_prix = randint(1, niveau)

  # Proposition
  proposition = 0
  while proposition != juste_prix and nb_tentatives < TENTATIVES_MAX:
    estValide = False

    while not estValide:
      proposition = input("Entrez une proposition :")
      
      # Vérifier que c'est un nombre
      while proposition.isalpha():
        proposition = input("Proposition incorrecte, entrez un nombre entier : ")
      
      proposition = int(proposition)

      if 1 <= proposition <= niveau:
        estValide = True
      else:
        print(f"Vous devez entrer un nombre entre 1 et {niveau}")
    nb_tentatives += 1

    if proposition != juste_prix:

      if proposition < juste_prix:
        print("C'est plus")
      else:
        print("C'est moins")

  if proposition == juste_prix: 
    print(f"Bravo, vous avez trouvé le juste prix ({juste_prix}) en {nb_tentatives} tentatives.")
  else: 
    print(f"Vous avez perdu, le juste prix était : {juste_prix}")



  # Demander à l'utilisateur s'il veut rejouer
  # true == True ? non
  rejouer = input("Voulez-vous rejouer ? (True/False) : ").lower() == "true"

# Ne plus rejouer
print("Merci d'avoir joué avec nous !")
