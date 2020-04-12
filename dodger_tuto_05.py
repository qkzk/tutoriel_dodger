from random import randint
import pgzrun

TITLE = "Dodger"
WIDTH = 600
HEIGHT = 600

CASE = 50
VITESSE = 10
x = WIDTH // 2
y = HEIGHT // 2

mechant_pos = [randint(0, WIDTH - CASE), 0]
mechant_liste = [mechant_pos]


def dessiner_perso(x, y, couleur):
    '''filled_rect(Rect, (r, g, b))
    Rect((x, y), (l, h))
    couleur (r, g, b) ou un nom de couleur html'''
    screen.draw.filled_rect(
        Rect(
            (x, y),
            (CASE, CASE)
        ),
        couleur)


def avancer_mechants(mechant_liste):
    for mechant in mechant_liste:
        mechant[1] += VITESSE


def update():
    global x, y, mechant_liste
    if keyboard["escape"]:
        exit()
    # déplacement du joueur
    if keyboard["left"] and x >= 0:
        x -= VITESSE
    if keyboard["right"] and x <= WIDTH - CASE:
        x += VITESSE
    if keyboard["up"] and y >= 0:
        y -= VITESSE
    if keyboard["down"] and y <= HEIGHT - CASE:
        y += VITESSE

    avancer_mechants(mechant_liste)


def draw():
    global x, y
    screen.fill("darkgrey")

    dessiner_perso(x, y, "orange")

    for mechant in mechant_liste:
        dessiner_perso(*mechant, "darkslateblue")


pgzrun.go()
