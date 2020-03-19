print('Hello, World!')
# Lainausmerkit voidaan escapeta \ merkillä merkkijonon sisällä, jolloin se
# voidaan tulostaa

# Print-funktion valinnaiset parametrit
# sep - merkkijonojen erotinmerkki
# end - merkkijonon lopetusmerkki
print('\"How are you?\" someone said')

print("Text", "Other text")

# Input-funktio lukee käyttäjän syötteen ja palauttaa sen merkkijonona
name = input("Please insert your name > ")

# Ennen nimen tulostamista, muuta ensimmäinen kirjain isolla kirjoitetuksi
# name = name.capitalize()

if len(name) > 0 and name[0].isupper() == False:
    name = name[0].upper() + name[1:]
    print("nimi päivitetty")

print("Hello", name)


loremIpsum ="Inviverrarutrumplacerat.Nullamplacerat, \
  sapienvitaeeleifendbibendum, loremloremauctornunc, \
    id auctor mauris nisi nec justo"

a = 1
b = 1
c = 2

# \ toimii rivinjatkomerkkinä, koodia voidaan sen avulla siis jatkaa toiselle
# riville
if a == b and \
   c != a:
    print("Aika satunnaista")

print("\n\n")

# Python on vahvasti tyypitetty, string tyyppiin ei voi lisätä int tyyppistä
# muuttujaa
sum = name + str(1)
print(sum)