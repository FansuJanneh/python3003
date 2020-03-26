# Harjoitus 4
# Pyydä käyttäjää syöttämään sana. Laske montako kertaa 
# eri kirjaimet esiintyvät sanassa.
# Lopuksi tulosta kirjaimet ja niiden esiintymiskerrat.
# Esimerkkitulosteet:
# Syötä sana > tietokone
# { "t": 2, "i": 1, "e": 2, "o": 1, "k": 1, "n": 1 }
# Vihje: operaattorit in ja not in
# Lisäksi: mikä tietorakenne sopii

word = input("Give a word: ")
word = word.lower()

letters = set(word.replace(" ", ""))

for x in sorted(letters):
   print(x, "=", word.count(x))
   
# -------------------------------
word = input("Give a word ")
word = word.lower()
charCount = {}
for char in word:
   if char not in charCount:
      charCount[char] = 0
   charCount[char] += 1
print(charCount)
