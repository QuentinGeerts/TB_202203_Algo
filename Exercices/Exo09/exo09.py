stockCoca = 0
stockFanta = 2
stockEau = 10

print("Menu :")
print("1. Coca")
print("2. Fanta")
print("3. Eau")
choix = input("Choisissez une boisson : ")

if choix == "1" or choix == "2" or choix == "3":
  
  if choix == "1" and stockCoca > 0:
    print("Voici votre boisson")
    # stockCoca = stockCoca - 1
    stockCoca -= 1
  
  elif choix == "2" and stockFanta > 0:
    print("Voici votre boisson")
    stockFanta -= 1

  elif choix == "3" and stockEau > 0:
    print("Voici votre boisson")
    stockEau -= 1

  else:
    print("Rupture de stocks")

else:
  print("Boisson non reconnue")