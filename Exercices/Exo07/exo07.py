year = int(input("Entrez une année :"))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
  print("Année bissextile")
else:
  print("Année non bissextile")