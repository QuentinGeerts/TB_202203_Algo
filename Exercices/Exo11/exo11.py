# exo11 Note
# Ecrivez un algorithme qui met l'appréciation par rapport à des notes.
# Ces notes sont comprises entre 0 et 20 et peuvent être un réel.
# ○ 0 10 : I
# ○ 11 12 : S
# ○ 13 15 : B
# ○ 16 18 : TB
# ○ 19 20 : Excellent
# /!\ Gérez les erreurs : ex : 2; 25

note = int(input("Entrez une note :"))

if note >= 0 and note <= 20:
  
  if note < 11:
    print("Insuffisant")
  
  elif note < 13:
    print("Suffisant")
  
  elif note < 16:
    print("Bien")
  
  elif note < 19:
    print("Très bien")

  else:
    print("Excellent")

else:
  print("La note doit être comprise entre 0 et 20.")