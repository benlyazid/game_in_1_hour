from ast import For
from shutil import move
from time import sleep
from xml.dom import InuseAttributeErr
import pygame
import time
NUMBER_OF_TURNS = 50
number_of_box = 100
SCORE = [0] * number_of_box
size = (1000, 1300)
size_of_box = 100



#######################################################################################
####################################### Teams info  ###################################
team_name1 = "Lwa3rin"
team_name2 = "HELLO world"
color_1 = (0, 255, 255)
color_2 = (255, 0, 255)
team_color_1 = (100,250,36)
team_color_2 = (250,100,0)

def bot_team_1():
    moves = []
    size = 0
    start = 1 # EDIT START HERE
    while size != NUMBER_OF_TURNS:
        if start > 100:
            start = start % 100
        if start <= 100:
            moves.append(start)
        size += 1
        start = start + 3 # EDIT EQUATION OF SUIVIE
    return moves

def bot_team_2():
    moves = []
    size = 0
    start = 2 # EDIT START HERE
    while size != NUMBER_OF_TURNS:
        if start > 100:
            start = start % 100
        if start <= 100:
            moves.append(start)
        size += 1
        start = start + 1 # EDIT EQUATION OF SUIVIE
    return moves

moves_team_1 = bot_team_1()
moves_team_2 = bot_team_2()
index = 0
i = 0
while 1:
    pygame.init()
    surface = pygame.display.set_mode(size)
    color = color_1
    #draw maps
    for y in range(10):
        for x in range(10):
            pygame.draw.rect(surface, (0,0,0), pygame.Rect(x * size_of_box - 1, y * size_of_box - 1,size_of_box + 2,size_of_box + 2))
            pygame.draw.rect(surface, (255,255,255), pygame.Rect(x * size_of_box,y * size_of_box,size_of_box,size_of_box))
    pygame.time.wait(1000)
    index = 0
    while  index <= i:
        index_1 =  moves_team_1[index] - 1
        index_2 =  moves_team_2[index] - 1
        if index_1 != index_2:
            x =  index_1 % 10
            y =  int(index_1 / 10)
            pygame.draw.rect(surface, (0,0,0), pygame.Rect(x * size_of_box - 1, y * size_of_box - 1,size_of_box + 2,size_of_box + 2))
            pygame.draw.rect(surface, team_color_1, pygame.Rect(x * size_of_box,y * size_of_box,size_of_box, size_of_box))
            SCORE[index_1] = 1
            # print(i)

            x =  index_2 % 10
            y =  int(index_2 / 10)
            pygame.draw.rect(surface, (0,0,0), pygame.Rect(x * size_of_box - 1, y * size_of_box - 1,size_of_box + 2,size_of_box + 2))
            pygame.draw.rect(surface, team_color_2, pygame.Rect(x * size_of_box,y * size_of_box,size_of_box, size_of_box))           
            pygame.display.flip()
            SCORE[index_2] = 2
        index += 1

    pygame.draw.rect(surface, (0,0,0), pygame.Rect(0, 1000,1000,300))

    pygame.font.init() # you have to call this at the start, 
    myfont = pygame.font.SysFont('TTF', 60)
    s = team_name1 + " : " + str(SCORE.count(1))
    textsurface = myfont.render(s, False, team_color_1)
    surface.blit(textsurface,(10,1100))
    # pygame.font.init() # you have to call this at the start, 
    # myfont = pygame.font.SysFont('Comic Sans MS', 60)
    s = team_name2 + " : " + str(SCORE.count(2))
    textsurface = myfont.render(s, False, team_color_2)
    surface.blit(textsurface,(10,1180))
    print(SCORE.count(1), SCORE.count(2))
    pygame.display.flip()


    if i < NUMBER_OF_TURNS - 1:
        i += 1
    else:
        pygame.time.wait(100000)