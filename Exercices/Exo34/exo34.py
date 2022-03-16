# exo 34
# Réalisez une fonction de recherche dans un tableau. 
# Cette fonction va recevoir un tableau, la taille du tableau, et la valeur recherchée 
# en paramètres et renvoyer l’indice de l’élément dans le tableau. 
# Si l’élément ne s’y trouve pas, la fonction renvoie -1.

# ! Basé sur l'exercice 28 !!!!

# * Déclaration de fonctions
def search_in_array(array, length, search_value):
  found_index = []

  for i, v in enumerate(array):
    if v == search_value:
      found_index.append(i)
  
  return found_index if len(found_index) > 0 else -1


# * Programme principal

from random import randint

array = []

length = 10

# Remplir le tableau
for i in range(length):
  array.append(randint(1, 100))

print(array)

# Inviter l'utilisateur à rentrer une valeur à rechercher dans le tableau
search_value = int(input("Entrez une valeur à rechercher dans le tableau : "))

# Rechercher la valeur recherchée dans le tableau
indexes = search_in_array(array, length, search_value)


# Afficher le résultat
if indexes != -1:
  print(f"La valeur {search_value} a été trouvée", end="")
  if len(indexes) > 1: print(f" aux indices {indexes}.")
  else: print(f" à l'indice {indexes[0]}.")
else :
  print(f"Aucune valeur trouvée dans le tableau pour la valeur {search_value}.")
