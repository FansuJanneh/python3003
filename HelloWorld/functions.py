def add(num1, num2):
   return num1 + num2

print(add(1, 2))

# Default parametri, jos muuta arvoa ei ole määritetty kutsuttaessa, name saa arvoksi None
def hello(name=None):
   if name == None:
      print("Hello")
   else:
      print("Hello", name)

hello()
hello("Suvi")

# * tarkoittaa sitä, että funktio saa määrittämättömän määrän parametreja
# 
def sum(*numbers, printResult=False):
   result = 0
   for number in numbers:
      result += number
   if printResult:
      print(result)
   return result

summa1 = sum()
summa2 = sum(1, 2)
summa3 = sum(9, 8, 7, 6, 5, 4, 3, 2, 1, printResult=True)

def rangeSum(number):
   if number == 0:
      return 0
   return number + rangeSum(number - 1)

summa = rangeSum(10)
print(summa)
