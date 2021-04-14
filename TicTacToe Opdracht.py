# OPGEPAST: Pas niets aan aan de code hieronder. De opdracht begint vanaf de vermelding "Hier begint de opdracht"

# Command-line Tic Tac Toe for HUMAN vs COMPUTER written in Python.
# Play in a terminal by running 'python tictactoe.py'.


import random

boxes = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]
MENS = 'X'
COMPUTER = '0'
first_player = MENS
turn = 1
winning_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                  [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6], ]

# ------------------ HIER BEGINT DE OPDRACHT ----------------------
# Vul de volgende functies aan om je eigen tic-tac-toe te maken

def keuze_van_computer():
    """ OPDRACHT: gebruik een return om een willekeurig getal terug te geven van 0 tot en met 8.
        TIP: in dit bestand is het package "random" al geïmporteerd
    """
    return 0


def keuze_van_speler():
    """
    OPDRACHT: vraag aan de speler een getal tussen 0 en 8.
    Als de speler een te groot getal geeft, vraag je het nog eens.
    Gebruik een return om het antwoord terug te geven
    """
    return input("  ")


def niet_bezet(vakjes, vak):
    """
    OPDRACHT: ga na of een vakje al bezet is. Een vakje niet bezet als het gelijk is aan ' '.
    TIP: om het juiste vakje te kiezen, kan je gebruik maken van vakjes[vak]
    """
    pass


def print_uitkomst(uitkomst, winnaar):
    """
    OPDRACHT: Print de winnaar van het spel, of gelijkstand.
    De variabele 'uitkomst' bevat oftewel gelijk, oftewel 'gewonnen'. Winnaar bevat wie gewonnen is.
    TIP:
        kijk eerst of de uitkomst 'gewonnen' of 'gelijk' is. Als de uitkomst 'gelijk' is, print je gelijkstand.
        Zo niet moet je kijken wie er gewonnen heeft
    """
    pass


# -------------------- HIER EINDIGT DE OPDRACHT --------------------
# Pas hieronder geen code aan !!

def print_board(initial=False):
    """ Print the game board. If this is the beginning of the game,
        print out 1-9 in the boxes to show players how to pick a
        box. Otherwise, update each box with X or 0 from boxes[].
    """
    board = '''
             {} | {} | {} 
            -----------
             {} | {} | {}
            -----------
             {} | {} | {} 
        '''
    print(board.format(*([x for x in range(1, 10)] if initial else boxes)))


def take_turn(player, turn):
    """ Create a loop that keeps asking the current player for
        their input until a valid choice is made.
    """

    while True:
        if player is COMPUTER:
            box = keuze_van_computer()
            if box not in range(9):
                raise RuntimeError("De computer kiest een verkeerd getal!")
        else:
            box = keuze_van_speler()
            try:
                if box < 0 or box > 8:
                    raise RuntimeError('Het getal is te klein of te groot. Zorg ervoor dat je een nieuw getal vraagt!')
            except:
                raise TypeError("Ben je er zeker van dat je int(input()) gebruikte?")

        if niet_bezet(boxes, box):  # initial value
            if boxes[box] != '':
                raise RuntimeError("Je functie niet_bezet werkt niet juist. Kijk nog eens na!")
            boxes[box] = player  # set to value of current player
            break
        else:
            print('Dit veldje is al bezet. Probeer opnieuw')

def switch_player(turn):
    """ Switch the player based on how many moves have been made.
        X starts the game so if this turn # is even, it's 0's turn.
    """
    current_player = COMPUTER if turn % 2 == 0 else MENS
    return current_player


def check_for_win(player, turn):
    """ Check for a win (or a tie). For each combo in winning_combos[],
        count how many of its corresponding squares have the current
        player's mark. If a player's score count reaches 3, return a win.
        If it doesn't, and this is already turn # 9, return a tie. If
        neither, return False so the game continues.
    """
    if turn > 4:  # need at least 5 moves before a win is possible
        for combo in winning_combos:
            score = 0
            for index in combo:
                if boxes[index] == player:
                    score += 1
                if score == 3:
                    return 'gewonnen'

        if turn == 9:
            return 'gelijk'


def play(player, turn):
    """ Create a loop that keeps the game in play
        until it ends in a win or tie
    """
    while True:
        take_turn(player, turn)
        print_board()
        result = check_for_win(player, turn)
        if result is not None:
            player_ext = player if result == 'gewonnen' else None
            print_uitkomst(result, player_ext)
            if result == 'gelijk':
                print("DIT IS EEN CONTROLE: het spel was gelijk. Zegt de lijn hierboven dat ook?")
            if result == 'gelijk':
                print(f"DIT IS EEN CONTROLE: het spel was gewonnen door {player}. Zegt de lijn hierboven dat ook?")
            break

        turn += 1
        player = switch_player(turn)


# Begin the game:
print('\n\nWelkom bij Tic Tac Toe versus de computer!')
antw = input("Ben je zeker dat je enkel code hebt aangepast waar het moest (dus tussen de twee "
             "OPDRACHT-vermeldingen)? \n "
             "Als je dit wel gedaan hebt, zal je spelletje niet werken! Geef 'ja' in als je zeker bent --> ")
if antw.lower() != 'ja':
    raise InterruptedError("Je bent niet zeker of je enkel de juiste code hebt aangepast. Kijk dit na of vraag hulp!")

print_board(initial=True)
play(first_player, turn)