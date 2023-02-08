person = Actor ('gamergirl')
person.pos = 75, 150
WIDTH=500
HEIGHT=300
BACKGROUND_COLOR= (173,216,230)

def draw():
    screen.fill(BACKGROUND_COLOR)
    person.draw()


def update():
        person.left = person.left + 2
        if person.left > 500:
            person.right= 0
