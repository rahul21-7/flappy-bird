import pygame
import random

pygame.init()

width = 600
height = 600

bird_radius = 40

bird_pos = [300,300]

pipe_width = 100

top_pipe_x = width - width/3

top_pipe_y = 0

bottom_pipe_x = top_pipe_x

top_pipe_height = 200

bottom_pipe_y = (top_pipe_height + bird_radius*2 +200)

bottom_pipe_height = height - bottom_pipe_y

obstacles = {
    'top_pipe_1' : pygame.Rect(top_pipe_x,top_pipe_y,pipe_width,top_pipe_height),
    'bottom_pipe_1' : pygame.Rect(bottom_pipe_x,bottom_pipe_y,pipe_width,bottom_pipe_height),
    'top_pipe_2' : pygame.Rect((top_pipe_x + width/2),(top_pipe_y - height/4),pipe_width,(top_pipe_height)),
    'bottom_pipe_2' : pygame.Rect((bottom_pipe_x + width/2),(bottom_pipe_y - height/4),pipe_width,(bottom_pipe_height + height/4))

}

first_pipe = True

def change_pipes_positions1():
    global top_pipe_x,bottom_pipe_x,obstacles

    top_pipe_x = width - pipe_width/2
    bottom_pipe_x = width - pipe_width/2

    height_change = random.randint(0,height//4)

    obstacles['top_pipe_1'] = pygame.Rect(top_pipe_x + width/2,top_pipe_y - height_change,pipe_width,top_pipe_height)
    obstacles['bottom_pipe_1'] = pygame.Rect(bottom_pipe_x + width/2,bottom_pipe_y - height_change,pipe_width,bottom_pipe_height + height_change)
    return

def change_pipes_positions2():
    global top_pipe_x,bottom_pipe_x,obstacles

    top_pipe_x = width - pipe_width/2
    bottom_pipe_x = width - pipe_width/2

    height_change = random.randint(0,height//4)
    
    obstacles['top_pipe_2'] = pygame.Rect((top_pipe_x + width/2),(top_pipe_y - height_change),pipe_width,(top_pipe_height))
    obstacles['bottom_pipe_2'] = pygame.Rect((bottom_pipe_x + width/2),(bottom_pipe_y - height_change),pipe_width,(bottom_pipe_height + height_change))

