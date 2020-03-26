# Pyydä käyttäjää syöttämään sanoja, kunnes käyttäjä syöttää sanan "stop".
# Lopuksi tulosta kaikki käyttäjän syöttämät sanat (paitsi "stop")
lista = []
sana = ""
while sana != "stop":
  sana = input("Anna sana: ")
  if sana != "stop":
    lista.append(sana)

print(lista)