import random
def rockPaperScissors():
    user_action = input("Geef je zet (schaar, steen, papier):  ")
    possible_actions = ["steen", "papier", "schaar"]
    computer_action = random.choice(possible_actions)
    print("Jij koos " + user_action + " ,de computer koos " + computer_action + " .")

    if user_action == computer_action:
        print(f"Jij en de computer kozen allebei {user_action}. Gelijkspel!")
    elif user_action == "steen":
        if computer_action == "schaar":
            print("Steen klopt de schaar kapot. Jij wint!")
        else:
            print("Papier bedekt steen! Je verliest.")
    elif user_action == "papier":
        if computer_action == "steen":
            print("Papier bedekt steen. Jij wint!")
        else:
            print("Schaar knipt papier. Je verliest.")
    elif user_action == "schaar":
        if computer_action == "papier":
            print("Schaar knipt papier. Jij wint!")
        else:
            print("Steen klopt de schaar kapot. Jij verliest.")

# Spelletje #
play_again = "ja"

while play_again == 'ja':
    rockPaperScissors()
    play_again = input("Nog eens spelen? (ja / nee): ").lower()
    while play_again.lower() != "ja" and play_again.lower() != "nee":
        play_again = input("Antwoord met ja of nee: ").lower()

