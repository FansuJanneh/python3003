a = 10
while a >= 0:
   print(a)
   a -= 1  # Vähennetään a:n arvoa yhdellä
   # a = a - 1 Sama asia
   # a-- Tämä ei toimi Pythonissa
   # a++ Eikä tämäkään
   b = a # Täällä määritetty muuttuja näkyy myös blockin ulkopuolelle
else:
   print("Silmukka päätty")

print("A:", a)
print("B:", b)

# Lista
cars = ["Toyota", "Volvo", "Seat", "Ford", "Fiat"]
for car in cars:
   print(car)

lenght = len(cars) # Cars-listan pituus
for index in range(0, lenght):
   car = cars[index]
   print(car)

# Dictionary
cars = {1:"Toyota", 2:"Volvo", 3:"Seat", 4:"Ford", 5:"Fiat"}
for car in cars:
   print("Key:", car, end=" ")
   print("Value:", cars[car])

number = 0
while True:  # Ikuinen silmukka
   number += 1
   if number % 2 == 0:
      continue
   if number >= 20:
      break
   print(number)
else: # Jos simlukasta poistutaan break:lla, elseä ei suoriteta
   print("Loop ends")
