# exo 01 Trouvez une méthode permettant d’inverser le contenu de deux variables (du même type évidemment) Si nb 1 5 et nb 2 7 après ce traitement, nb 1 7 et nb 2 5


# Affectation
nb1 = "5"
nb2 = "7"

# Affichage des résultats
print("Avant : nb1 = ", nb1, "et nb2 =", nb2)

# Traitement
# save = nb1
# nb1 = nb2
# nb2 = save

# Raccourcis en Python
nb1, nb2 = nb2, nb1

# Affichage des résultats
print("Après : nb1 =", nb1, "et nb2 =", nb2)