# File created by: Domenico DiStefano

# import libraries
# delay to have it be more digestible to the user
from time import sleep
# used to pick a random number from the list of options
from random import randint
# imports pygame functions as pg
import pygame as pg
# imports os which a multiple functions used for your operating system to manage files and folders
import os

# setup asset folders - images and sounds
# variable that equals a module that pulls from rps.py file and locates which file directory it is in
game_folder = os.path.dirname(__file__)

# game settings
WIDTH = 1200
HEIGHT = 600
FPS = 30
PLAY = False

# define numerical values as colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# init pygame and create a window
pg.init()
# initiating sound mixer
pg.mixer.init()
# initiates screen display
screen = pg.display.set_mode((WIDTH, HEIGHT))
# changes display name of the app window
pg.display.set_caption("Rock Paper Scissors")
clock = pg.time.Clock()

# variable that equals the image in the file directory
rock_image = pg.image.load(os.path.join(game_folder, "rock.jpg")).convert()
rock_rect = rock_image.get_rect()

# variable that equals image in file directory
paper_image = pg.image.load(os.path.join(game_folder, "paper.png")).convert()
paper_rect = paper_image.get_rect()

# varibale that equals image in file directory 
scissors_image = pg.image.load(os.path.join(game_folder, "scissors.png")).convert()
scissors_rect = scissors_image.get_rect()

# gets font from file directory and defines the font size
font = pg.font.Font(os.path.join(game_folder, "font.ttf"), 256)
playfont = pg.font.Font(os.path.join(game_folder, "font.ttf"), 64)

