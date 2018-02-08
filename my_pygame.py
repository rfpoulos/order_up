import pygame
pygame.init()
canvas_width = 800
canvas_height = 600
screen = pygame.display.set_mode((canvas_width, canvas_height))

clock = pygame.time.Clock()
done = False

ball_x = 100
ball_y = 100
ball_radius = 50
while not done:
    for event in pygame.event.get():
        print event #For debugging
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            ball_y -= 3
        if pressed[pygame.K_DOWN]:
            ball_y +=3
        if pressed[pygame.K_LEFT]:
            ball_x -=3
        if pressed[pygame.K_RIGHT]:
            ball_x +=3
        if event.type == pygame.QUIT:
            done = True
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_radius, 0)
        pygame.display.update()
        clock.tick(60)
        
pygame.quit()