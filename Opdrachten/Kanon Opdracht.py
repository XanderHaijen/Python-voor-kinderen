# Kanon: raak zo veel mogelijk doelen
# De opdracht begint bij "HIER BEGINT DE OPDRACHT"

# Laat deze imports staan: je hebt ze straks nodig.
import collections.abc as collections
import math
import random
import turtle


# --------------------------- HIER BEGINT DE OPDRACHT ---------------------------------


def verbergTurtle():
    """
    OPDRACHT: Gebruik een commando uit het turtle-package om de turtle te verbergen.
    TIP: dit kan in 1 lijn!
    """
    pass

def snelheidVanDoelen():
    """
    OPDRACHT: Gebruik een return-statement om de snelheid van de doelen te bepalen.
        Dit is een kommagetal tussen 0 en 3. Je mag zelf kiezen hoe snel je doelen vliegen.
    """
    return 0

def verhoogScore(score):
    """
    OPDRACHT: Als je een bal raakt, verdien je een punt. Gebruik een return om een verhoogde score terug te geven.
            Een verhoogde score is de score met één punt bij.
    """
    return 0

def spelVoorbij(status):
    """
    OPDRACHT: Print een bericht als het spel afgelopen is. Het spel is afgelopen als de variabele status gelijk is
            aan 'gedaan'.
    """
    print("")

def positieVanDoelen():
    """
    OPDRACHT: De doelen verschijnen op een willekeurige plaats langs de zijkant. Om die plaats te bepalen, moet je een
                return gebruiken om een willekeurig getal tussen -150 en 150 terug te geven
    TIP: het package 'random' is al geïmporteerd
    """
    return 0

def scorebord(score):
    """
    OPDRACHT: maak een string voor het scorebord die de score weergeeft.
            !! Gebruik een return om je string terug te geven. !!
    VOORBEELD: Zo'n string ziet er bijvoorbeeld als volgt uit.

            " SCORE : 12 "

    TIP: Wil je een getal gebruiken in een string, kan je dit doen door er str(  ) rond te zetten
    """
    return ""


# ------------------------------------ HIER EINDIGT DE OPDRACHT -------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# -------------------------------                                         ---------------------------------------------
# -------------------------------     PAS HIERONDER GEEN CODE AAN !!      ---------------------------------------------
# -------------------------------                                         ---------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------


