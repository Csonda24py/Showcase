import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
size = 900, 700
green = (255,255,255)
blue = (0, 0, 0)
picture = pygame.image.load('dvd.png')
picture = pygame.transform.scale(picture, (80, 50))
font = pygame.font.Font('freesansbold.ttf', 32)


# create a rectangular object for the
# text surface object

X = 50
Y = 50



# set the center of the rectangular object.

display_surface = pygame.display.set_mode((X, Y))
gradient = 2
direction = 1

last_point = [200,130]

screen = pygame.display.set_mode(size,0,32)
pygame.display.set_caption('GAME')
x, y = 200, 130
 
sprite=picture
loop = True
while loop:
    # this adds the sprite at every frame rate
    screen.fill((0,0,0))
    screen.blit(sprite,(x,y))
    zx = str([x,y])
    text = font.render(zx, True, green, blue)
    textRect = text.get_rect()
    display_surface.blit(text, textRect)
    textRect.center = (X // 2, Y // 2)
    
    
    for event in pygame.event.get():
        # this is to close the window
        if event.type==QUIT:
            loop = False
            #sys.exit() # this will close the kernel too
            # in development mode leave the comment above
    # this is the list with the keys being pressed
    
    

    

    y +=gradient
    x += direction

    if x < 0:
        if last_point[1] < y:
            gradient = 2
        else:
            gradient = -2
        direction = 1
        last_point[0] = x
        last_point[1] = y
    if x > 816:
        if last_point[1] < y:
            gradient = 2
        else:
            gradient = -2

        direction = -1
        last_point[0] = x
        last_point[1] = y
    if y < 0:

        
        gradient = 2
        if last_point[0] < x:
            direction = 1
        else:
            direction = -1
        last_point[0] = x
        last_point[1] = y
    if y > 650:
        
        gradient = -2
        if last_point[0] < x:
            direction = 1
        else:
            direction = -1
    
        last_point[0] = x
        last_point[1] = y
    
    # we update the screen at every frame

    pygame.display.flip()
    # if we put the frame rate at 60 the sprite will move slower
    clock.tick(120)
    
pygame.quit()


