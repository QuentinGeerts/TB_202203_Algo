# exo 24 
# Écrivez un algorithme demandant à l’utilisateur le nombre de joueurs (max 10 joueurs) 
# Ensuite, l’algorithme doit demander à l’utilisateur le score de chaque joueur 
# Une fois ceci fini, il faut afficher la moyenne des scores

# Déclaration / Initialisation
scores = []
MAX_JOUEURS = 10
nb_joueurs = 0

# TODO Demander à l'utilisateur de rentrer le nombre de joueurs
while not 1 <= nb_joueurs <= MAX_JOUEURS:
  nb_joueurs = int(input("Entrez le nombre de joueurs de votre équipe (max: 10 joueurs) : "))

# TODO demander à l’utilisateur le score de chaque joueur et calculer la somme
somme = 0
for i in range(nb_joueurs):
  score = int(input(f"Entrez le score du joueur n°{i + 1} : "))
  # Vérification du score si besoin
  somme += score
  scores.append(score)

# TODO Calculer la moyenne des scores
moyenne = somme / len(scores)

# TODO Affichage de la moyenne des scores
print(f"La moyenne des scores est de {round(moyenne, 2)} pour les scores {scores}")