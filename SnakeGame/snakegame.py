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
fps = 30
# Game Loop

clock = pygame.time.Clock()

while not exit_game:

    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_x+=10
            
            if event.key == pygame.K_LEFT:
                snake_x-=10

            if event.key == pygame.K_UP:
                snake_y-=10

            if event.key == pygame.K_DOWN:
                snake_y+=10

            
            
    gameWindow.fill(white)
    pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()