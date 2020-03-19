from Contact.contact import Contact
import sys
from os import path  # Tiedostopolkufunktioita jne.


class AddressBook():
    def __init__(self, filePath):
        super().__init__()
        # Lista, johon yhteystiedot tallennetaan
        self.contacts = []
        # Tiedostopolku yhteystietojen tallentamiseen
        self.filePath = filePath
        # Lukee yhteystiedot tiedostosta
        self.ReadFromFile(filePath)

    def AddContact(self, contact):
        if isinstance(contact, Contact) == False:
            # isinstance tarkistaa, onko muuttuja tiettyä tyyppiä,
            # tässä tapauksessa Contact-tyyppiä
            raise TypeError()

        if contact in self.contacts:
            # Tarkistetaan, onko kontakti jo lisätty listaan. Jos on, palauta False
            return False

        # Lisätään kontakti listaan ja palautetaan True onnistumisen merkiksi
        self.contacts.append(contact)
        return True

    def ReadFromFile(self, filePath=None):
        # Lukee kontaktit tiedostosta, luo niistä Contact-oliot ja tallentaa
        # ne luokan sisäiseen tietorakenteeseen
        if filePath == None:
            # Jos filePath == None, käytetään jäsenmuuttujan filePath-arvoa
            filePath = self.filePath

        if path.exists(filePath) == False:
            # Tiedostoa ei ole olemassa, poistutaan funktiosta
            return False

        with open(filePath, "r", encoding='utf-8') as file:
            # Tiedosto avattu lukemista varten. Viittaus tiedostoon tallennettu
            # file-muuttujaan
            for line in file:
                # For-silmukka, joka käy tiedoston läpi rivi kerrallaan
                # strip() poistaa white spacet rivin alusta ja lopusta
                # split jakaa merkkijonon erotinmerkkien kohdilta osiin
                # Etunimi (0), Sukunimi (1), Puhelin (2), Sähköposti (3)
                items = line.strip().split(';')
                contact = Contact(items[0], items[1])
                contact.setPhone(items[2])
                contact.setEmail(items[3])
                self.AddContact(contact)

    def SaveContacts(self, filePath=None):
        # Tallentaa kontaktit luokan sisäisestä tietorakenteesta tiedostoon
        if filePath == None:
            # Jos filePath:ia ei ole välitetty, käytetään jäsenmuuttujaa
            filePath = self.filePath

        fileContent = ""
        for contact in self.contacts:
            # Käydään kontaktit läpi ja kirjoitetaan jokainen fileContent merkkijonoon
            # omalle rivilleen
            fileContent += contact.toCSV() + '\n'

        with open(filePath, "w", encoding='utf-8') as file:
            # Ylikirjoitetaan koko tiedosto (parametri "w")
            file.write(fileContent)

    def PrintContacts(self):
        # Tulostaa yhteystiedot
        for contact in self.contacts:
            print(contact.toString(includeDetails=True))


def main():
    # Luetaan tiedoston polku komentoriviltä, parametrit listassa sys.argv
    # sys.argv[0] sisältää sovelluksen nimen (contacts.py)
    # Loput parametrit ovat tämän jälkeen tulevissa alkioissa
    if len(sys.argv) != 2:
        # Sulkee sovelluksen. Virhekoodi 2 tarkoittaa virhettä parametreissa
        print("Virheelliset parametrit")
        sys.exit(2)

    filePath = sys.argv[1]  # Yhteystietotiedoston polku

    addressBook = AddressBook(filePath)

    # Luetaan komento siten, että poistetaan siitä edeltävät ja lopettavat white spacet
    # ja muutetaan komento pienellä kirjoitetuksi

    # Silmukassa pyydetään käyttäjän komentoa, kunnes käyttäjä haluaa sulkea sovelluksen
    # Komennot:
    # a: lisää uusi yhteystieto. Kysy yhteystiedon datat erikseen
    # p: tulostaa yhteystiedot
    # s: tallentaa yhteystiedot tiedostoon
    # q: sulkee sovelluksen
    # mikä tahansa muu komento: tulosta ohje
    command = input("> ").strip().lower()
    while command != 'q':
        if command == 'a':
            firstName = input("First Name: ")
            lastName = input("Last Name: ")
            phone = input("Phone: ")
            email = input("Email: ")

            contact = Contact(firstName, lastName)
            contact.setPhone(phone)
            contact.setEmail(email)

            addressBook.AddContact(contact)
        elif command == 'p':
            addressBook.PrintContacts()
        elif command == 's':
            addressBook.SaveContacts()
        elif command != 'q':
            print("Komennot", "a: lisää yhteystieto", "p: tulosta yhteystiedot",
                  "s: tallenna yhteystiedot", "q: sulje sovellus", sep="\n")

        if command != 'q':
            command = input("> ").strip().lower()


if __name__ == "__main__":
    main()
