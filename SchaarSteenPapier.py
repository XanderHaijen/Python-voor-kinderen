import random

# OPDRACHT:
# Schrijf je eigen versie van shcaar-steen-papier tegen de computer
# 1. Begin met een programma dat het spel exact 1 keer uitvoert
# 2. Maak hiervan een functie
# 3. Vraag na elk spelletje of de speler nog eens wil spelen
#   3b. Stel de vraag nog eens als je speler niet antwoord met ja of nee
# 4. Zorg ervoor dat je programma een nieuwe keuze vraagt als de speler geen schaar, steen of papier ingeeft
# 5. Zorg ervoor dat je spelletje niet hoofdlettergevoelig is, maar alles in kleine letters kan verwerken


def schaar_steen_papier():
    keuze_van_speler = input("Geef je zet (schaar, steen, papier):  ")
    while keuze_van_speler.lower() not in ("schaar", "steen", "papier"):
        keuze_van_speler = input("Kies tussen schaar, steen of papier! \n "
                            "Geef je zet (schaar, steen, papier):  ")
    keuze_van_speler = keuze_van_speler.lower()
    mogelijke_acties = "steen", "papier", "schaar"
    keuze_van_computer = random.choice(mogelijke_acties)
    print("Jij koos " + keuze_van_speler + " ,de computer koos " + keuze_van_computer + " .")

    if keuze_van_speler == keuze_van_computer:
        print("Jij en de computer kozen allebei " + keuze_van_speler +". Gelijkspel!")
    elif keuze_van_speler == "steen":
        if keuze_van_computer == "schaar":
            print("Steen klopt de schaar kapot. Jij wint!")
        else:
            print("Papier bedekt steen! Je verliest.")
    elif keuze_van_speler == "papier":
        if keuze_van_computer == "steen":
            print("Papier bedekt steen. Jij wint!")
        else:
            print("Schaar knipt papier. Je verliest.")
    elif keuze_van_speler == "schaar":
        if keuze_van_computer == "papier":
            print("Schaar knipt papier. Jij wint!")
        else:
            print("Steen klopt de schaar kapot. Jij verliest.")

# Spelletje #
speel_nog_eens = "ja"

while speel_nog_eens == 'ja':
    schaar_steen_papier()
    speel_nog_eens = input("Nog eens spelen? (ja / nee): ").lower()
    while speel_nog_eens.lower() != "ja" and speel_nog_eens.lower() != "nee":
        speel_nog_eens = input("Antwoord met ja of nee: ").lower()


