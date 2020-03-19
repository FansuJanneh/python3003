import os

dirname = os.path.dirname(__file__)
filePath = os.path.join(dirname, 'exampleFile.txt')

fruits = []

# Polku suhteessa siihen sijaintiin, josta sovellusta suoritetaan
# filePath = "File/exampleFile.txt"

# Avataan tiedosto luku-tilassa
file = open(filePath, "r")

for row in file:
    # str.strip() poistaa white spacet merkkijonon alusta ja lopusta
    fruits.append(row.strip())

# Avattu tiedosto on muistettava sulkea
file.close()

for fruit in fruits:
    print(fruit)

fruits.append("Banana")
fruits.append("Kiwi")

# Tiedostoon kirjoitettava data
fileContent = ""

for fruit in fruits:
    # Kirjoitetaan hedelmät merkkijonoon erotettuna rivinvaihtomerkillä
    fileContent += fruit + "\n"

# Kun tiedosto avataan with avainsanan avulla, tiedostoa ei tarvitse erikseen sulkea
# Python tekee sen meidän puolesta
with open(filePath, "w") as file:
    file.write(fileContent)
