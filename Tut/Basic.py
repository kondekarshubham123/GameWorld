import pygame
x = pygame.init()

# Creating Window
gameWindow = pygame.display.set_mode((500,500))
pygame.display.set_caption("Hello Shubham")


# Game Specific Variable
exit_game = False
game_over = False

# Crearing game loop

while not exit_game:
    # Event Handling
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("Right Key")

pygame.quit()
quit()