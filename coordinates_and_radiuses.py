import pygame

pygame.init()

width = 600
height = 600

bird_radius = 40

bird_pos = [300,300]

pipe_width = 100

top_pipe_x = width/2

top_pipe_y = 0

bottom_pipe_x = top_pipe_x

top_pipe_height = 200

bottom_pipe_y = (top_pipe_height + bird_radius*2 +200)

bottom_pipe_height = height - bottom_pipe_y
# top_pipe = pygame.Rect(top_pipe_x,top_pipe_y,100,200)

obstacles = {
    'top_pipe_1' : pygame.Rect(top_pipe_x,top_pipe_y,pipe_width,top_pipe_height),
    'bottom_pipe_1' : pygame.Rect(bottom_pipe_x,bottom_pipe_y,pipe_width,bottom_pipe_height),
    'top_pipe_2' : pygame.Rect((top_pipe_x + width/2),(top_pipe_y - height/4),pipe_width,(top_pipe_height)),
    'bottom_pipe_2' : pygame.Rect((bottom_pipe_x + width/2),(bottom_pipe_y - height/4),pipe_width,(bottom_pipe_height + height/4))

}

def change_pipes_positions():
    global top_pipe_x,bottom_pipe_x,obstacles

    top_pipe_x = width - pipe_width/2
    bottom_pipe_x = width - pipe_width/2

    obstacles = {
    'top_pipe_1' : pygame.Rect(top_pipe_x,top_pipe_y,pipe_width,top_pipe_height),
    'bottom_pipe_1' : pygame.Rect(bottom_pipe_x,bottom_pipe_y,pipe_width,bottom_pipe_height),
    'top_pipe_2' : pygame.Rect((top_pipe_x + width/2),(top_pipe_y - height/4),pipe_width,(top_pipe_height)),
    'bottom_pipe_2' : pygame.Rect((bottom_pipe_x + width/2),(bottom_pipe_y - height/4),pipe_width,(bottom_pipe_height + height/4))
}



# bird_rect = {
#     "left" : bird_pos[0] - bird_radius
#     ""
# }