class Vector(collections.Sequence):
    """Two-dimensional Vector.
    Vectors can be modified in-place.
    >>> v = Vector(0, 1)
    >>> v.move(1)
    >>> v
    Vector(1, 2)
    >>> v.rotate(90)
    >>> v
    Vector(-2.0, 1.0)

    """
    # pylint: disable=invalid-name
    PRECISION = 6

    __slots__ = ('_x', '_y', '_hash')

    def __init__(self, x, y):
        """Initialize Vector with coordinates: x, y.

        >>> v = Vector(1, 2)
        >>> v.x
        1
        >>> v.y
        2

        """
        self._hash = None
        self._x = round(x, self.PRECISION)
        self._y = round(y, self.PRECISION)

    @property
    def x(self):
        """X-axis component of Vector.

        >>> v = Vector(1, 2)
        >>> v.x
        1
        >>> v.x = 3
        >>> v.x
        3

        """
        return self._x

    @x.setter
    def x(self, value):
        if self._hash is not None:
            raise ValueError('cannot set x after hashing')
        self._x = round(value, self.PRECISION)

    @property
    def y(self):
        """Y-axis component of Vector.

        >>> v = Vector(1, 2)
        >>> v.y
        2
        >>> v.y = 5
        >>> v.y
        5

        """
        return self._y

    @y.setter
    def y(self, value):
        if self._hash is not None:
            raise ValueError('cannot set y after hashing')
        self._y = round(value, self.PRECISION)

    def __hash__(self):
        """v.__hash__() -> hash(v)

        >>> v = Vector(1, 2)
        >>> h = hash(v)
        >>> v.x = 2
        Traceback (most recent call last):
            ...
        ValueError: cannot set x after hashing

        """
        if self._hash is None:
            pair = (self.x, self.y)
            self._hash = hash(pair)
        return self._hash

    def __len__(self):
        """v.__len__() -> len(v)

        >>> v = Vector(1, 2)
        >>> len(v)
        2

        """
        return 2

    def __getitem__(self, index):
        """v.__getitem__(v, i) -> v[i]

        >>> v = Vector(3, 4)
        >>> v[0]
        3
        >>> v[1]
        4
        >>> v[2]
        Traceback (most recent call last):
            ...
        IndexError

        """
        if index == 0:
            return self.x
        if index == 1:
            return self.y
        raise IndexError

    def copy(self):
        """Return copy of Vector.

        >>> v = Vector(1, 2)
        >>> w = v.copy()
        >>> v is w
        False

        """
        type_self = type(self)
        return type_self(self.x, self.y)

    def __eq__(self, other):
        """v.__eq__(w) -> v == w

        >>> v = Vector(1, 2)
        >>> w = Vector(1, 2)
        >>> v == w
        True

        """
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __ne__(self, other):
        """v.__ne__(w) -> v != w

        >>> v = Vector(1, 2)
        >>> w = Vector(3, 4)
        >>> v != w
        True

        """
        if isinstance(other, Vector):
            return self.x != other.x or self.y != other.y
        return NotImplemented

    def __iadd__(self, other):
        """v.__iadd__(w) -> v += w

        >>> v = Vector(1, 2)
        >>> w = Vector(3, 4)
        >>> v += w
        >>> v
        Vector(4, 6)
        >>> v += 1
        >>> v
        Vector(5, 7)

        """
        if self._hash is not None:
            raise ValueError('cannot add Vector after hashing')
        if isinstance(other, Vector):
            self.x += other.x
            self.y += other.y
        else:
            self.x += other
            self.y += other
        return self

    def __add__(self, other):
        """v.__add__(w) -> v + w

        >>> v = Vector(1, 2)
        >>> w = Vector(3, 4)
        >>> v + w
        Vector(4, 6)
        >>> v + 1
        Vector(2, 3)
        >>> 2.0 + v
        Vector(3.0, 4.0)

        """
        copy = self.copy()
        return copy.__iadd__(other)

    __radd__ = __add__

    def move(self, other):
        """Move Vector by other (in-place).

        >>> v = Vector(1, 2)
        >>> w = Vector(3, 4)
        >>> v.move(w)
        >>> v
        Vector(4, 6)
        >>> v.move(3)
        >>> v
        Vector(7, 9)

        """
        self.__iadd__(other)

    def __isub__(self, other):
        """v.__isub__(w) -> v -= w

        >>> v = Vector(1, 2)
        >>> w = Vector(3, 4)
        >>> v -= w
        >>> v
        Vector(-2, -2)
        >>> v -= 1
        >>> v
        Vector(-3, -3)

        """
        if self._hash is not None:
            raise ValueError('cannot subtract Vector after hashing')
        if isinstance(other, Vector):
            self.x -= other.x
            self.y -= other.y
        else:
            self.x -= other
            self.y -= other
        return self

    def __sub__(self, other):
        """v.__sub__(w) -> v - w

        >>> v = Vector(1, 2)
        >>> w = Vector(3, 4)
        >>> v - w
        Vector(-2, -2)
        >>> v - 1
        Vector(0, 1)

        """
        copy = self.copy()
        return copy.__isub__(other)

    def __imul__(self, other):
        """v.__imul__(w) -> v *= w

        >>> v = Vector(1, 2)
        >>> w = Vector(3, 4)
        >>> v *= w
        >>> v
        Vector(3, 8)
        >>> v *= 2
        >>> v
        Vector(6, 16)

        """
        if self._hash is not None:
            raise ValueError('cannot multiply Vector after hashing')
        if isinstance(other, Vector):
            self.x *= other.x
            self.y *= other.y
        else:
            self.x *= other
            self.y *= other
        return self

    def __mul__(self, other):
        """v.__mul__(w) -> v * w

        >>> v = Vector(1, 2)
        >>> w = Vector(3, 4)
        >>> v * w
        Vector(3, 8)
        >>> v * 2
        Vector(2, 4)
        >>> 3.0 * v
        Vector(3.0, 6.0)

        """
        copy = self.copy()
        return copy.__imul__(other)

    __rmul__ = __mul__

    def scale(self, other):
        """Scale Vector by other (in-place).

        >>> v = Vector(1, 2)
        >>> w = Vector(3, 4)
        >>> v.scale(w)
        >>> v
        Vector(3, 8)
        >>> v.scale(0.5)
        >>> v
        Vector(1.5, 4.0)

        """
        self.__imul__(other)

    def __itruediv__(self, other):
        """v.__itruediv__(w) -> v /= w

        >>> v = Vector(2, 4)
        >>> w = Vector(4, 8)
        >>> v /= w
        >>> v
        Vector(0.5, 0.5)
        >>> v /= 2
        >>> v
        Vector(0.25, 0.25)

        """
        if self._hash is not None:
            raise ValueError('cannot divide Vector after hashing')
        if isinstance(other, Vector):
            self.x /= other.x
            self.y /= other.y
        else:
            self.x /= other
            self.y /= other
        return self

    def __truediv__(self, other):
        """v.__truediv__(w) -> v / w

        >>> v = Vector(1, 2)
        >>> w = Vector(3, 4)
        >>> w / v
        Vector(3.0, 2.0)
        >>> v / 2
        Vector(0.5, 1.0)

        """
        copy = self.copy()
        return copy.__itruediv__(other)

    def __neg__(self):
        """v.__neg__() -> -v

        >>> v = Vector(1, 2)
        >>> -v
        Vector(-1, -2)

        """
        # pylint: disable=invalid-unary-operand-type
        copy = self.copy()
        copy.x = -copy.x
        copy.y = -copy.y
        return copy

    def __abs__(self):
        """v.__abs__() -> abs(v)

        >>> v = Vector(3, 4)
        >>> abs(v)
        5.0

        """
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def rotate(self, angle):
        """Rotate Vector counter-clockwise by angle (in-place).

        >>> v = Vector(1, 2)
        >>> v.rotate(90)
        >>> v == Vector(-2, 1)
        True

        """
        if self._hash is not None:
            raise ValueError('cannot rotate Vector after hashing')
        radians = angle * math.pi / 180.0
        cosine = math.cos(radians)
        sine = math.sin(radians)
        x = self.x
        y = self.y
        self.x = x * cosine - y * sine
        self.y = y * cosine + x * sine

    def __repr__(self):
        """v.__repr__() -> repr(v)

        >>> v = Vector(1, 2)
        >>> repr(v)
        'Vector(1, 2)'

        """
        type_self = type(self)
        name = type_self.__name__
        return '{}({!r}, {!r})'.format(name, self.x, self.y)


