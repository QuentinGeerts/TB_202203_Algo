# exo 13
#  À l’aide d’une boucle, affichez la table de multiplication par 2

table = 2
# Initialisation
facteur = 1

# Condition
while facteur <= 10:
  resultat = table * facteur
  print(table, " * ", facteur, " = ", resultat)

  # Incrémentation / Modification
  # facteur = facteur + 1
  facteur += 1
