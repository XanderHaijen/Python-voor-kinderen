import collections.abc as collections
import math
import random
import turtle

# ------------------------ HIER BEGINT HET EERSTE DEEL VAN DE OPDRACHT-----------------------------
# Vul hieronder de functies aan, zodat ze doen wat gevraagd wordt in de opgave.


def scorebord(score, level):
    """
    Maak een string met een scorebord en gebruik een return.
    Een scorebord moet er als volgt uitzien:

                SCORE : 50    LEVEL 4

    Tip: wil je een getal in een string gebruiken, moet je gebruik maken van str (  )
    """
    return ""


def binnenin(punt):
    """
    Deze functie geeft waar (True) terug als een punt binnenin het scherm ligt. Een punt ligt binnenin het scherm
    als de waarde ervan tussen -200 en 200 ligt. Is dat niet het geval, geeft de functie onwaar (False) terug. Gebruik
    een return.
    """
    return True, False



def kleur(levend):
    """
    Zolang je nog leeft, ziet je balletje groen. Als je een bal raakt, ga je dood en wordt het balletje rood. Deze functie
    geeft de juiste kleur terug. Als levend dus waar is (True), dan geeft de functie 'groen' terug, anders 'rood'.
    """
    return ""


def willekeurig_getal():
    """
    Geef een willekeurige integer terug tussen -199 en 199. Gebruik hiervoor een return.
    """
    return 0


# ------------------------------------ HIER EINDIGT HET EERSTE DEEL VAN DE OPDRACHT------------------------------------

# ------------------------------------ HIER BEGINT HET TWEEDE DEEL VAN DE OPDRACHT ------------------------------------
# Let op: dit is een moeilijke opdracht. Doe dit enkel als je Python goed begrijpt.


# Vul hieronder de functie aan, zodat ze doet wat gevraagd wordt in de opgave.


def maakBal(hoogte, ballen):
    """
    Deze functie maakt een bal aan. In Python wordt een bal voorgesteld door een "Vector". Wat dit precies is, is niet
    zo belangrijk. Je kunt een nieuwe vector maken, met de naam "bal" op de volgende manier
    bal = Vector(breedte, hoogte). Bijvoorbeeld

    >> bal = Vector(250, 50)

    maakt een bal op 250 pixels rechts van het midden en 50 pixels boven het midden.

    Nadat je een bal hebt aangemaakt, moet je deze toevoegen aan de lijst met ballen. Die lijst heet gewoon "ballen".
    Een bal toevoegen doe je met "append", wat Engels is voor "eraan toevoegen". Bijvoorbeeld

    >> lijst.append((nieuw_stukje,extra_info))

    voegt een nieuw stukje toe aan de lijst met naam "lijst".

    OPDRACHT: Zorg ervoor dat de ballen verschillende groottes hebben. De maximale grootte is 40 en de minimale
    grootte is 5.
    """
    bal = Vector(199, hoogte)
    grootte = 20
    ballen.append((bal, 20))  # 20 is de grootte van de bal


def tekenBal(ballen):
    """
    Nu je ervoor gezorgd hebt dat ballen een verschillende grootte hebben, gaan we ook zorgen dat het programma
    de ballen tekent met de juiste grootte.
    OPDRACHT: zorg ervoor dat de ballen getekend worden met de juiste grootte

    TIP: 'for __ in ballen' betekent dat je iets doet voor alle ballen.
    """
    for bal, grootte in ballen:
        turtle.goto(bal.x, bal.y)
        turtle.dot(20, "black")  # 20 is de grootte van de bal


# ------------------------------------ HIER EINDIGT DE OPDRACHT -------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# -------------------------------                                         ---------------------------------------------
# -------------------------------     PAS HIERONDER GEEN CODE AAN !!      ---------------------------------------------
# -------------------------------                                         ---------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------


