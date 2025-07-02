score = 0
score_font = pygame.font.Font(None,12)
score_text = score_font.render(score,True,'White')
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = not running
    
    gravity_and_movements()
    bird_rect.topleft = coord.bird_pos[0] - coord.bird_radius,coord.bird_pos[1] - coord.bird_radius

    screen.fill('Black')
    screen.blit(score_text,(10,10))
    score += 1
