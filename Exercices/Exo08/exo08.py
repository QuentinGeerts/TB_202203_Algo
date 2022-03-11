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



