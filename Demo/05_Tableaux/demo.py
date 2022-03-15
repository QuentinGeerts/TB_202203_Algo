# Déclaration de mon tableau
ages = []
entree = 0

# Remplir le tableau sur base des ages de la classe
while entree != -1:
  entree = int(input("Entrez votre age : "))
  if entree != -1: ages.append(entree)

print(ages)

# Afficher tous les âges
indice = 0
while indice < len(ages) :
  print(ages[indice])
  indice += 1

# Réaliser la moyenne des ages
somme = 0
indice = 0

while indice < len(ages):
  somme += ages[indice]
  indice += 1

print(somme)

moyenne = somme / len(ages)
print(moyenne)


print(f"La moyenne d'âge est de {moyenne}")