# variable that equals text for winning as well as text color and box color
wintext = font.render("YOU WIN", True, BLACK, WHITE)
win_rect = wintext.get_rect()
win_rect.center = (WIDTH // 2, HEIGHT // 2)

# variable that equals text for losing lose
losetext = font.render("YOU LOSE", True, BLACK, WHITE)
lose_rect = losetext.get_rect()
lose_rect.center = (WIDTH // 2, HEIGHT // 2)

# variable tht equals text for tie
tietext = font.render("WE TIED", True, BLACK, WHITE)
tie_rect = tietext.get_rect()
tie_rect.center = (WIDTH // 2, HEIGHT // 2)

# variable tht equals text for player choice
playtext = playfont.render("WANT TO PLAY ROCK PAPER SCISSORS?", True, BLACK, WHITE)
play_rect = playtext.get_rect()

# variable tht equals text for yes
yestext = playfont.render("YES", True, BLACK, WHITE)
yes_rect = yestext.get_rect()

# variable tht equals text for no
notext = playfont.render("NO", True, BLACK, WHITE)
no_rect = notext.get_rect()

# variable that equals a list of choices
choices = ["rock","paper","scissors"]

# function that randomly chooses a number between 0 and 2 and returns a string value
def cpu_choice():
    # randomly chooses an integer betwen 0 and 2 and then refers back to the function to return a string value
    return choices[randint(0,2)]

# functions for displaying text on win/loss/tie
def win():
    screen.fill(WHITE)
    screen.blit(wintext, win_rect)
def lose():
    screen.fill(WHITE)
    screen.blit(losetext, lose_rect)
def tie():
    screen.fill(WHITE)
    screen.blit(tietext, tie_rect)  

# function that compares player choice to cpu choice and displays appropriate response on pygame
def rps():
    cpu = cpu_choice()
    # variables for text that displays the cpu choice
    cpuchoicetext = playfont.render("CPU chose: " + str(cpu), True, BLACK, WHITE)
    cpuchoicetext_rect = cpuchoicetext.get_rect()
    cpuchoicetext_rect.center = (WIDTH // 2, HEIGHT // 4)

    # variables for text that displays the user choice
    userchoicetext = playfont.render("USER chose: " + str(user_choice), True, BLACK, WHITE)
    userchoicetext_rect = userchoicetext.get_rect()
    userchoicetext_rect.center = (WIDTH //2, HEIGHT // 8)

    # block for if the user ties with the cpu
    if user_choice == cpu:
        tie()
        screen.blit(cpuchoicetext, cpuchoicetext_rect)
        screen.blit(userchoicetext, userchoicetext_rect)
    # block for if user chooses rock
    elif user_choice == "rock":
        if cpu == "scissors":
            win()
            screen.blit(cpuchoicetext, cpuchoicetext_rect)
            screen.blit(userchoicetext, userchoicetext_rect)
        elif cpu == "paper":
            lose()
            screen.blit(cpuchoicetext, cpuchoicetext_rect)
            screen.blit(userchoicetext, userchoicetext_rect)
    # block for if user chooses paper
    elif user_choice == "paper":
        if cpu == "rock":
            win()
            screen.blit(cpuchoicetext, cpuchoicetext_rect)
            screen.blit(userchoicetext, userchoicetext_rect)
        elif cpu == "scissors":
            lose()
            screen.blit(cpuchoicetext, cpuchoicetext_rect)
            screen.blit(userchoicetext, userchoicetext_rect)
    # block for if user chooses scissors
    elif user_choice == "scissors":
        if cpu == "paper":
            win()
            screen.blit(cpuchoicetext, cpuchoicetext_rect)
            screen.blit(userchoicetext, userchoicetext_rect)
        elif cpu == "rock":
            lose()
            screen.blit(cpuchoicetext, cpuchoicetext_rect)
            screen.blit(userchoicetext, userchoicetext_rect)
    # feedback option for user error
    else:
        print("Something went wrong (●__●)")


running = True
# while loop for running pygame
while running:
    # method: fucntion tied to class
    clock.tick(FPS)

    # if else statement for what objects to display at certain game states depending on if PLAY is true or false
    if not PLAY:
        # sets the function FPS to 30 allowing game to update faster
        FPS = 30

        # displays text and background
        screen.fill(WHITE)
        screen.blit(playtext, play_rect)
        screen.blit(yestext, yes_rect)
        screen.blit(notext, no_rect)

        # defines location of text boxes
        play_rect.center = (WIDTH // 2, HEIGHT // 2)
        yes_rect.center = (500, 550)
        no_rect.center = (700, 550)
        rock_rect.center = (100000, HEIGHT // 2)
        paper_rect.center = (100000, HEIGHT // 2)
        scissors_rect.center = (100000, 250)
    else:
        # updates text and background to new background and images
        screen.fill(WHITE)
        screen.blit(rock_image, rock_rect)
        screen.blit(paper_image, paper_rect)
        screen.blit(scissors_image, scissors_rect)

        # defines location of text boxes
        rock_rect.center = (100, HEIGHT // 2)
        paper_rect.center = (400, HEIGHT // 2)
        scissors_rect.center = (800, 250)
        play_rect.center = (100000, HEIGHT // 2)
        yes_rect.center = (10000, 550)
        no_rect.center = (10000, 550)

    # "if else statements" for events that may happen
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        # if statement for what happens after the left mouse button goes back up
        if event.type == pg.MOUSEBUTTONUP:
            # stores the xy position of the mouse after a left click
            mouse_coords = pg.mouse.get_pos()
            # checks mouse coords are colliding with the image and then runs the "if statement" if true
            if yes_rect.collidepoint(mouse_coords):
                # makes play equal to true which will display new objects on pygame
                PLAY = True
            elif no_rect.collidepoint(mouse_coords):
                # closes game
                running = False
            elif rock_rect.collidepoint(mouse_coords):
                # variable equal to string rock
                user_choice = "rock"
                # reduces the variable FPS to keep feedback on screen longer
                FPS = 0.35
                # calls function rps
                rps()
                # changes game setting "PLAY" to false allowing screen to update
                PLAY = False
            # checks mouse coords are colliding with the image and then runs the if statement if true
            elif paper_rect.collidepoint(mouse_coords):
                # variable equal to string rock
                user_choice = "paper"
                # reduces the variable FPS to keep feedback on screen longer
                FPS = 0.35
                # calls function rps
                rps()
                # changes game setting "PLAY" to false allowing screen to update
                PLAY = False
            # checks mouse coords are colliding with the image and then runs the if statement if true
            elif scissors_rect.collidepoint(mouse_coords):
                # print("you clicking scissors")
                user_choice = "scissors"
                # reduces the variable FPS to keep feedback on screen longer
                FPS = 0.35
                # calls function rps
                rps()
                # changes game setting "PLAY" to false allowing screen to update
                PLAY = False

    
    

    # updates screen to show stuff
    pg.display.flip()

# closes pygame box once the loop is broken
pg.quit()