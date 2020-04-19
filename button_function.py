import pygame


# This is the button function
def text_objects(text, font):
    textSurface = font.render(text, True, (255, 255, 255))
    return textSurface, textSurface.get_rect()


# Button function to create functions #
def button(win,msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(win, ac,(x,y,w,h), 6)
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(win, ic,(x,y,w,h), 6)
    smallText = pygame.font.SysFont("freesansbold.ttf", 50)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    win.blit(textSurf, textRect)
