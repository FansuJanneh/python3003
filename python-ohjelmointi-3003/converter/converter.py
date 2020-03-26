# Yksikkömuunnin
# Kirjoita sovellus yksikkömuunnosten tekemiseen.
# Ohjelman tulee kysyä käyttäjältä, millaisen yksikkömuunnoksen tämä haluaa tehdä.
# Vaihtoehtoja esimerkiksi:
# t: Lämpötilamuunnos
# v: Valuuttamuunnos
#
# Kun käyttäjä on valinnut haluamansa muunnoksen: kysy käyttäjältä lisätietoja muunnoksesta
# Esim.
# Lämpötilamuunnos:
# 1: Celcius -> Fahrenheit
# 2: Fahrenheit -> Celcius
#
# Tämän valinnan jälkeen kysy käyttäjältä muunnettava arvo
# Esim:
# Anna lämpötila
#
# Lopuksi ohjelma tulostaa muunnoksen tiedot
# Esimerkkiajo (englanniksi, saa toteuttaa myös suomeksi):
# > t
# Convert temperature
# 1: Celcius to Fahrenheit
# 2: Fahrenheit to Celcius
# > 1
# Temperature to convert
# > 20
# 20°C = 68.0°F
# >
#
# Tehtävässä saatte valmiina Convertion-luokan. Peri tästä luokasta muunnoksissa
# tarvittavat luokat. Esimerkki lämpötilalle
# class TemperatureConvertion(Convertion)
# Tämä luokka muuntaa lämpötiloja °C ja °F välillä
# convert-funktio muuntaa esim. °C -> °F ja
# convertBack °F -> °C
#
# Tehtävänanto:
# Toteuta ylläkuvattu toiminnallisuus ja tuki lämpötilamuunnoksille (°C -> °F ja °F -> °C).
# Lisäominaisuutena voit toteuttaa valuuttamuunnoksia (tuki €, $ ja £)
# Valuuttamuunnokset näiden valuuttojen välillä vaatii siis kolmen luokan toteuttamista,
# muunnokset € ja £ välillä, muunnokset £ ja $ välillä ja muunnokset $ ja € välillä.


class Convertion():
    def __init__(self, value):
        self.value = value
        self.source = ""  # Lähdeyksikkö, esim. €
        self.destination = ""  # Kohdeyksikkö, esim. $

    def convert(self):
        ''' Tekee yksikkömuunnoksen lähdeyksiköstä kohdeyksikköön '''
        return 1

    def convertBack(self):
        ''' Tekee yksikkömuunnoksen kohdeyksiköstä lähdeyksikköön '''
        return 1


def main():
    pass


if __name__ == '__main__':
    main()
