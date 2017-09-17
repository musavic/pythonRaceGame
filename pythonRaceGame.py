import pygame
import time
import random

pygame.init()


display_width = 800
display_height = 600

#COLORS
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0,200,0)
green_bright = (0,255,0)
red_bright = (255,0,0)


car_width = 49

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Let us race')
clock = pygame.time.Clock()

redImg = pygame.image.load('redcar.png')
carImg = pygame.image.load('car.png')
blackImg = pygame.image.load('blackcar.png')
roadImg = pygame.image.load('road.png')


pause = False

#DEFINTIONS
def quitgame():
    pygame.quit()
    quit()

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("POINTS: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))

'''def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])'''


def road(dx, dy, dw, dh):
    gameDisplay.blit(roadImg, (dx, dy, dw, dh))

def things(rx, ry, rw, rh):
    gameDisplay.blit(redImg, (rx, ry, rw, rh))

def blackcar(bx, by, bw, bh):
    gameDisplay.blit(blackImg, (bx, by, bw, bh))

def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    play_again()

def crash():
    message_display('You Crashed')

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,((x - 5),(y - 5),(w + 10),(h + 10)))


        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))


    smallText = pygame.font.SysFont("jokerman",30)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


def unpause():
    global pause
    pause = False


def paused():
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # gameDisplay.fill(white)


        button("Continue", 150, 450, 150, 50, green, green_bright, unpause)
        button("Quit", 550, 450, 100, 50, red, red_bright, quitgame)

        pygame.display.update()
        clock.tick(15)

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms", 115)
        TextSurf, TextRect = text_objects("Let us Race", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Play!", 150, 450, 100, 50, white, green_bright, game_loop)
        button("Quit", 550, 450, 100, 50, white, red_bright, quitgame)


        pygame.display.update()
        clock.tick(15)

def play_again():

    again = True

    while again:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms", 115)
        TextSurf, TextRect = text_objects("TRY AGAIN", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Play Again!", 150, 450, 175, 50, green, green_bright, game_loop)
        button("Quit", 550, 450, 100, 50, red, red_bright, quitgame)



        pygame.display.update()
        clock.tick(15)

#OUR GAME
def game_loop():
    global pause
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    '''thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100
    thingCount = 1'''




    start_dx = -200
    start_dy = -30
    d_speed = 10
    d_width = 49
    d_height = 100



    start_rx = random.randrange(0, display_width)
    start_ry = -600
    r_speed = 5
    r_width = 49
    r_height = 100


    start_bx = random.randrange(0, display_width)
    start_by = random.randrange(-1000, -550)
    b_speed = 5
    b_width = 49
    b_height = 100


    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)

        '''things(thing_startx, thing_starty, thing_width, thing_height, block_color)

        thing_starty += thing_speed'''

        road(start_dx, start_dy, d_width, d_height, )
        start_dy == d_speed



        things(start_rx, start_ry, r_width, r_height,)
        start_ry += r_speed

        blackcar(start_bx, start_by, b_width, b_height, )
        start_by += b_speed

        car(x, y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        '''if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)

        if y < thing_starty + thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                print('x crossover')
                crash()



        if y < thing_starty + thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                print('x crossover')
                crash()'''

        if start_ry> display_height:
            start_ry = 0 - r_height
            start_rx = random.randrange(0, display_width)
            dodged += 1
            r_speed += 0.4


        if start_dy> display_height:
            start_dy = -150
            start_dx = -200







        if y < start_ry + r_height:
            print('y crossover')

            if x > start_rx and x < start_rx + r_width or x + car_width > start_rx and x + car_width < start_rx + r_width:
                print('x crossover')
                crash()


        if start_by> display_height:
            start_by = 0 - b_height
            start_bx = random.randrange(0, display_width)
            dodged += 1
            b_speed += 0.4


        if y < start_by + b_height:


            if x > start_bx and x < start_bx + b_width or x + car_width > start_bx and x + car_width < start_bx + b_width:

                crash()




        pygame.display.update()
        clock.tick(60)


game_intro()
game_loop()
pygame.quit()
quit()
