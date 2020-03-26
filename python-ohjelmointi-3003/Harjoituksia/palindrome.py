# Kirjoita funktio, joka tarkistaa, onko parametrina saatu sana palindromi
def isPalindrome(word):
   word = word.lower()

   # Poistaa kaikki white spacet (tyhjät merkit) sanasta
   # strip funktio poistaa white spacet sanan alusta ja lopusta
   # split erottaa sanan white spacen kohdalta listaksi sanoja
   # join yhdistää listan sanat yhteen
   word = "".join(word.strip().split())

   start = 0
   end = len(word) - 1

   while start <= end:
      if word[start] != word[end]:
         return False # Paluuarvon palauttaminen lopettaa funktion suorituksen
      start += 1
      end -= 1
   
   return True

sana = "Saippuakauppias"
print("Onko", sana, "palindromi?", isPalindrome(sana))
sana = "aa"
print("Onko", sana, "palindromi?", isPalindrome(sana))