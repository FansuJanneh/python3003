from exceptions import ValueTooLowError, ValueTooHighError


def giveNumber():
    while True:
        try:
            number = int(input("Give a number between 1 and 10 "))
            if number < 1:
                raise ValueTooLowError()
            if number > 10:
                raise ValueTooHighError()

            return number  # lopettaa funktion suorituksen ja palauttaa number-muuttujan arvon
        except ValueError:
            print("Invalid input")
        except ValueTooLowError:
            print("Given value was too small")
        except ValueTooHighError:
            print("Given value was too great")


number = giveNumber()
print(number)
