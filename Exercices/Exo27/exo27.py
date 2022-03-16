# exo 27 
# Refaites l'algorithme qui demande à l’utilisateur de taper 10 entiers et 
# qui affiche le plus petit de ces entiers mais cette fois ci à l'aide d'un tableau
# et sans retenir le minimum lors de la saisie

from random import randint

# array = [5, 7, 3, 1, 2, 9]
array = [] 
length = 10

# TODO Remplir le tableau
for i in range(length):
  # array.append(int(input("Entrez une valeur : ")))
  array.append(randint(1, 100))

# TODO Analyser le tableau pour trouver le minimum
min = array[0]
max = array[0]

for i, v in enumerate(array):
  if v < min:
    min = v
    min_pos = i
  
  if v > max:
    max = v
    max_pos = i

# TODO Afficher le minimum
print(array)
print(f"La valeur minimum est {min} et se trouve à la position {min_pos}")
print(f"La valeur maximum est {max} et se trouve à la position {max_pos}")
