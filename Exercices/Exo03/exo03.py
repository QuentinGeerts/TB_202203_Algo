# Calcul des résultats
a = 8 % 3 # 2
b = 4 + a # 6
c = b * a # 12
d = (c - a) * b # 60
e = ((a + 7) * (d // a)) * 0 # (270) * 0 = > 0

# Affichage des réponses
print("a: " + str(a), 
      "b: " + str(b), 
      "c: " + str(c), 
      "d: " + str(d), 
      "e: " + str(e), 
      sep="\n")
