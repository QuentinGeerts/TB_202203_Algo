# exo 22 Écrivez un algorithme qui saisit 6 entiers et les stocke dans un tableau,
# puis affiche le contenu de ce tableau une fois qu’il est rempli

# Déclaration le tableau
tab = [0, 0, 0, 0, 0, 0]
# OU
tab = [0] * 6

for i in range(len(tab)):
  tab[i] = int(input("Entrez un entier : "))

print(tab)

# -------------------------------------------

tab = []

for i in range(6):
  tab.append(int(input("Entrez un entier : ")))

print(tab)