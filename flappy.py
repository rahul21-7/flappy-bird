import pygame
import coordinates_and_radiuses as coord
import random

pygame.init()

screen = pygame.display.set_mode((coord.width,coord.height))
clock = pygame.time.Clock()

bird_surface = pygame.Surface((coord.bird_radius*2,coord.bird_radius*2))

pygame.draw.circle(bird_surface,'Red',(coord.bird_radius,coord.bird_radius),coord.bird_radius)

bird_rect = pygame.Rect(coord.bird_pos[0] - coord.bird_radius,coord.bird_pos[1] - coord.bird_radius,coord.bird_radius*2,coord.bird_radius*2)
bird_vel = [2,0]
bird_acc = [0,0.5]

#defeat
font = pygame.font.Font(None, 36)
lost_text = font.render('GAME LOST',True, 'White')
lost_flag = False
def game_lost():
    screen.blit(lost_text, (coord.width/3,coord.height/2))
    pygame.display.update()
    bird_acc[0] = 0
    bird_acc[1] = 0
    bird_vel[0] = 0
    bird_vel[1] = 0

def gravity_and_movements():
    bird_vel[0] += bird_acc[0]
    bird_vel[1] += bird_acc[1]
    # coord.bird_pos[0] += bird_vel[0]
    coord.bird_pos[1] += bird_vel[1]
    return


running = True
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = not running
    
    gravity_and_movements()
    bird_rect.topleft = coord.bird_pos[0] - coord.bird_radius,coord.bird_pos[1] - coord.bird_radius

    screen.fill('Black')

    mouse = pygame.mouse.get_pressed()

    if(mouse[0] or mouse[2]):
        bird_vel[1] = 0
        bird_vel[1] = -5
    
    if(coord.bird_pos[1] >= coord.height or coord.bird_pos[1] <= coord.bird_radius):
        game_lost()
        continue

    for name,rect in coord.obstacles.items():
        pygame.draw.rect(screen,'Green',rect)
        # pygame.draw.rect(screen,'Green',coord.obstacles['bottom_pipe'])
        if bird_rect.colliderect(rect):
            game_lost()
            continue
        
        if rect.x - coord.pipe_width <= 0:
            if coord.first_pipe:
                coord.change_pipes_positions1()
            else:
                coord.change_pipes_positions2()
            coord.first_pipe = not coord.first_pipe
            pygame.display.update()

    for rect in coord.obstacles.values():
        pygame.display.update()
        rect.x -= bird_vel[0]

    pygame.draw.circle(screen,'Red', (coord.bird_pos[0],coord.bird_pos[1]), coord.bird_radius)

    pygame.draw.rect(screen,'Blue',bird_rect,2)

    pygame.display.update()
    clock.tick(60)

pygame.quit()