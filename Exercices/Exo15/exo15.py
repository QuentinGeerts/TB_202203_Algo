# exo 15
# À l’aide de deux boucles, affichez les tables de multiplication de 1 à 9

table = 1

while table <= 9:

  # Initialisation
  facteur = 1

  # Condition
  while facteur <= 10:
    resultat = table * facteur
    print(table, " * ", facteur, " = ", resultat)

    # Incrémentation / Modification
    # facteur = facteur + 1
    facteur += 1

  table += 1
