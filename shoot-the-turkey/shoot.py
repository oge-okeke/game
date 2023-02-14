WIDTH= 600
HEIGHT=600
BACKGROUND_COLOR= (173,216,230)
score=0
from random import randint
import time
turkey= Actor("turkey")
game_over = False

start_time=time.time()
elapsed_time=0
time_limit=5

def draw():
    if game_over:
        screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize=60)

    else:
        screen.fill("green")
        screen.clear()
        turkey.draw()
        screen.draw.text("Score: " + str(score), color="blue", topleft=(10, 10))

def update():
    elapsed_time = time.time() - start_time
    if elapsed_time>time_limit:
        global game_over
        game_over = True

def place_turkey():
    turkey.x=randint(10,600)
    turkey.y=randint(10,600)

def on_mouse_down(pos):
    if turkey.collidepoint(pos):
        print("Good shot!")
        global score
        score+=1
        place_turkey()
    else:
        print ("You missed lol!")
        global game_over
        game_over = True








