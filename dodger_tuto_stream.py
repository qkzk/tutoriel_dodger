'''
01 update, draw, remplir l'écran, constantes
02 dessiner un rectangle
03 draw fct dessiner joueur, update gestion touche : déplacer sortie avec escape
04 liste de mechants, dessiner,
05 fct avancer_mechants, fct deplacer joueur
06 fct nouveau mechant (un seul), liste de nouveau mechants
07 mechant sorti écran,
08 si mechant sorti, reset
09 collision 2 rectangle -> bool, ecrire la mort à l'écran
10 rejouer : distinguer mort vivant (nlle varialbe pour joueur)
11 score + high_score

pas fait. !!!!
12 sauvegarder/lire high score ds un fichier, chgt couleur, docs
'''
import pgzrun
from random import randint

TITLE = "dodger"
WIDTH = 600
HEIGHT = 600
CASE = 50
TAILLE_MAX = WIDTH // CASE


VITESSE_MECHANT = 1  # 5
VITESSE_JOUEUR = 10
couleur_joueur = (200, 20, 100)


def reset():
    x = CASE * 2
    y = CASE * 4
    vivant = True
    mechant_liste = []
    for _ in range(30):
        mechant_liste.append(creer_mechant([0, 0]))
    score = 0
    return x, y, vivant, mechant_liste, score


def creer_mechant(mechant):
    mechant[0] = CASE * randint(0, TAILLE_MAX)
    mechant[1] = -CASE * randint(0, TAILLE_MAX)
    return mechant


def avancer_mechants(mechant_liste):
    for mechant in mechant_liste:
        avancer_mechant(mechant)


def avancer_mechant(mechant):
    global score
    mechant[1] = mechant[1] + VITESSE_MECHANT
    if mechant[1] >= HEIGHT:
        score = score + 1
        mechant = creer_mechant(mechant)
    return score
    # mechant = creer_mechant(mechant)


def collision(x, y, mechant):
    '''test if two rectangles overlap
    colliderect(Rect) -> bool
    Returns true if any portion of either rectangle
    overlap (except the top+bottom or left+right edges).
    '''
    return Rect((x, y), (CASE, CASE)).colliderect(
        Rect((mechant[0], mechant[1]), (CASE, CASE))
    )


def toujours_vivant(x, y, mechant_liste):
    vivant = True
    for mechant in mechant_liste:
        if collision(x, y, mechant):
            vivant = False
    return vivant


def dessiner_perso(absc, ord, couleur):
    screen.draw.filled_rect(Rect((absc, ord), (CASE, CASE)),
                            couleur)


def deplacer_joueur(x, y):
    if keyboard["up"] and y > 0:
        y = y - VITESSE_JOUEUR
    if keyboard["down"] and y < HEIGHT - CASE:
        y = y + VITESSE_JOUEUR
    if keyboard["right"] and x < WIDTH - CASE:
        x = x + VITESSE_JOUEUR
    if keyboard["left"] and x > 0:
        x = x - VITESSE_JOUEUR
    return x, y


def ecrire_mort():
    screen.draw.text("MORT",
                     (WIDTH // 2 - 100, HEIGHT // 2 - 50),
                     color='red',
                     shadow=(1, 1),
                     scolor='orange',
                     fontsize=100)


def update():
    global x, y, vivant, score, high_score
    global mechant_liste
    if keyboard["escape"]:
        exit()

    if vivant:
        x, y = deplacer_joueur(x, y)

        avancer_mechants(mechant_liste)

    if not toujours_vivant(x, y, mechant_liste):
        vivant = False

    if not vivant and keyboard["return"]:
        x, y, vivant, mechant_liste, score = reset()

    if score > high_score:
        high_score = score


def draw():
    if vivant:
        screen.fill('grey')
        for mechant in mechant_liste:
            dessiner_perso(mechant[0], mechant[1], "darkgreen")

        dessiner_perso(x, y, couleur_joueur)
    else:
        screen.fill('black')
        ecrire_mort()

    # interface en dernier
    screen.draw.text(str(score),
                     (CASE, CASE),
                     color=couleur_joueur,
                     fontsize=50)
    screen.draw.text(str(high_score),
                     (WIDTH - 2 * CASE, CASE),
                     color=couleur_joueur,
                     fontsize=50)


high_score = 0
x, y, vivant, mechant_liste, score = reset()
pgzrun.go()
