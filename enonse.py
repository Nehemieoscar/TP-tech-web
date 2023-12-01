# Mete tout karaktè yo an miniskil
chen = "Ayiti se Ayibobo"
miniskil = chen.lower()
print(miniskil)

# Koupe chenn nan tout kote ki gen espas. Epi afiche yon lis ki gen chak eleman yo.
koupe = chen.replace(" ", "")
print(list(koupe))

# Mete tout premye lèt chak mo an majiskil
mo_list = chen.split()
nouvo_chenn = ''
for mo in mo_list:
    nouvo_chenn += mo[0].upper()
print(nouvo_chenn)

# Rekipere premye lèt chak mo. Epi afiche yon nouvo chenn ak tout inisyal sa yo.
inisyal = ''
mots = chen.split()
for mot in mots:
    inisyal += mot[0]
print(inisyal)

# Ranplase tout karaktè "a" ki nan yon chenn pa "@"
nouvo_chenn = chen.replace('a', '@')
print(nouvo_chenn)

# Mete yon chenn karaktè devan dèyè, answit mete l an majiskil.
chenn_anko = chen[::-1].title()
print(chenn_anko)

# Afiche endeks premye karaktè "a" ki nan yon chenn.
endeks = chen.find('a')
print(endeks)

# Afiche total tout endeks karaktè "a" ki nan yon chenn
total = chen.count('a')
print(total)

# Kreye yon lis ki gen endeks tout karaktè "a" ki nan yon chenn
index_list = [index for index, char in enumerate(chen) if char == 'a']
print(index_list)

# Retire tout espas ki nan yon chenn, epi kole chenn sa ak kantite karaktè li genyen
chenn_sans_espas = chen.replace(" ", "")
kantite = len(chenn_sans_espas)
print(chenn_sans_espas, kantite)
