# exo05
# Réalisez un algorithme convertisseur de secondes. 

# Ce dernier reçoit un nombre de secondes et détermine le nombre de jours, heures, minutes et secondes auquel il correspond.

# ● 4561 secondes correspondent à 0 jour 1 heure 16 minutes et 1 seconde.

# Réfléchissez à la méthode que nous devons utiliser.

# Déclaration + affectation
NBS_DAY = 86400
NBS_HOUR = 3600
NBS_MINUTE = 60

# Inviter la personne a entrer un temps à convertir
seconds_T = int(input("Entrez un temps à convertir :"))

# Conversion de la durée total en secondes vers une durée en jour heure minute et seconde

days = seconds_T // NBS_DAY
hours = seconds_T % NBS_DAY // NBS_HOUR
minutes = seconds_T % NBS_DAY % NBS_HOUR // NBS_MINUTE
seconds = seconds_T % NBS_DAY % NBS_HOUR % NBS_MINUTE

# Afficher le résultat de la conversion
print(seconds_T, " secondes correspondent à ", days, " jour ", hours, " heure ", minutes, " minutes et ", seconds, " seconde.", sep="")
