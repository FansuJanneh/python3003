# Kysy käyttäjältä numero ja tulosta "Parillinen" tai "Pariton" sen mukaan,
# oliko käyttäjän syöttämä luku parillinen vai pariton
number = int(input("Anna numero: "))
if (number % 2) == 0:
    print("Parillinen")
else:
    print("Pariton")