# klasse vector overgenomen uit package freegames -> utils -> Vector
class Vector(collections.Sequence):
    """Two-dimensional vector.

    Vectors can be modified in-place.

    >>> v = Vector(0, 1)
    >>> v.move(1)
    >>> v
    vector(1, 2)
    >>> v.rotate(90)
    >>> v
    vector(-2.0, 1.0)

    """
    # pylint: disable=invalid-name
    PRECISION = 6

    __slots__ = ('_x', '_y', '_hash')

    def __init__(self, x, y):
        """Initialize vector with coordinates: x, y.

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
        """X-axis component of vector.

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
        """Y-axis component of vector.

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
        """Return copy of vector.

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
        vector(4, 6)
        >>> v += 1
        >>> v
        vector(5, 7)

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
        vector(4, 6)
        >>> v + 1
        vector(2, 3)
        >>> 2.0 + v
        vector(3.0, 4.0)

        """
        copy = self.copy()
        return copy.__iadd__(other)

    __radd__ = __add__

    def move(self, other):
        """Move vector by other (in-place).

        >>> v = Vector(1, 2)
        >>> w = Vector(3, 4)
        >>> v.move(w)
        >>> v
        vector(4, 6)
        >>> v.move(3)
        >>> v
        vector(7, 9)

        """
        self.__iadd__(other)

    def __isub__(self, other):
        """v.__isub__(w) -> v -= w

        >>> v = Vector(1, 2)
        >>> w = Vector(3, 4)
        >>> v -= w
        >>> v
        vector(-2, -2)
        >>> v -= 1
        >>> v
        vector(-3, -3)

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
        vector(-2, -2)
        >>> v - 1
        vector(0, 1)

        """
        copy = self.copy()
        return copy.__isub__(other)

    def __imul__(self, other):
        """v.__imul__(w) -> v *= w

        >>> v = Vector(1, 2)
        >>> w = Vector(3, 4)
        >>> v *= w
        >>> v
        vector(3, 8)
        >>> v *= 2
        >>> v
        vector(6, 16)

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
        vector(3, 8)
        >>> v * 2
        vector(2, 4)
        >>> 3.0 * v
        vector(3.0, 6.0)

        """
        copy = self.copy()
        return copy.__imul__(other)

    __rmul__ = __mul__

    def scale(self, other):
        """Scale vector by other (in-place).

        >>> v = Vector(1, 2)
        >>> w = Vector(3, 4)
        >>> v.scale(w)
        >>> v
        vector(3, 8)
        >>> v.scale(0.5)
        >>> v
        vector(1.5, 4.0)

        """
        self.__imul__(other)

    def __itruediv__(self, other):
        """v.__itruediv__(w) -> v /= w

        >>> v = Vector(2, 4)
        >>> w = Vector(4, 8)
        >>> v /= w
        >>> v
        vector(0.5, 0.5)
        >>> v /= 2
        >>> v
        vector(0.25, 0.25)

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
        vector(3.0, 2.0)
        >>> v / 2
        vector(0.5, 1.0)

        """
        copy = self.copy()
        return copy.__itruediv__(other)

    def __neg__(self):
        """v.__neg__() -> -v

        >>> v = Vector(1, 2)
        >>> -v
        vector(-1, -2)

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
        """Rotate vector counter-clockwise by angle (in-place).

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
        'vector(1, 2)'

        """
        type_self = type(self)
        name = type_self.__name__
        return '{}({!r}, {!r})'.format(name, self.x, self.y)

bird = Vector(0, 0)
balls = []


def up(x, y):
    "Move bird up in response to screen tap."
    up = Vector(0, 30)
    bird.move(up)

