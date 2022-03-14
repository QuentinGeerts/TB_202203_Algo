# exo 12
# Réalisez un algorithme utilisant le convertisseur de secondes,
# il reçoit deux durées en jours, heures, minutes et secondes
# puis il calcule la différence entre ces dernières

NBS_DAY = 86400
NBS_HOUR = 3600
NBS_MINUTE = 60

print("Initialisation de la première durée :")
j1 = int(input("Entrez le nombre de jours :"))
h1 = int(input("Entrez le nombre d'heures :"))
m1 = int(input("Entrez le nombre de minutes :"))
s1 = int(input("Entrez le nombre de secondes :"))

print("Initialisation de la deuxième durée :")
# Version optimisée de Python
# Découpe la chaine de caractères entrée sur base de l'espace
# Pour chaque nombre en caractères, renvoie la version convertie en entier
j2, h2, m2, s2 = [int(nombre) for nombre in input("Entrez la deuxième durée au format J H M S : ").split(" ")]

# Conversion des durées en secondes
d1 = j1 * NBS_DAY + h1 * NBS_HOUR + m1 * NBS_MINUTE + s1
d2 = j2 * NBS_DAY + h2 * NBS_HOUR + m2 * NBS_MINUTE + s2

if d1 > d2:
  dt = d1 - d2
else:
  dt = d2 - d1

# Opérateur ternaire
# dt =  d1 - d2 if d1 > d2 else d2 - d1

# Conversion de la durée en secondes en JHMS
jt = dt // NBS_DAY
ht = (dt % NBS_DAY) // NBS_HOUR
mt = ((dt % NBS_DAY) % NBS_HOUR) // NBS_MINUTE
st = ((dt % NBS_DAY) % NBS_HOUR) % NBS_MINUTE


# Afficher le résultat final

print("Récapitulatif des durées : ")
print("Durée 1 : ", j1, " jour(s) ", h1, " heure(s) ", m1, " minute(s) ", s1, " seconde(s)")
print("Durée 2 : ", j2, " jour(s) ", h2, " heure(s) ", m2, " minute(s) ", s2, " seconde(s)")
print("Durée totale : ", jt, " jour(s) ", ht, " heure(s) ", mt, " minute(s) ", st, " seconde(s)")