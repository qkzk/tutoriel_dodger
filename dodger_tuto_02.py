import pgzrun

TITLE = "Dodger"
WIDTH = 600
HEIGHT = 600


def update():
    pass


def draw():
    screen.fill("grey")
    # filled_rect(Rect, (r, g, b))
    # Rect((x, y), (l, h))
    # couleur (r, g, b) ou un nom de couleur html
    screen.draw.filled_rect(
        Rect(
            (WIDTH // 2, HEIGHT // 2),
            (50, 50)),
        "orange")


pgzrun.go()
