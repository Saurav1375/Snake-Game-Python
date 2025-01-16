import pygame
pygame.init()

#Creating Game Window
gameWindow = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("My First Game")

#Game specific variable
exit_game = False
game_over = False

#Creating a game loop
while not exit_game:
    for event in pygame.event.get():
          if event.type == pygame.QUIT:
            exit_game = True
    
          if event.type == pygame.KEYDOWN: 
             if event.key == pygame.K_RIGHT:
                 print("You have pressed right arrow key")
1
pygame.quit()
quit()