ball = Vector(-200, -200)
speed = Vector(0, 0)
targets = []
score = 0


def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25


def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw(nb_hits):
    "Draw ball and targets."
    turtle.clear()

    for target in targets:
        turtle.goto(target.x, target.y)
        turtle.dot(20, 'blue')

    if inside(ball):
        turtle.goto(ball.x, ball.y)
        turtle.dot(6, 'red')

    update_score(nb_hits)
    turtle.update()


def update_score(nb_hits):
    global score
    try:
        for i in range(nb_hits):
            score = verhoogScore(score)
    except:
        print("Je functie verhoogScore() werkt niet correct!")
        exit(-2)
    turtle.goto(0, 175)
    turtle.pendown()
    try:
        my_string = scorebord(score)
        turtle.write(my_string, align='center', font=("Arial", 20, 'normal'))
    except TypeError:
        print("Je functie scorebord() maakt geen string aan! Denk aan str( ).")
        exit(-2)
    except:
        print("Je functie scorebord() werkt niet correct.")
        exit(-2)
    turtle.penup()


def move():
    "Move ball and targets."
    global score
    if random.randrange(40) == 0:
        try:
            y = positieVanDoelen()
            assert y in range(-150, 150)
            target = Vector(200, y)
        except AssertionError:
            print("Je functie positieVanDoelen() geeft een te groot of een te klein getal. Kijk nog eens goed na.")
            exit(-2)
        except:
            print("Je functie positieVanDoelen() werkt niet correct!")
            exit(-2)
        targets.append(target)

    for target in targets:
        try:
            target.x -= (snelheidVanDoelen() * 0.5 if snelheidVanDoelen() != 0 else 0.5)
        except:
            target.x -= 0.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    nb_hits = 0
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)
        else:
            nb_hits += 1

    draw(nb_hits)

    for target in targets:
        try:
            spelVoorbij(None)
        except:
            print("Je functie spelVoorbij() werkt niet goed.")
            exit(-2)
        if not inside(target):
            spelVoorbij("gedaan")
            return

    turtle.ontimer(move, 50)


if 'ja' in (input("Welkom bij Kanon! \n \n"
                  "Voordat je dit spelletje kan spelen, moet je eerst alle functies voltooien die in dit bestand staan. \n"
                  "Krijg je een foutmelding in de vorm van rode tekst? Lees dan eens de laatste lijn van de foutmelding om te \n"
                  "zien wat je foutdeed. Schrijf hier 'ja' als je deze uitleg gelezen hebt. --> ")).lower():

    turtle.setup(420, 420, 370, 0)
    verbergTurtle()
    if turtle.isvisible():
        print("Je moet je turtle verbergen met de functie verbergTurtle()!")
        exit(-2)
    turtle.up()
    turtle.tracer(False)
    turtle.onscreenclick(tap)
    move()
    turtle.done()
else:
    print("Lees bovenstaand bericht goed en herstart je spelletje!")
    exit(-2)