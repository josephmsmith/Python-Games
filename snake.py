#Today we will be building a snake game in Python!

#import library
import pygame
import time
import random

#start creating the parameters for the actual game
snake_speed = 40
window_x = 720
window_y = 480

                                                               #create the window and speed of the snake

#define the colors
grey = pygame.Color(81,81,81)
white = pygame.Color(255, 255, 255)
red = pygame.Color(139, 34, 82)
green = pygame.Color(0, 205, 102)
blue = pygame.Color(99, 184, 255)
gold = pygame.Color(238, 173, 14)

# Iniatilize pygame
pygame.init()
# Initialize game window
pygame.display.set_caption("Joe's Spicy Snake Game")
game_window = pygame.display.set_mode((window_x, window_y))
# FPS (frames per second) controller
fps = pygame.time.Clock()  #Here pygame.time.Clock() will be used further in the main logic of the game to change the speed of the snake.


#now we need to initialize snake position and it's size
#define snake default position
snake_position = [100,50]
#define the first 4 blocks of snake
snake_body = [  [100,50],
                [90,50],
                [80,50],
                [70,50]
            ]
#fruit position 
fruit_position = [random.randrange(1,(window_x//10)) * 10, random.randrange(1,(window_y//10)) * 10]
fruit_spawn = True

#set default snake direction to right. Whenever user runs game, snake must move to the right. 
direction = 'RIGHT'
change_to = direction

score = 0
 
# displaying Score function
def show_score(choice, color, font, size):                                         #defining one large function to display score of the player
    score_font = pygame.font.SysFont(font, size)                                   # creating font object score_font
     
    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
     
    # create a rectangular object for the
    # text surface object
    score_rect = score_surface.get_rect()
     
    # displaying text
    game_window.blit(score_surface, score_rect)

#create game over function
def game_over():
    my_font = pygame.font.SysFont('broadway',50)                                 #create font object
    game_over_surface = my_font.render("Wasted! Score is: " + str(score), True, red)      #create a text surface
    game_over_rect = game_over_surface.get_rect()                                       #create rectangular object
    game_over_rect.midtop = (window_x/2, window_y/4)                                    #setting position of the text
    game_window.blit(game_over_surface, game_over_rect)                                 #blit will draw the text on screen
    pygame.display.flip()
    time.sleep(2)                                                                       #after 2 seconds we will quit the program
    pygame.quit()                                                                       #deactivating pygame library
    quit()

#lets write the main function for how the game works
while True:
    for event in pygame.event.get():                                                    #handling key events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
               change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    if change_to == 'UP' and direction != 'DOWN':                                        #if 2 keys pressed simultaneously, we dont want snake 
        direction = 'UP'                                                                 #to move in 2 directions at the simult
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':                                                                 #moving the snake
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    snake_body.insert(0, list(snake_position))                                             #snake body growing mechanism, if fruit/snake collid score +10
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]
    fruit_spawn = True
    game_window.fill(grey)

    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window,gold , pygame.Rect(
        fruit_position[0], fruit_position[1],10, 10))

    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    show_score(1, white, 'broadway', 20)
    pygame.display.update()
    fps.tick(snake_speed)