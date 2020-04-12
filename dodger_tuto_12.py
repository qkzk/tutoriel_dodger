from random import randint
import pgzrun

TITLE = "Dodger"
WIDTH = 600
HEIGHT = 600

CASE = 40
VITESSE_JOUEUR = CASE // 4
VITESSE_MECHANT = CASE // 20


def dessiner_perso(x, y, couleur):
    '''
    Dessine un personnage à l'écran

    @param x: (int) l'abscisse
    @param y: (int) l'ordonnée
    @param couleur: (int, int, int) ou (str) la couleur

    Utilise
    filled_rect(Rect, (r, g, b))
    Rect((x, y), (l, h))
    couleur (r, g, b) ou un nom de couleur html'''
    screen.draw.filled_rect(Rect((x, y), (CASE, CASE)), couleur)


def avancer_mechant(mechant):
    '''
    Retourne le nouveau tableau d'un méchant, son second élément ayant augmenté
    @param mechant: (list)
    @return (list)
    '''
    mechant[1] += VITESSE_MECHANT
    return mechant


def nouveau_mechant(mechant):
    mechant[0] = randint(0, (WIDTH - CASE) // CASE) * CASE
    mechant[1] = randint(-HEIGHT // CASE, -1) * CASE
    return mechant


def mechant_sorti_ecran(mechant):
    return mechant[1] >= HEIGHT


def collision(joueur, mechant):
    return Rect((joueur[0], joueur[1]), (CASE, CASE)).colliderect(
        Rect((mechant[0], mechant[1]), (CASE, CASE)))


def deplacer_joueur(joueur):
    x = joueur[0]
    y = joueur[1]
    vivant = joueur[2]
    if keyboard["left"] and x >= 0:
        x -= VITESSE_JOUEUR
    if keyboard["right"] and x <= WIDTH - CASE:
        x += VITESSE_JOUEUR
    if keyboard["up"] and y >= 0:
        y -= VITESSE_JOUEUR
    if keyboard["down"] and y <= HEIGHT - CASE:
        y += VITESSE_JOUEUR
    return [x, y, vivant]


def ecrire_mort():
    screen.draw.text("YOU DIED",
                     midtop=(WIDTH // 2, HEIGHT // 2 - 60),
                     owidth=1,
                     ocolor=(180, 50, 50),
                     color=(100, 0, 0),
                     fontsize=120)


def ecrire_score(score, x):
    screen.draw.text(str(score),
                     topleft=(x, CASE),
                     color="darkorange",
                     fontsize=40)


def update():
    global joueur, score, high_score
    if keyboard["escape"]:
        exit()
    # déplacement du joueur
    if joueur[2]:
        joueur = deplacer_joueur(joueur)

        for mechant in mechant_liste:
            mechant = avancer_mechant(mechant)

            if mechant_sorti_ecran(mechant):
                mechant = nouveau_mechant(mechant)
                score += 1
                if score >= high_score:
                    high_score = score

            if collision(joueur, mechant):
                joueur[2] = False

    else:
        score = 0
        if keyboard["return"]:
            for mechant in mechant_liste:
                mechant = nouveau_mechant(mechant)
            joueur = [WIDTH // (2 * CASE) * CASE, HEIGHT // (2 * CASE) * CASE, True]


def draw():
    global score, high_score
    if joueur[2]:
        screen.fill("darkgrey")

        for mechant in mechant_liste:
            dessiner_perso(*mechant, "darkslateblue")

        dessiner_perso(joueur[0], joueur[1], "darkorange")
        ecrire_score(score, CASE)
        ecrire_score(high_score, WIDTH - 2 * CASE)
    else:
        screen.fill("black")
        ecrire_mort()


mechant_liste = [nouveau_mechant([0, 0]) for _ in range(20)]
joueur = [WIDTH // (2 * CASE) * CASE, HEIGHT // (2 * CASE) * CASE, True]
score = 0
high_score = 0
pgzrun.go()
