class Contact():
    def __init__(self, firstName, lastName):
        # Alustetaan firstName-jäsenmuuttuja parametrina saadulla arvolla
        self.firstName = firstName
        self.lastName = lastName
        self.phone = ""  # Alustetaan phone-jäsenmuuttuja tyhjäksi
        self.email = ""

    def setPhone(self, phone):
        self.phone = phone

    def setEmail(self, email):
        self.email = email

    def toString(self, includeDetails=False):
        ''' Luokan esitys merkkijonona '''
        result = self.firstName + " " + self.lastName
        if includeDetails:
            result += " " + self.phone + " " + self.email
        return result

    def toCSV(self, separator=';'):
        return self.firstName + separator + self.lastName + separator + self.phone + separator + self.email

# StudentContact perii Contact-luokan


class StudentContact(Contact):
    ''' Kontaktiluokka opiskelijalle '''

    def __init__(self, firstName, lastName, studentNumber):
        # super suorittaa kantaluokan toteutuksen funktiosta, tässä tapauksessa rakentajan
        super().__init__(firstName, lastName)
        self.studentNumber = studentNumber

    # toString ylikirjoittaa kantaluokan toteutuksen
    # Koska funktion sisällä on suoritettu myös kantaluokan toteutus, se tulee mukaan lopputulokseen
    def toString(self):
        # Alla kantaluokan toteutuksen kutsu super()-funktion avulla ja kommenteissa ilman
        # return Contact.toString(self) + ", #" + str(self.studentNumber)
        return super().toString() + ", #" + str(self.studentNumber)


def main():
    contact = Contact("Donald", "Trump")
    print(contact.toString())

    student = StudentContact("Iiro", "Insinööri", 12345)
    student.setPhone("+35840123456")
    print(student.toString())


# Tämä suorittaa main() funktion siinä tapauksessa, että tiedosto suoritetaan scriptinä.
# Jos tiedosto ladataan moduulina toiseen scriptiin tai moduuliin, jää main() suorittamatta.
if __name__ == "__main__":
    main()
