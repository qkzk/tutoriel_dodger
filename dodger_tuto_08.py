from random import randint
import pgzrun

TITLE = "Dodger"
WIDTH = 600
HEIGHT = 600

CASE = 50
VITESSE_JOUEUR = 10
VITESSE_MECHANT = 3
x = WIDTH // 2
y = HEIGHT // 2


def dessiner_perso(x, y, couleur):
    '''filled_rect(Rect, (r, g, b))
    Rect((x, y), (l, h))
    couleur (r, g, b) ou un nom de couleur html'''
    screen.draw.filled_rect(Rect((x, y), (CASE, CASE)), couleur)


def avancer_mechant(mechant):
    mechant[1] += VITESSE_MECHANT
    return mechant


def nouveau_mechant(mechant):
    mechant[0] = randint(0, WIDTH - CASE)
    mechant[1] = 0
    return mechant


def mechant_sorti_ecran(mechant):
    return mechant[1] >= HEIGHT


def deplacer_joueur(joueur):
    x = joueur[0]
    y = joueur[1]
    if keyboard["left"] and x >= 0:
        x -= VITESSE_JOUEUR
    if keyboard["right"] and x <= WIDTH - CASE:
        x += VITESSE_JOUEUR
    if keyboard["up"] and y >= 0:
        y -= VITESSE_JOUEUR
    if keyboard["down"] and y <= HEIGHT - CASE:
        y += VITESSE_JOUEUR
    return (x, y)


def update():
    global joueur
    if keyboard["escape"]:
        exit()
    # déplacement du joueur
    joueur = deplacer_joueur(joueur)

    for mechant in mechant_liste:
        mechant = avancer_mechant(mechant)

        if mechant_sorti_ecran(mechant):
            mechant = nouveau_mechant(mechant)


def draw():
    screen.fill("darkgrey")

    dessiner_perso(joueur[0], joueur[1], "orange")

    for mechant in mechant_liste:
        dessiner_perso(*mechant, "darkslateblue")


mechant_liste = [nouveau_mechant([0, 0]) for _ in range(4)]
joueur = [x, y]
pgzrun.go()
