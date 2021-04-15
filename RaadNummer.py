import random

geheim_nummer = random.randint(1,10)
gok = int(input("Geef je gok tussen 1 en 10: "))

while geheim_nummer != gok:
    if geheim_nummer > gok:
        print("Je gekozen nummer is te klein!")
    elif geheim_nummer < gok:
        print("Je gekozen nummer is te groot")
    gok = int(input("Geef je gok tussen 1 en 10: "))

print("Juist! Je hebt het juiste nummer geraden!")
