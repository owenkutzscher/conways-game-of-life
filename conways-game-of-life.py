import pygame
import sys
import time
import numpy as np
import algorithm # Conway's Game, matrix updating function

pygame.init()


# Screen setup
info = pygame.display.Info()
dim_x = info.current_w
dim_y = info.current_h
screen = pygame.display.set_mode((dim_y, dim_y))
pygame.display.set_caption('Conway\'s Game of Life')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKBLUE = (0, 0 , 90)


# Font and text
font = pygame.font.Font(None, 36)
start_text = font.render("START", True, GREEN)
stop_text = font.render("STOP", True, RED)

# Game settings
game_arr = np.zeros((dim_y//10, dim_y//10)) # Initial game array
center = np.shape(game_arr)[0] // 2
game_arr[center][center-1:center+2] = 1 # Initial alive squares
game_arr[center+1][center] = 1
origional_game_arr = np.copy(game_arr)


# Game state and controls
playing = False
display_boundries = (dim_y, dim_y)
# Game speed
timer_interval = 100  # 1000 milliseconds = 1 second
previous_time = pygame.time.get_ticks()

# Button and text coordinates
y_ = dim_y / 30
button_top, button_bottom, button_left, button_right = y_, 3*y_, y_, 3*y_
play_button_coords = [(button_top, button_left), (button_left, button_bottom), (button_right, (button_top+button_bottom)/2)]
rect_width, rect_height = 200, 100
start_stop_coords = (button_left, button_top+button_bottom)


    
    
def draw_square(i, j, game_arr, display_boundries, COLOR):
    boundry_x_len, boundry_y_len = display_boundries
    game_x_len = np.shape(game_arr)[1]
    game_y_len = np.shape(game_arr)[0]
        
    size_x = boundry_x_len / game_x_len
    size_y = boundry_y_len / game_y_len
    
    x = size_x * j
    y = size_y * i
    
    pygame.draw.rect(screen, COLOR, (x, y, size_x, size_y))
    
def darken_color(color, amount):
    amount = 100*np.log(amount) + 100
    r, g, b = color
    r = max(0, r - amount)
    g = max(0, g - amount)
    b = max(0, b - amount)
    return (r, g, b)
    
    
def draw_game(game_arr, display_boundries):
    for i in range(len(game_arr)):
        for j in range(len(game_arr[0])):
            if game_arr[i][j]:
                draw_square(i, j, game_arr, display_boundries, WHITE)
                
            else: # Add in fun color fx
                square_found = False
                f = 0
                while not square_found:
                    f += 1
                    x_min, x_max = max(j-f, 0), min(j+1+f, dim_y)
                    y_min, y_max = max(i-f, 0), min(i+1+f, dim_y)
                    surrownding_squares = game_arr[y_min:y_max, x_min:x_max]
                    if surrownding_squares.any() == 1:
                        square_found = True
                        draw_square(i, j, game_arr, display_boundries, darken_color(WHITE, f))
                    elif f == 3:
                        square_found = True
                        draw_square(i, j, game_arr, display_boundries, BLACK)
                        
                

def kill_or_reive_square(game_arr, mouse_x, mouse_y):
    square = game_arr[mouse_y//10][mouse_x//10]
    if square:
        game_arr[mouse_y//10][mouse_x//10] = 0
    else:
        game_arr[mouse_y//10][mouse_x//10] = 1

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button_left < mouse_x < button_right and button_top < mouse_y < button_bottom:
                if not playing:
                    playing = True
                else:
                    playing = False
            else: # User has clicked on a square to be killed or revived
                kill_or_reive_square(game_arr, mouse_x, mouse_y)
            
            
    screen.fill(BLACK)

    
    
    
   
    if not playing:
        game_arr = origional_game_arr
        draw_game(game_arr, display_boundries)
        pygame.draw.polygon(screen, GREEN, play_button_coords) 
        screen.blit(start_text, start_stop_coords)
        
    if playing:
        draw_game(game_arr, display_boundries)
        
        pygame.draw.rect(screen, RED, (button_left, button_top, button_right-button_left, button_bottom-button_top)) 
        screen.blit(stop_text, start_stop_coords)
        
        
        
        
                
        # Calculate elapsed time
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - previous_time
        if elapsed_time >= timer_interval:
            # Update game array
            previous_time = current_time
            game_arr = algorithm.update_grid(game_arr)
        
        
    
    
    
    
    
    # Final updates
    pygame.display.flip() # Update the display
    pygame.time.Clock().tick(60)  # Cap at 60 frames per second
    
    

# Quit Pygame
pygame.quit()