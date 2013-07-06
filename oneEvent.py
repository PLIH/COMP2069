#Source File Name: oneEvent.py
#Author's Name: Paige Harvey
#Last Modified By: Paige Harvey
#Last Modified On: 2012-07-04
#Program Description: Paint Program
#Revision History:
#  - Attempt using a For Event as the start of the tree

import pygame, Buttons

def text(toPrint):
    font = pygame.font.SysFont("None", 30)
    label = font.render(toPrint, 1, (255,255,255))
    return label

def main():
    pygame.init()

##    The creation information for the main Screen

    screen = pygame.display.set_mode((550,550))

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255,0,0))

    ##    #buttons
    lines = Buttons.Button()
    shapes = Buttons.Button()
##    colour1 = Buttons.Button()
##    colour2 = Buttons.Button()
##    save = Buttons.Button()

    canvas = pygame.Surface((500,500))
    canvas = canvas.convert()
    canvas.fill((255,255,255))

##        The creation information for the tools Screen

    tools = pygame.display.set_mode((550,550))

    bk = pygame.Surface(tools.get_size())
    bk = bk.convert()
    bk.fill((0,0,255))

    #Buttons for Lines
    str8Line = Buttons.Button()
    curvedLine = Buttons.Button()
    

    #Buttons for shapes

    

##        Initial Variables

    clock = pygame.time.Clock()
    preview = False
    toolMenu = False
    keepGoing = True
    LineStart = (0,0)
    LineEnd = (0,0)

    selectedLine = "str8line.png"
    selectedShape = "FillSquare"
    
    while (keepGoing):
        clock.tick(30)

        errorMess = text(selectedLine)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            #Switch between the Screens
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if toolMenu:
                        toolMenu = False
                    else:
                        toolMenu = True
                elif event.key == pygame.K_RIGHT:
                    if toolMenu:
                        toolMenu = False
                    else:
                        toolMenu = True

##            ///////////////////////////////
##            /
##            /  Canvas
##            /
##            ///////////////////////////////
            elif lines.onClick(pygame.mouse.get_pos()) and toolMenu == False:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    lineStart = pygame.mouse.get_pos()
                    preview = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    lineEnd = pygame.mouse.get_pos()
                    pygame.draw.line(canvas, (0,0,0),lineStart,lineEnd)
                    preview = False
                elif event.type == pygame.MOUSEMOTION:
                    lineEnd = pygame.mouse.get_pos()

            elif str8line.onClick(pygame.mouse.get_pos()) and toolMenu == True:
                selectedLine = "str8line.png"
            elif curvedLine.onClick(pygame.mouse.get_pos()) and toolMenu == True:
                selectedLine = "curvedline.png"


        if toolMenu:
            tools.blit(bk, (0,0))
            screen.blit(errorMess, (0,510))
            str8Line.graphic(bk,30,30,15,15,"str8line.png")
            curvedLine.graphic(bk,30,30,50,15,"curvedline.png")

        else:
            screen.blit(background, (0, 0))
            screen.blit(canvas, (0,0))
            screen.blit(errorMess, (0,510))
            lines.graphic(screen, 30,30,510,510,selectedLine)
            if preview:
                pygame.draw.line(screen, (100, 100, 100), lineStart, lineEnd, 1)

        pygame.display.flip()

if __name__ == "__main__": main()
