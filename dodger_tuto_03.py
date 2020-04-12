import pgzrun

TITLE = "Dodger"
WIDTH = 600
HEIGHT = 600

CASE = 50
VITESSE_JOUEUR = 10
x = WIDTH // 2
y = HEIGHT // 2


def dessiner_joueur(x, y):
    '''filled_rect(Rect, (r, g, b))
    Rect((x, y), (l, h))
    couleur (r, g, b) ou un nom de couleur html'''
    screen.draw.filled_rect(
        Rect(
            (x, y),
            (CASE, CASE)
        ),
        "orange")


def update():
    global x, y

    if keyboard["left"]:
        x -= VITESSE_JOUEUR
    if keyboard["right"]:
        x += VITESSE_JOUEUR
    if keyboard["up"]:
        y -= VITESSE_JOUEUR
    if keyboard["down"]:
        y += VITESSE_JOUEUR


def draw():
    global x, y
    screen.fill("grey")

    dessiner_joueur(x, y)


pgzrun.go()
