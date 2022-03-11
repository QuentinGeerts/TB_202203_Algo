nb1 = float(input("Entrez le premier nombre : "))
op = input("Entrez l'opérateur (+, -, *, /, %)")
nb2 = float(input("Entrez le deuxième nombre : "))

if op == "+" or op == "-" or op == "*" or op == "/" or op == "%":
  print("Opérateur reconnu")

  if op == "+":
    # Addition
    result = nb1 + nb2

  elif op == "-":
    # Soustraction
    result = nb1 - nb2

  elif op == "*":
    # Multiplication
    result = nb1 * nb2

  elif op == "/":
    # Division
    if nb2 != 0:
      result = nb1 / nb2

  elif op == "%":
    # Modulo
    if nb2 != 0:
      result = nb1 % nb2

  # Affichage du résultat
  if op == "/" and nb2 == 0:
    print("Erreur : Division par 0 impossible")
  else:
    print(nb1, op, nb2, "=", result)

else:
  print("Opérateur non reconnu")