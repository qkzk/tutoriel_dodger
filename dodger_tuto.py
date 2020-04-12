from random import randint
import pgzrun

__doc__ = '''
titre :  {__title__}
auteur : {__author__}
date :   {__date__}

Simple jeu de reflexe où il faut éviter des ennemis qui descendent l'écran
'''
__title__ = 'Tutoriel dodger'
__author__ = 'qkzk'
__date__ = '2020/04/12'

TITLE = "Dodger"
WIDTH = 600
HEIGHT = 600
FICHIER_HIGH_SCORE = "high_score.txt"

CASE = 40
VITESSE_JOUEUR = CASE // 4
VITESSE_MECHANT = CASE // 20


def nouveau_joueur():
    return [WIDTH // (2 * CASE) * CASE,
            HEIGHT // (2 * CASE) * CASE, True]


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
    '''retourne un nouveau méchant. modifie le tableau transmis
    @param mechant: (list)
    @return : (list)
    '''
    mechant[0] = randint(0, (WIDTH - CASE) // CASE) * CASE
    mechant[1] = randint(-HEIGHT // CASE, -1) * CASE
    return mechant


def mechant_sorti_ecran(mechant):
    '''
    vrai si l'ordonnée est supérieure à la taille de l'écran
    @param mechant: (list)
    @return (list)
    '''
    return mechant[1] >= HEIGHT


def collision(joueur, mechant):
    '''
    vrai si les deux objets se touchent
    @param joueur, mechant: (list)
    @return: (bool)
    '''
    return Rect((joueur[0], joueur[1]), (CASE, CASE)).colliderect(
        Rect((mechant[0], mechant[1]), (CASE, CASE)))


def deplacer_joueur(joueur):
    '''
    retourne un nouveau tableau du joueur avec ses coordonnées modifiées
    s'il a enfoncé une touche
    @param joueur: (list)
    @return: (list)
    '''
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
    '''Ecrit le texte YOU DIED à l'écran'''
    screen.draw.text("YOU DIED",
                     midtop=(WIDTH // 2, HEIGHT // 2 - 60),
                     owidth=1,
                     ocolor=(180, 50, 50),
                     color=(100, 0, 0),
                     fontsize=120)


def ecrire_score(score, x):
    '''Ecrit le score en haut de l'écran, à l'abscisse transmise
    @param score: (int) la valeur à écrire
    @param x: (int) son ordonnée
    '''
    screen.draw.text(str(score),
                     topleft=(x, CASE),
                     color="darkorange",
                     fontsize=40)


def sauvegarder_highscore(high_score):
    '''
    sauvegarde le high_score dans un fichier
    @param high_score: (int)
    @SE: écrit dans le fichier FICHIER_HIGH_SCORE
    '''
    with open(FICHIER_HIGH_SCORE, 'w') as f:
        f.write(str(high_score))


def lire_highscore():
    '''
    lit le high_score dans un fichier
    @return: (int)
    '''
    with open(FICHIER_HIGH_SCORE) as f:
        data = f.read()
    try:
        data = int(data)
    except Exception as e:
        data = 0
    return data


def reset():
    joueur = nouveau_joueur()
    mechant_liste = [nouveau_mechant([0, 0]) for _ in range(20)]
    score = 0
    return joueur, mechant_liste, score


def update():
    '''
    met à jour les éléments
    SE. modifie les variables globales
    joueur, score, high_score, mechant_liste
    '''
    global joueur, score, high_score, mechant_liste
    if keyboard["escape"]:
        # on arrête le jeu

        exit()
    # déplacement du joueur
    if joueur[2]:
        joueur = deplacer_joueur(joueur)

        # modification des machants
        for mechant in mechant_liste:
            # deplacements
            mechant = avancer_mechant(mechant)

            if mechant_sorti_ecran(mechant):
                # reset du méchant
                mechant = nouveau_mechant(mechant)
                # le score augmente
                score += 1
                if score >= high_score:
                    # on enregistre le high_score
                    high_score = score
                    sauvegarder_highscore(high_score)

            if collision(joueur, mechant):
                # collision => mort
                joueur[2] = False

    else:
        if keyboard["return"]:
            # on rejoue
            joueur, mechant_liste, score = reset()


def draw():
    '''dessine 60x par seconde les éléments du jeu'''
    global score, high_score
    if joueur[2]:
        # si le joueur est vivant
        screen.fill((51, 51, 51))  # le fond en gris foncé

        for mechant in mechant_liste:
            # dessine chaque méchant
            dessiner_perso(*mechant, "deepskyblue")

        # dessin du joueur
        dessiner_perso(joueur[0], joueur[1], "darkorange")
    else:
        # mise en scène dramatique de la mort
        screen.fill("black")
        ecrire_mort()

    # dans tous les cas on écrit le score
    ecrire_score(score, CASE)
    ecrire_score(high_score, WIDTH - 2 * CASE)


# on crée les variables
high_score = lire_highscore()
joueur, mechant_liste, score = reset()
# on lance le jeu
pgzrun.go()
