phones = ("iPhone", "Samsung Galaxy", "Nokia")
print(phones)

phone = phones[0]
print("First phone", phone)

# Tuplea ei voi muokata, mutta siitä voidaan tehdä lista, johon voidaan lisätä ja josta
# voidaan poistaa alkioita
phoneList = list(phones)
phoneList.append("OnePlus")
phones = tuple(phoneList)
print(phones)