import pygame as pg
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