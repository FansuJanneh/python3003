carInfo = {
   "brand": "Toyota",
   "model": "Avensis",
   "year": 2010,
   "price": 10249.95
}

print(carInfo)

# Jos dictionary ei sisällä avainta, voidaan avain-arvopari lisätä dictionaryyn määrittelyn jälkeenkin
carInfo["color"] = "red"

# Jos avain on jo olemassa, arvo päivitetään
carInfo["year"] = 2011

print(carInfo)

# Dictionaryn indeksointi tapahtuu avaimen avulla
price = carInfo["price"]
print("Hinta", price)

# Pop poistaa avanta vastaavan avain-arvoparin, jos sellainen löytyy.
# Jos avainta ei löydy, palautetaan default-arvo, jos sellainen on määritetty.
# Jos avainta ei löydy ja default-arvoa ei ole määritetty, heittää pop KeyError virheen
price = carInfo.pop("price", -1)
print("Poistettu hinta", price)
price = carInfo.pop("price", -1)
print("Poistettu hinta", price)

carInfo2 = {
   "brand": "Jeep", # Auton merkki
   "model": "Compass", # Malli
   "year": 2018, # Vuosimalli
   "price": 30120.53, # Euroina
   "color": "green"
}

carList = (carInfo, carInfo2)
print(carList)

carList[0]["brand"] = "Audi"
print(carList)