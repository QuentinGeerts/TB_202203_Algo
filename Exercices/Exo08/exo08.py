# exo8 Lanceur de balles de tennis (Pseudo Code + Python)
# Réalisez l’algorithme d’un lanceur de balles de tennis. Ce lanceur possède deux états
# – pret : permet de savoir si le tennisman est prêt. Il ne faut pas lancer de balles dans le cas contraire
# – panier_vide : permet de savoir s’il y a encore des balles disponibles
# Le lanceur de balle possède l’opération « lancerBalle » qui, vous l’aurez compris, permet de lancer une balle.

pret = input("Êtes-vous prêt ?") == "True"
panier_vide = input("Le panier est-il vide ?") == "True"

if pret and not panier_vide:
  print("Lancer la balle")
else:
  print("Ne pas lancer la balle")

  if not pret: 
    print("Car vous n'êtes pas prêt.")
  
  if panier_vide: 
    print("Car le panier est vide")



