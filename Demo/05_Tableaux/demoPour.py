from os import system
fruits = ["Pomme", "Banane", "Litchi", "Kaki", "Tomate"]

# Parcourir avec la boucle FOR tout élément itérable
for fruit in fruits:
  print(fruit)

# for lettre in "Bonjour":
#   print(lettre)


system("cls")
# POUR version 2
print(fruits)
# for indice in range(0, len(fruits), 1):
#   print(indice, fruits[indice])

# for indice in range(len(fruits) - 1, -1, -1):
#   print(indice, fruits[indice])

for indice in range(len(fruits)):
  print(indice, fruits[indice])


system("cls")
# Pour version 3

for indice, valeur in enumerate(fruits):
  print(indice, valeur)