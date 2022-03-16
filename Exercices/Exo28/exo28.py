# exo 28
# Réalisez un algorithme permettant de rechercher une valeur dans un tableau 
# Si la valeur se trouve bien dans le tableau, nous affichons sa position

from random import randint


array = []
found_index = []
length = 10

# Remplir le tableau
for i in range(length):
  array.append(randint(1, 100))

print(array)

# Inviter l'utilisateur à rentrer une valeur à rechercher dans le tableau
search_value = int(input("Entrez une valeur à rechercher dans le tableau : "))

# Rechercher la valeur recherchée dans le tableau
for i, v in enumerate(array):
  if v == search_value:
    found_index.append(i)


# Afficher le résultat
if len(found_index) > 0:
  print(f"La valeur {search_value} a été trouvée", end="")
  if len(found_index) > 1: print(f" aux indices {found_index}.")
  else: print(f" à l'indice {found_index[0]}.")
else :
  print(f"Aucune valeur trouvée dans le tableau pour la valeur {search_value}.")