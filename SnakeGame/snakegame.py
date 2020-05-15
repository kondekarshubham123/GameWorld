import pygame
pygame.init()

# Colors
white = (255,255,255) 
red = (255,0,0)
black = (0,0,0)


# Size
screen_width = 500
screen_height = 650
gameWindow = pygame.display.set_mode((screen_width,screen_height))


# Game Title
pygame.display.set_caption("SnakesWithShubham")
pygame.display.update()

# Game Spacific Variable
exit_game = False
game_over = False

# Snake Object
snake_x = 45
snake_y = 55
snake_size = 10

# Game Loop

while not exit_game:

    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            exit_game = True
            
    gameWindow.fill(white)
    pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
    pygame.display.update()

pygame.quit()
quit()