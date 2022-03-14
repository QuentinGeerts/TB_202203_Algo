# exo07
# Année bissextile

# Réalisez un petit algorithme qui sur base d’une année donnée va déterminer s’il s’agit d’une année bissextile. 

# Une année est bissextile si :

# elle est divisible par 4, 
# mais non divisible par 100. 
# Ou si elle est divisible par 400.

# Bissextile : 2000, 1996
# !Bissextile : 1900, 1997

year = int(input("Entrez une année :"))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
  print("Année bissextile")
else:
  print("Année non bissextile")
