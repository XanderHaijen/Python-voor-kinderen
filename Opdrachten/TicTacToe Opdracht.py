# OPGEPAST:
# De opdracht begint vanaf de vermelding "Hier begint de opdracht"
# Laat deze import staan. Je hebt hem straks nodig
import random

# ------------------ HIER BEGINT DE OPDRACHT ----------------------
# Vul de volgende functies aan om je eigen tic-tac-toe te maken

def keuze_van_computer():
    """ OPDRACHT: gebruik een return om een willekeurig getal terug te geven van 0 tot en met 8.
        TIP: in dit bestand is het package "random" al geïmporteerd
    """
    return


def keuze_van_speler():
    """
    OPDRACHT: vraag aan de speler een getal tussen 1 en 9.
    Als de speler een te groot getal geeft, vraag je het nog eens.
    Gebruik een return om het antwoord terug te geven.
    TIP: gebruik een while-lus om te checken of de input juist was.
    """
    return

def verminder_getal(getal):
    """
    OPDRACHT: verlaag het gegeven getal met 1 en gebruik een return om het terug te geven
    TIP: gebruik hiervoor een nieuwe variabele
    """
    return

def niet_bezet(vakjes, vak):
    """
    OPDRACHT: ga na of een vakje al bezet is. Een vakje niet bezet als het gelijk is aan ' ' (een spatie).
    TIP: om het juiste vakje te kiezen, kan je gebruik maken van de variabele vakjes[vak]
    """
    return True, False

def print_uitkomst(uitkomst, winnaar):
    """
    OPDRACHT: Print de winnaar van het spel, of gelijkstand.
    De variabele 'uitkomst' bevat oftewel gelijk, oftewel 'gewonnen'. Winnaar bevat wie gewonnen is.
    TIP:
        kijk eerst of de uitkomst 'gewonnen' of 'gelijk' is. Als de uitkomst 'gelijk' is, print je 'gelijkstand'.
        Zo niet moet je bekijken wie er gewonnen heeft
    """
    print('')


# -------------------- HIER EINDIGT DE OPDRACHT --------------------
# Pas hieronder geen code aan !!
# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------


boxes = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]
MENS = 'X'
COMPUTER = '0'
first_player = MENS
turn = 1
winning_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                  [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6], ]

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
            try:
                box = keuze_van_computer()
                assert box in range(9)
            except AssertionError:
                print("\n Je functie keuze_van_computer() geeft geen getal terug tussen 0 en 8!")
                exit(-2)
            except:
                print("\n Er zit een fout in je functie keuze_van_computer().")
                exit(-2)
        else:
            try:
                box = verminder_getal(keuze_van_speler())
                assert box in range(9)
            except TypeError:
                print("Ben je er zeker van dat je functie keuze_van_speler een getal vroeg en geen string? (denk aan int())")
                exit(-2)
            except AssertionError:
                print("Je functie keuze_van_speler geeft geen getal terug tussen 0 en 8!")
                exit(-2)
            except:
                print("Je functie verminder_getal() of keuze_van_speler() werkt niet correct!")
                exit(-2)
        try:
            nt_bezet = niet_bezet(boxes, box)
            if type(nt_bezet) != bool:
                print("Je functie niet_bezet() moet True of False teruggeven met een return-statement.")
                exit(-2)
            assert (boxes[box] == ' ') if nt_bezet else (boxes[box] != ' ')
        except AssertionError:
            print("Je functie niet_bezet() voert geen juiste vergelijking uit.")
            exit(-2)
        except:
            print("Je functie niet_bezet() werkt niet correct.")
            exit(-2)

        if niet_bezet(boxes, box):  # initial value
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
            player_ext = ("mens" if player == 'X' else "computer") if result == 'gewonnen' else None
            try:
                print_uitkomst(result, player_ext)
            except:
                print("Je functie print_uitkomst() werkt niet correct!")
                exit(-2)

            if result == 'gelijk':
                print("DIT IS EEN CONTROLE: het spel was gelijk. Zegt de lijn hierboven dat ook?")
            if result == 'gewonnen':
                print(f"DIT IS EEN CONTROLE: het spel was gewonnen door {player_ext}. Zegt de lijn hierboven dat ook?")
            break

        turn += 1
        player = switch_player(turn)


# Begin the game:
print('\n\nWelkom bij Tic-Tac-Toe versus de computer!')
antw = input("Ben je zeker dat je enkel code hebt aangepast waar het moest (dus tussen de twee "
             "OPDRACHT-vermeldingen)? \n"
             "Als je dit wel gedaan hebt, zal je spelletje niet werken! Geef 'ja' in als je zeker bent --> ")
if 'ja' not in antw.lower():
    exit(-2)

print_board(initial=True)
play(first_player, turn)
