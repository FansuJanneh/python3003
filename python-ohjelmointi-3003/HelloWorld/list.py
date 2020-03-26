carInfo = ["Volvo", "V70", 2019, "Red", 39495.95, 5]
print(carInfo)

carList = ["Volvo", "Toyota", "Volkswagen", "Audi", "Nissan", "Audi"]
print(carList)

car = carList[2]  # Volkswagen
print("Car at index 2", car, sep="\t")

car = carList[-1]  # Nissan
print("Last car:", car)

carList.append("Jeep")  # append lisää alkion listan loppuun
carList.insert(1, "Fiat")  # Lisää alkion listan tiettyyn indeksiin
print(carList)

# poistaa index-parametrilla märitetyn tai oletuksena viimeisen alkion listasta
removed = carList.pop()
print(carList)
print("Removed", removed)

# Poistaa tietyn arvon (vain ensimmäisen listassa olevan)
# Ei palauta poistettua arvoa
carList.remove("Audi")
print(carList)

del carList[1:3] # Poistaa indeksillä määritetyn arvon listasta
print(carList)

carList.clear() # Tyhjentää listan

del carList # Poistaa muuttujan (ja sen sisällön)
print(carList)