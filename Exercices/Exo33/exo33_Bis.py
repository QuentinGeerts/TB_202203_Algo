# exo 33 
# Réalisez une fonction calculant le carré d’un nombre entier donné en paramètre.

# Remplissez un tableau de valeurs entières, ensuite créez un second tableau qui possède les carrés des valeurs du premier tableau.

# Déclaration des fonctions/procédures
def square(number : int):
  return number * number

def squareArray(array):
  array_copy = array[:]
  
  for i in range(len(array_copy)):
    array_copy[i] = square(array_copy[i])

  return array_copy


# ! Programme principal

# Faire l'appel de ma fonction
print(squareArray([5, 1, 3]))
print(squareArray([5, 1, 3, 8, 9, 1]))
print(squareArray([5, 1]))
print(squareArray([5, 1, 3, 1]))