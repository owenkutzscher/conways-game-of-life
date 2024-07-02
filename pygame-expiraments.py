import pygame
import sys
import time
pygame.init()

info = pygame.display.Info()
dim_x = info.current_w
dim_y = info.current_h

screen = pygame.display.set_mode((dim_x, dim_y))
pygame.display.set_caption('Conways Game of Life')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)



# start/stop text
font = pygame.font.Font(None, 36)

start_text = font.render("START", True, WHITE)
stop_text = font.render("STOP", True, WHITE)




# play/pause button properties
y_ = dim_y / 30
button_top = y_
button_bottom = 3*y_
button_left = y_
button_right = 3*y_
play_button_coords = [(button_top, button_left), (button_left, button_bottom), (button_right, (button_top+button_bottom)/2)]
rect_width, rect_height = 200, 100
start_stop_coords = (button_left, button_top+button_bottom)

# circle properties
circle_x, circle_y = 0, 0
circle_radius = 30
circle_speed = 5

# Indicate if playing
playing = False




def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)




'''
Game loop
'''
running = True
while running:
    '''
    Event handling
    '''
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
            
    screen.fill(BLACK)

    
    
    
    
    """
    Not playing
    """
    if not playing:
        pygame.draw.polygon(screen, GREEN, play_button_coords) 
        screen.blit(start_text, start_stop_coords)
    
    
    
    
    
    
    """
    Playing
    """
    if playing:
        pygame.draw.circle(screen, WHITE, (circle_x, circle_y), circle_radius)
        pygame.draw.rect(screen, RED, (button_left, button_top, button_right-button_left, button_bottom-button_top)) 
        screen.blit(stop_text, start_stop_coords)
    
    
    
    
    
    """
    Final updates
    """
    pygame.display.flip() # Update the display
    pygame.time.Clock().tick(60)  # Cap at 60 frames per second
    
    

# Quit Pygame
pygame.quit()