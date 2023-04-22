import pygame
import random

# initialize Pygame
pygame.init()

# create window
window = pygame.display.set_mode((400, 400))

# set up game properties
snake_position = [200, 200]
snake_body = [[200, 200], [180, 200], [160, 200]]
food_position = [random.randrange(1, 40) * 10, random.randrange(1, 40) * 10]
food_spawned = True
direction = "RIGHT"
change_to = direction
score = 0

# set up colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# set up sound effects
eat_sound = pygame.mixer.Sound("eat.wav")
game_over_sound = pygame.mixer.Sound("game_over.wav")

# define game over function
def game_over():
    pygame.mixer.Sound.play(game_over_sound)
    font = pygame.font.SysFont("comicsansms", 72)
    text = font.render("Game Over!", True, red)
    text_rect = text.get_rect()
    text_x = window.get_width() / 2 - text_rect.width / 2
    text_y = window.get_height() / 2 - text_rect.height / 2
    window.blit(text, [text_x, text_y])
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()

# start game loop
while True:
    # check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # check for arrow key input
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"
            elif event.key == pygame.K_LEFT:
                change_to = "LEFT"
            elif event.key == pygame.K_UP:
                change_to = "UP"
            elif event.key == pygame.K_DOWN:
                change_to = "DOWN"

    # check for direction change
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"
    elif change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    elif change_to == "UP" and direction != "DOWN":
        direction = "UP"
    elif change_to == "DOWN" and direction != "UP":
        direction = "DOWN"

    # move snake
    if direction == "RIGHT":
        snake_position[0] += 10
    elif direction == "LEFT":
        snake_position[0] -= 10
    elif direction == "UP":
        snake_position[1] -= 10
    elif direction == "DOWN":
        snake_position[1] += 10

    # check for snake collision with window edges
    if snake_position[0] >= 400 or snake_position[0] < 0 or snake_position[1] >= 400 or snake_position[1] < 0:
        game_over()

    # check for snake collision with food
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        food_spawned = False
        score += 10
        pygame.mixer.Sound.play(eat_sound)

    # spawn