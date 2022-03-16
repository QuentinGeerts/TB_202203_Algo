# exo 25 
# Inversez un tableau soit un tableau T Saisissez ce tableau 
# Changez de place les éléments de ce tableau de façon à ce que le nouveau tableau 
# soit une sorte de miroir de l'ancien et affichez le nouveau tableau

# tab = [5, 7, 1, 6, 9, 2, 3]
# tab2 = tab[::-1]

# print(tab)
# print(tab2)

# ------------------------

tab = [5, 7, 1, 6, 9, 2, 3]
tab2 = tab[:]

tab2.reverse()

print(tab)
print(tab2)