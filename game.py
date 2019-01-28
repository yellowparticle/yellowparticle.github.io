"""
Snake Pygame Code modified by Emily Huang
--Must have pygame installed and pictures used in this game downloaded--

thenewboston pygame tutorials 
"""

import pygame
import time
import random

pygame.init() # returns a tupul which is successful initialations and nonsuccessful

black = (255,255,255)
black = (0,0,0)
gold = (196, 193, 111)
red = (255,0,0)
orange = (255, 165, 0)
green = (9, 160, 115)
brown = (147, 112, 20)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height)) # (width, height) #returns a pygame.surface object
pygame.display.set_caption('Slither') # title

# 1. Image as background instead of fill color ( from stack overflow https://stackoverflow.com/questions/47878264/background-image-not-appearing-in-pygame)
background = pygame.image.load("wiipicture.jpg").convert()

# 2. Mouse instead of an apple (drew mouse instead of apple with my very professional artsy skillz)
icon = pygame.image.load('C:/Users/Emu/Pictures/mouse.png')
pygame.display.set_icon(icon)

img = pygame.image.load('C:/Users/Emu/Pictures/snakehead.png')
mouseimg = pygame.image.load('C:/Users/Emu/Pictures/mouse.png')

# pygame.display.flip() does the same thing as update. like a flip book, but however this updates entire surface at once
# pygame.display.update() <-- don't really need it #only updates the specfic area you mentioned but if you put no parameters in the function it'll update the entire surface

# 3. Clock showing time duration of game (from part of a tutorial code https://pythonprogramming.net/adding-sounds-music-pygame/)
clock = pygame.time.Clock()
surviveTimeClock = pygame.time.Clock()

AppleThickness = 30
block_size = 20

frameCount = 0
FPS = 15 #15 frames per second

direction = "right"

smallfont = pygame.font.SysFont("couriernew", 20)
medfont = pygame.font.SysFont("couriernew", 30)
largefont = pygame.font.SysFont("couriernew", 70)

# 4. Background music ( from tutorial https://pythonprogramming.net/adding-sounds-music-pygame/)
pygame.mixer.init()
pygame.mixer.music.load('miiplaza.mp3')
pygame.mixer.music.play(-1)

def snakeSize(snakeSize):
    text = smallfont.render("Mice Count: "+str(snakeSize), True, black)
    gameDisplay.blit(text, [0,0])

# 2. Clock showing time duration of game (from part of a tutorial code https://pythonprogramming.net/adding-sounds-music-pygame/)
def time(gameTime):
    text = smallfont.render(gameTime, True, red)
    gameDisplay.blit(text, [0,20])

def showFPS(FPS):
    text = smallfont.render(FPS, True, black)
    gameDisplay.blit(text, [575,570])

def randAppleGen():
    randAppleX = round(random.randrange(0, display_width-AppleThickness)) #/10.0))*10.0
    randAppleY = round(random.randrange(0, display_height-AppleThickness)) #/10.0)*10.0

    return randAppleX, randAppleY


def game_intro():
    
    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pyame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(gold)
        message_to_screen("Welcome to Slither",
                          green,
                          -100,
                          "large")
        message_to_screen("Can as many mice as you can. How long can you survive?",
                          black,
                          -30)
        message_to_screen("The more mice you eat, the longer you get.",
                          black,
                          10)
        message_to_screen("If you run into yourself, or the edges, you DIE!",
                          black,
                          50)
        message_to_screen("Press C to play, P to pause, or Q to quit.",
                          brown,
                          180)
        message_to_screen("Audio Avaliable",
                          red,
                          230)
         
        pygame.display.update()
         
        clock.tick(15)

def snake(block_size, snakeList):

    if direction == "right":
        head = pygame.transform.rotate(img, 270)

    if direction == "left":
        head = pygame.transform.rotate(img, 90)

    if direction == "up":
        head = img

    if direction == "down":
        head = pygame.transform.rotate(img, 180)


    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))

    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size]) # (where, what color, specify rectangle using list [x is 400, y is 300, width, height] 


def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    
    return textSurface, textSurface.get_rect()
    
def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    #screen_text = font.render(msg, True, color)
    #gameDisplay.blit(screen_text, [display_width/2, display_height/2])
    textRect.center = (display_width/2), (display_height/2)+ y_displace
    gameDisplay.blit(textSurf, textRect)

                       
def gameLoop():
    global direction

    direction = 'right'
    gameExit = False
    gameOver = False
    paused = False
    
    lead_x = display_width/2 # head of the snake 
    lead_y = display_height/2 # head of the snake
    
    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1
    
    randAppleX, randAppleY = randAppleGen()
    
    while not gameExit:

        if gameOver == True:
            message_to_screen("Game Over",
                              green,
                              y_displace=-50,
                              size = "large")
        
            message_to_screen("Press C to continue or Q to quit",
                              black,
                              50,
                              size="medium")
            pygame.display.update()

 
        while gameOver == True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
            
        if paused == True:
            message_to_screen("Paused",
                                orange,
                                -100,
                                size = "large")
                
            message_to_screen("Press C to continue or Q to quit.",
                              black,
                              25)

            pygame.display.update()

        while paused:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
            
            clock.tick(5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size # we want to move it by segments of 10 b/c block (thickness of snake) is 10 pixels wide and tall
                    lead_y_change = 0 
                if event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0 
                if event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0 
                if event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0

                if event.key == pygame.K_p:
                    paused = True
                    
    # boundaries 
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
                     
            #logic loop
        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.blit(background, [0,0])

        #pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])

        gameDisplay.blit(mouseimg, (randAppleX, randAppleY))


        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        
        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
            
        snake(block_size, snakeList)

        snakeSize(snakeLength-1)
        showFPS(str(clock))

        # 5. FPS counter (friend's suggestion & help)
        global frameCount
        frameCount += 1
        total_seconds = frameCount / FPS
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        output_Time = "Time: {0:02}:{1:02}".format(minutes, seconds)
        time(output_Time)
        
        pygame.display.update()

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:

            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness or lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:

                    randAppleX, randAppleY = randAppleGen()
                    snakeLength += 1

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:

                    randAppleX, randAppleY = randAppleGen()
                    snakeLength += 1

        clock.tick(FPS) 
            #print(event)

    pygame.quit() # uninitializes pygame (quits)
    quit() # exits out of python

game_intro()
gameLoop()




