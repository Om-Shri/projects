import pygame as pg
from pygame.locals import *
import time 
import random

pg.init()
red = "#C10505"
blue = "#1D69DC"
gray = "#B1B1B122"
green = "#0ED21ECE"

win_width = 600
win_height = 400

window = pg.display.set_mode((win_width,win_height))
pg.display.set_caption("SNAKE GAME")
time.sleep(2)
 
snake = 10
snake_speed = 15

clock = pg.time.Clock()

font_style = pg.font.SysFont("calibri",26)
score_font = pg.font.SysFont("comicsansms",30)

def user_score(score):
    number = score_font.render("score :"+str(score),True,red)
    window.blit(number,[0,0])

def game_snake(snake,snake_length_list):
    for x in snake_length_list:
        pg.draw.rect(window,green,[x[0],x[1],snake,snake])
    

def message(msg):
    msg = font_style.render(msg,True,red)
    window.blit(msg,[win_width/15, win_height/3])

def game_loop():
    gameOver = False
    gameClose = False

    x1 = win_width/2
    y1 = win_height/2

    x1_change = 0
    y1_change = 0

    snake_length_list = []
    snake_length = 1

    foodx = round(random.randrange(0,win_width - snake)/10.0)*10.0
    foody = round(random.randrange(0,win_height - snake)/10.0)*10.0

    while not gameOver :

        while gameClose == True:
            window.fill(gray)
            message("You lost press 'p' for play and 'Q' for quit.")
            user_score(snake_length -1)
            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        gameOver = True
                        gameClose = False
                    if event.key == pg.K_p:
                        game_loop()

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x1_change = -snake
                    y1_change = 0
                if event.key == pg.K_RIGHT:
                    x1_change = snake
                    y1_change = 0
                if event.key == pg.K_UP:
                    x1_change = 0
                    y1_change = -snake
                if event.key == pg.K_DOWN:
                    x1_change = 0
                    y1_change = snake

        if x1 > win_width or x1<0 or y1 > win_height or y1<0:
            gameClose = True

        x1 += x1_change
        y1 += y1_change
        window.fill(gray)
        pg.draw.rect(window,blue,[foodx,foody,snake,snake])
        snake_size =[]
        snake_size.append(x1)
        snake_size.append(y1)
        snake_length_list.append(snake_size)
        if len(snake_length_list) > snake_length:
            del snake_length_list[0]

        game_snake(snake,snake_length_list)
        user_score(snake_length-1)
        pg.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0,win_width - snake)/10.0)*10.0
            foody = round(random.randrange(0,win_height - snake)/10.0)*10.0
            snake_length += 1

        clock.tick(snake_speed)

    pg.quit()
    quit()
game_loop()