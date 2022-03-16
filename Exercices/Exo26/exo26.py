# exo 26 
# À l’aide des boucles, 
# réalisez un algorithme permettant de trier un tableau d’entiers 
# dans l’ordre croissant

# Version 1 - array.sort() => trier le tableau par ordre croissant (<!> directement)
print("Version 1")
v1 = [4, 1, 6, 7, 2, 9, 1, 3, 10]

print(f"Avant : {v1}")

v1.sort()
# v1.sort(reverse=True)

print(f"Après : {v1}")

# Version 2 - sorted(array) => va renvoyer un tableau trié 
print("Version 2")
v2 = [4, 1, 6, 7, 2, 9, 1, 3, 10]

print(f"Avant : {v2}")

v2_trie = sorted(v2)
# v2_trie = sorted(v2, reverse=True)

# v2_trie2 = v2[:].sort()

print(f"Après : {v2_trie}")
