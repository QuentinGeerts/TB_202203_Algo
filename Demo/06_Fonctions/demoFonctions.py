# Création d'une procédure
def direBonjour() :
  print("Bonjour")

def direBonjourPrenom(prenom) :
  print("Bonjour", prenom)

def metAJour(entier):
  entier = 3
  print("Dans la fonction metAJour:", entier) # 3

def metAJour2(tableau):
  tableau[2] = 100
  print("Dans la fonction metAJour:", tableau) # [1, 2, 100, 4, 5]

# Création d'une fonction
def auCarre(number):
  return number * number


# ------ Programme principal --------

# Instructions...
# direBonjour()
direBonjourPrenom("Quentin")

my_name = "William"
direBonjourPrenom(my_name)

result = auCarre(9)
print(result)

print(auCarre(11))

entier = 8

metAJour(entier)

print("Dans le programme principal:", entier) #


tableau = [1, 2, 3, 4, 5]
metAJour2(tableau)
print("Dans le programme principal:", tableau) # [1, 2, [3 | 100], 4, 5]
