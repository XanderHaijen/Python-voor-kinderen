# Schaar, steen, papier
# 1. computer kiest
# 2. jij kiest
import random
computer = random.choice(("schaar","steen","papier"))
speler = input("Schaar, steen of papier? ")
if computer == "schaar":
    if speler == "schaar":
        print("gelijkspel")
    elif speler == "steen":
        print("je bent gewonnen")
    elif 