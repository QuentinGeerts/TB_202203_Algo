# --- Récupération d'une ou plusieurs valeurs ---
tab = [4, 7, 9, 3, 8, 2, 6, 5]
#      0  1  2  3  4  5  6  7

#  [début : fin (exclus) : pas]
#  [0 : len(tab) : 1]

print(tab[4])  # 8
print(tab[2:5])  # [9, 3, 8]
print(tab[5:7])  # [2, 6]
print(tab[5:])  # [2, 6, 5]
print(tab[:4])  # [4, 7, 9, 3]

print(tab[:])  # [4, 7, 9, 3, 8, 2, 6, 5]

print(tab[::2])  # [4, 9, 8, 6]
print(tab[::-1])  # [5, 6, 2, 8, 3, 9, 7, 4]

print()
# print(tab[9]) # list index out of range
print(tab[-1])  # [5]
print(tab[-6: 0])  # []
# -----------------------------------------------------------------

t = []

# --- Ajouter une valeur au tableau ---
# Array.append() : permet d'ajouter une valeur à la fin du tableau

t.append(3)
t.append("Bonjour")
t.append(True)

print(t)

# Array.insert(index, valeur) : permet d'ajouter une valeur à un index particulier

t.insert(0, "Jérémy")
print(t)

t.insert(2, 3.141592)
print(t)

t.insert(len(t), "Quentin")
print(t)

# --- Supprimer la valeur d'un tableau ---

removedItem = t.pop()
print(t)
print(removedItem)

removedItem = t.pop(3)
print(t)
print(removedItem)

# --- Renverser un tableau ---

t.reverse()  # Attention, modifie directement le tableau
print(t)


# --- Concaténer deux tableaux

t1 = [1, 2, 3]
t2 = [4, 5, 6]

print(t1)
print(t2)

t1.extend(t2)

print(t1)
print(t2)

