# In dit bestand ga je je eigen versie van Snake maken !!
# De opdracht begint vanaf de vermelding "BEGIN VAN DE OPDRACHT"

# Laat deze imports staan. Je hebt ze straks nodig
import turtle
import turtle as t
import time
import random

# ------------------------- BEGIN VAN DE OPDRACHT ----------------------------------

def mijnNaam():
    """
    OPDRACHT: gebruik return om een string terug te geven met je naam
    """
    return 'Xander'

def maakSlang(turtle):
    """
    OPDRACHT: Gebruik Turtle en stel de slang van het spelletje in voor gebruik. Doe hiervoor het volgende:
        0. zet de snelheid van je Turtle op 0 (is al gedaan in de eerste lijn)
        1. Maak de kleur van je turtle zwart
        2. Zet de vorm van je turtle op een vierkant
        3. Hef de pen van je turtle op
        4. Ga naar de positie (0,0)
    """
    turtle.speed(0)
    turtle.color('black')
    turtle.shape('square')
    turtle.penup()
    turtle.goto(0,0)

def maakEten(turtle):
    """
    OPDRACHT: Gebruik Turtle en stel het eten van het spelletje in voor gebruik. Doe hiervoor het volgende:
        0. zet de snelheid op het laagste (is al gedaan in de eerste lijn)
        1. Maak de kleur rood
        2. Maak de vorm een cirkel. PAS OP: het is niet de bedoeling dat je een cirkel tekent!
        3. Hef de pen van je turtle op
        4. zet de beginpositie op (0,100)
    """
    turtle.speed(0)
    turtle.color("red")
    turtle.shape("circle")
    turtle.penup()
    turtle.goto(0,100)

def maakTitel(score, highscore):
    """
    OPDRACHT: maak een string die de score en highscore weergeeft. Hiervoor moet je strings bij elkaar optellen.
            Gebruik hiervoor een return
    VOORBEELD: de string zou er als volgt kunnen uitzien

           " SCORE: 50   HIGHSCORE: 250 "

    TIP: als je een getal als string wil gebruiken, kan je er str(  ) rondzetten
    """
    return "SCORE : " + str(score) + "     HIGHSCORE : " + str(highscore)

def kiesNieuwePositie():
    """
    OPDRACHT: Wanneer de slang het eten opeet, moet je een nieuwe positie voor het eten kiezen.
            Hiervoor heeft de computer een willekeurig getal tussen -290 en 290 nodig. Gebruik een return.
    TIP: gebruik hiervoor het package "random"
    """
    return random.randint(-290,290)

def nieuweScore(score):
    """
    OPDRACHT: Wanneer de slang het eten opeet, krijg je 10 punten erbij. Verhoog de gegeven score met 10 en
                gebruik een return om de nieuwe score terug te geven.
    """
    nieuweScore = score + 10
    return nieuweScore

def kiesMaximum(getal1, getal2):
    """
    OPDRACHT: bepaal het grootste van de 2 gegeven getallen en gebruik een return om dit terug te geven.
    TIP: hiervoor bestaat er een speciale functie. Welke?
    """
    maximum = max(getal1, getal2)
    return maximum

# ----------------------------- EINDE VAN DE OPDRACHT -------------------------------


if (input("Welkom bij Snake! \n \n"
      "Voordat je dit spelletje kan spelen, moet je eerst alle functies voltooien die in dit bestand staan. \n"
      "Krijg je een foutbericht? Lees dan eens de laatste lijn van de foutmelding om te"
      "zien wat je foutdeed. \n Schrijf hier 'ja' als je deze uitleg gelezen hebt. --> ")).lower().__contains__('ja'):
    pass
else:
    exit(-2)
DELAY = 0.25
delay = DELAY

# Score
score = 0
high_score = 0

# Set up the screen
wn = t.Screen()
name = mijnNaam()
if len(name) == 0:
    print("\n Je bent vergeten je naam in te geven in mijnNaam()")
    exit(-2)
else:
    my_string = "Snake Game van" + name
wn.title(my_string)
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

# Snake head
snake = t.Turtle()
maakSlang(snake)
if snake.shape() != "square" or snake.color() != ("black", "black") or snake.xcor() != 0 or snake.ycor() != 0:
    print("\n Je functie maakSlang() is niet juist.")
    exit(-2)
snake.direction = "stop"

# Snake food
food = t.Turtle()
maakEten(food)
if food.shape() != "circle" or food.color() != ("red", "red") or food.xcor() != 0 or food.ycor() != 100:
    print(" \n Je functie maakEten() is niet juist.")
    exit(-2)

segments = []

# Pen
pen = t.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
try:
    scoreboard = maakTitel(score, high_score)
    if not (scoreboard.__contains__(str(score)) and scoreboard.__contains__(str(high_score))):
        print(" \n Je score-string geeft de score en highscore niet weer.")
        exit(-2)
except:
    print("\n Je functie maakTitel() geeft geen string terug.")
    exit(-2)
pen.write(scoreboard, align="center", font=("Courier", 24, "normal"))


# Functions
def go_up():
    if snake.direction != "down":
        snake.direction = "up"


def go_down():
    if snake.direction != "up":
        snake.direction = "down"


def go_left():
    if snake.direction != "right":
        snake.direction = "left"


def go_right():
    if snake.direction != "left":
        snake.direction = "right"


def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)


# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "z")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "q")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        time.sleep(1)
        snake.goto(0, 0)
        snake.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = DELAY

        pen.clear()
        pen.write(maakTitel(score, high_score), align="center", font=("Courier", 24, "normal"))

        # Check for a collision with the food
    if snake.distance(food) < 20:
        try:
            x = kiesNieuwePositie()
            y = kiesNieuwePositie()
        except:
            print("Je functie kiesNieuwePositie() werkt niet correct.")
            exit(-2)
        food.goto(x, y)

        # Add a segment
        new_segment = t.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        old_score = score
        try:
            score = nieuweScore(score)
            score += 1
            score += -1
            assert score == old_score + 10
        except:
            print("Je functie nieuweScore werkt niet correct. Ben je er zeker van dat je een getal teruggeeft en score met 10 verhoogt?")
            exit(-2)

        old_high_score = high_score
        try:
            high_score = kiesMaximum(score, high_score)
            assert high_score == max(old_high_score, score)
        except:
            print("Je functie kiesMaximum() werkt niet correct.")
            exit(-2)

        pen.clear()
        pen.write(maakTitel(score, high_score), align="center", font=("Courier", 24, "normal"))

        # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0, 0)
            snake.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

    time.sleep(delay)


wn.mainloop()