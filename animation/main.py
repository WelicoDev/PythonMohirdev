import pygame

# initialize Pygame
pygame.init()

# create window
window = pygame.display.set_mode((400, 400))

# set up ball properties
ball_radius = 20
ball_x = 200
ball_y = 200
ball_dx = 5
ball_dy = 5

# start game loop
while True:
    # check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # move ball
    ball_x += ball_dx
    ball_y += ball_dy

    # check for ball collision with window edges
    if ball_x + ball_radius > 400 or ball_x - ball_radius < 0:
        ball_dx = -ball_dx
    if ball_y + ball_radius > 400 or ball_y - ball_radius < 0:
        ball_dy = -ball_dy

    # fill window with white color
    window.fill((255, 255, 255))

    # draw ball on window
    pygame.draw.circle(window, (255, 0, 0), (ball_x, ball_y), ball_radius)

    # update window
    pygame.display.update()

    # set frame rate
    pygame.time.Clock().tick(60)