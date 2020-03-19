from enums import Choice
from player import HumanPlayer, CPUPlayer

# Tämä olisi hyvä olla määritettynä luokan ulkopuolella
winningData = {
    Choice.ROCK: {
        Choice.ROCK: 0,
        Choice.PAPER: -1,
        Choice.SCISSORS: 1
    },
    Choice.PAPER: {
        Choice.ROCK: 1,
        Choice.PAPER: 0,
        Choice.SCISSORS: -1
    },
    Choice.SCISSORS: {
        Choice.ROCK: -1,
        Choice.PAPER: 1,
        Choice.SCISSORS: 0
    }
}


def resolve(p1Choice, p2Choice, winningData):
    ''' Palauttaa 1, jos pelaaja 1 voittaa, 0 tasapelissä ja -1 pelaajan 2 voittaessa '''
    return winningData[p1Choice][p2Choice]


playerName = input("Give your name: ")

player1 = HumanPlayer(playerName)
player2 = CPUPlayer("CPU")

isQuitting = False

while isQuitting == False:
    # Peliä loopataan, kunnes pelaaja päättä lopettaa pelin
    p1Choice = player1.play()
    p2Choice = player2.play()
    result = resolve(p1Choice, p2Choice, winningData)

    print(player1.name, p1Choice.name)
    print(player2.name, p2Choice.name)

    if result == 0:
        print("It's a tie!")
    elif result == 1:
        print(player1.name, "wins!")
    else:
        print(player2.name, "wins!")

    playAgain = input("Play again (y/n)? ").lower().strip()
    isQuitting = playAgain == "n"  # true vain, kun pelaaja syöttää merkin 'n'
