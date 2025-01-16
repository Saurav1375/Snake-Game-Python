import pygame
import random
import os

os.chdir("C:/Users/Saurav Gupta/OneDrive/Desktop/DESKTOP/Python Projects/Game/Snake Game")

#Sound:
pygame.mixer.init()

#importing all modules:
pygame.init()

#colors:
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
yellow = (255, 255, 0)
Olive =  (128, 128, 0)
Lime = 	(0, 255, 0)
Green =  (0, 128, 0)

#Creating Window:
screen_width = 700
screen_height = 450

#Setting Title:
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SNAKE")
icon_surf = pygame.image.load(os.path.join("ASSETS", "snake32.png"))
pygame.display.set_icon(icon_surf)
pygame.display.update()

#Text font and FPS:
font = pygame.font.SysFont('calibri', 30)
clock = pygame.time.Clock()

#Functions:
def welcome():
   exit_game = False
   while not exit_game:

      gameWindow.fill((150,132,194))
      text_screen("WELCOMES TO SNAKE", black, 200, 200)
      text_screen("Press Space Bar To Play", black, 200, 240)

      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            exit_game = True

         if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               gameloop()   

      pygame.display.update()
      clock.tick(60)  

def plot_snake(gameWindow, color, snk_list, snake_size):
   for x,y in snk_list:
     pygame.draw.rect(gameWindow, color, [x, y ,snake_size, snake_size])

def text_screen(text, color, x, y):
   screen_text = font.render(text, True, color)
   gameWindow.blit(screen_text, [x, y])

#Game Loop:
def gameloop():
   #game specific variables:
   exit_game = False
   game_over = False

   snake_x = 55
   snake_y = 45
   snake_size = 25

   velocity_x = 0
   velocity_y = 0
   init_velocity = 2

   snk_list = []
   snk_length = 1

   if (not os.path.exists("highscore.txt")):
      with open ("highscore.txt", "w") as f:
         f.write("0")
   with open("highscore.txt", "r") as f:
      highscore = f.read()

   score = 0
   fps = 120

   food_x = random.randint(20, screen_width/2)
   food_y = random.randint(20, screen_height/2)
   
   while not exit_game:

      if game_over:
         # init_velocity=5
         with open("highscore.txt", "w") as f:
            f.write(str(highscore))
      
         gameWindow.fill((212,229,233))
         text_screen("GAME OVER! Press Enter To Continue", red, 100, 200)
         text_screen( "Your Score: " + str(score), red, 250, 250)

         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  exit_game = True

            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_RETURN:
                  gameloop()
            
      else:

         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  exit_game = True

            if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_RIGHT:
                     velocity_x = init_velocity 
                     velocity_y = 0

                  if event.key == pygame.K_LEFT:
                     velocity_x = - init_velocity
                     velocity_y = 0

                  if event.key == pygame.K_UP:
                     velocity_y = - init_velocity
                     velocity_x = 0
                     
                  if event.key == pygame.K_DOWN: 
                     velocity_y = init_velocity
                     velocity_x = 0
         
         snake_x = snake_x + velocity_x
         snake_y = snake_y + velocity_y

         if abs(snake_x - food_x)< 12 and abs(snake_y - food_y)< 12:
            pygame.mixer.music.load(
                r'C:\Users\Saurav Gupta\OneDrive\Desktop\DESKTOP\Python Projects\Game\Snake Game\assets\jump.wav')
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(100)
            # init_velocity=init_velocity+0.001
            
            score += 10
            
          
            food_x = random.randint(20, screen_width/2)
            food_y = random.randint(20, screen_height/2)
            
            snk_length += 4

            if score>int(highscore):
               highscore = score

         gameWindow.fill(black)   
         text_screen("SCORE: "+ str(score), red, 5, 5)
         text_screen("HIGHSCORE: " + str(highscore), red, 470, 10)

         pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

         head = []
         head.append(snake_x)
         head.append(snake_y)
         snk_list.append(head)


         if len(snk_list)>snk_length:
            del snk_list[0]
            

         if head in snk_list[:-1]:
            game_over = True
            pygame.mixer.music.load(
                r'C:\Users\Saurav Gupta\OneDrive\Desktop\DESKTOP\Python Projects\Game\Snake Game\assets\gameover.mp3')
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(.3)


         if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
            game_over = True
            pygame.mixer.music.load(
                r'C:\Users\Saurav Gupta\OneDrive\Desktop\DESKTOP\Python Projects\Game\Snake Game\assets\gameover.mp3')
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(.3)

         
         plot_snake(gameWindow, yellow, snk_list, snake_size)

      pygame.display.update()
      clock.tick(fps)

   pygame.quit()
   quit()

welcome()