def inside(point):
    try:
        assert binnenin(point.x) == (-200 < point.x < 200)
        assert binnenin(point.y) == (-200 < point.y < 200)
        return binnenin(point.x) and binnenin(point.y)
    except AssertionError:
        print("Je functie binnenin( ) geeft het verkeerde resultaat. Kijk nog eens goed na.")
        exit(-2)
    except TypeError:
        print("Je functie binnenin( ) geeft geen waar of onwaar (True / False) terug. Kijk nog eens na.")
        exit(-2)
    except:
        print("Je functie binnenin( ) werkt niet goed. Kijk nog eens goed na.")
        exit(-2)


def draw(alive, score, level):
    "Draw screen objects."
    turtle.clear()

    turtle.goto(0, 180)
    turtle.showturtle()

    try:
        turtle.write(scorebord(score, level), align='center', font=("Calibri", 15, "bold"))
    except TypeError:
        print("Je functie scorebord( ) geeft geen string terug.")
        exit(-2)
    except:
        print("Je functie scorebord( ) werkt niet goed.")
        exit(-2)

    turtle.hideturtle()
    turtle.goto(bird.x, bird.y)

    try:
        color = kleur(alive).lower()
        assert color == "groen" if alive else "rood"
        color = "green" if color == "groen" else "red"
        turtle.dot(10, color)

    except AssertionError:
        print("Je functie kleur( ) geeft een verkeerde kleur, of helemaal geen kleur terug. Kijk nog eens na.")
        exit(-2)
    except TypeError:
        print("Je functie kleur( ) geeft geen string terug!")
        exit(-2)
    except:
        print("Je functie kleur( ) werkt niet goed.")
        exit(-2)
    if enable:
        try:
            tekenBal(balls)
        except:
            print("Je functie tekenBal() werkt niet goed.")
            exit(-2)
    else:
        for ball, size in balls:
            turtle.goto(ball.x, ball.y)
            turtle.dot(20, 'black')

    turtle.update()


def move():
    "Update object positions."
    turtle.listen()
    turtle.onkey(up, "Up")
    bird.y -= 5

    global enable
    global score
    global ball_speed
    global level

    for ball, _ in balls:
        ball.x -= ball_speed

    if random.randrange(10 // level) == 0:
        try:
            y = willekeurig_getal()
            assert y in range(-200,200)
        except AssertionError:
            print("Je functie willekeurig_getal() geeft een getal terug dat te groot of te klein is.")
            exit(-2)
        except TypeError:
            print("Je functie willekeurig_getal() geeft geen getal terug.")
            exit(-2)
        except:
            print("Je functie willekeurig_getal() werkt niet goed.")
            exit(-2)

        if enable:
            try:
                bal = maakBal(y, balls)
            except:
                print("Je functie maakBal() werkt niet goed. Kijk nog eens na!")
                exit(-2)
        else:
            size = 30
            ball = Vector(199, y)
            balls.append((ball, size))

    while len(balls) > 0 and not inside(balls[0][0]):
        balls.pop(0)
        score += 1
        if score % 15 == 0 and score != 0:
            ball_speed += 1.5
            level += 1

    if not inside(bird):
        draw(False, score, level)
        return

    for ball, size in balls:
        if abs(ball - bird) < size // 2:
            draw(False, score, level)
            return

    draw(True, score, level)
    turtle.ontimer(move, 50)

if 'ja' not in (input("Welkom bij Flappy Bird! \n \n"
                  "Voordat je dit spelletje kan spelen, moet je eerst alle functies voltooien die in dit bestand staan. \n"
                  "Krijg je een foutmelding in de vorm van rode tekst? Lees dan eens de laatste lijn van de foutmelding om te \n"
                  "zien wat je foutdeed. Schrijf hier 'ja' als je deze uitleg gelezen hebt. --> ")).lower():
    exit(-2)
else:
    print("")
    if 'ja' in (input("Heb je ook het tweede deel van de opdracht gemaakt? Ja / Nee ---> ")).lower():
        enable = True
    else:
        enable = False

score = 0
ball_speed = 3
level = 1

turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.up()
turtle.tracer(False)
turtle.onscreenclick(up)
move()
turtle.done()