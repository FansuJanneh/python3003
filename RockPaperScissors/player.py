import random
from enums import Choice


class Player():
    def __init__(self, name):
        self.name = name

    def play(self):
        pass


class HumanPlayer(Player):
    ''' Kuvaa ihmispelaajaa '''

    def play(self):
        choice = Choice.NONE
        while choice == Choice.NONE:
            try:
                choice = Choice(
                    int(input("Give your choice (1=Rock, 2=Paper, 3=Sicssors): ")))
                if choice.value <= 0 or choice.value > 3:
                    choice = Choice.NONE
            except ValueError:
                print("Invalid input, give a number between 1-3")
                choice = Choice.NONE
            except (KeyboardInterrupt, SystemExit):
                print("Abort execution")
                raise  # Kaataa sovelluksen
            except:
                print("Unknown error")
                choice = Choice.NONE
        return choice


class CPUPlayer(Player):
    def play(self):
        return Choice(random.randint(1, 3))
