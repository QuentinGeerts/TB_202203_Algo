# exo 35
# Réalisez une procédure dont l’objectif est de fusionner deux tableaux d’entiers.

def fusion(tab1, tab2):
  print(tab1)
  print(tab2)
  return tab1[:] + tab2[:]

def fission(array):
  tab1 = []
  tab2 = []

  for i, v in enumerate(array):
    if i < len(array) / 2:
      tab1.append(v)
    else:
      tab2.append(v)

  return [tab1, tab2]

print("--- Fusion ---")

my_array = fusion([1, 2, 3], [4, 5, 6])

print(my_array)

print("--- Fission ---")
print(fission([1, 2, 3, 4, 5, 6, 7, 8]))

t1, t2 = fission([1, 2, 3, 4, 5, 6, 7, 8])

print(t1)
print(t2)
