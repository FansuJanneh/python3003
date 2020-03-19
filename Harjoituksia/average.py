# Pyydä käyttäjää syöttämään, monenko luvun keskiarvon tämä haluaa laskea.
# Tämän jälkeen pyydä käyttäjää syöttämään näin monta lukua.
# Laske lopuksi lukujen keskiarvo ja tulosta tämä käyttäjälle
amount = int(input("Insert length: "))
arr = []
j = 0

while j < amount:
    num = int(input("Insert number: "))
    arr.append(num)
    j += 1
avrg = sum(arr) / len(arr)
print(arr, avrg)