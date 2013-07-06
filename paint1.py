#Source File Name: paint1.py
#Author's Name: Paige Harvey
#Last Modified By: Paige Harvey
#Last Modified On: 2012-07-04
#Program Description: Paint Program
#Revision History:
#  - Placing buttons on screens has broken the program.

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
                                
        #All the events for the Canvas menu are active        
        if toolMenu == False:
            for event in pygame.event.get():
                if lines.onClick(pygame.mouse.get_pos()):
                    if selectedLine == "str8line.png":
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            lineStart = pygame.mouse.get_pos()
                            preview = True
                        elif event.type == pygame.MOUSEBUTTONUP:
                            lineEnd = pygame.mouse.get_pos()
                            pygame.draw.line(canvas, (0, 0, 0), lineStart, lineEnd, 3)
                            preview = False
                        elif event.type == pygame.MOUSEMOTION:
                            lineEnd = pygame.mouse.get_pos()
                    elif selectedLine == "curvedline.png":
                        if event.type == pygame.MOUSEMOTION:
                            lineEnd = pygame.mouse.get_pos()
                            if pygame.mouse.get_pressed() == (1,0,0):
                                pygame.draw.line(canvas, (0,0,0), lineStart, lineEnd, 1)
                                lineStart = lineEnd
##                if shapes.onClick(pygame.mouseget_pos()):

            screen.blit(background, (0, 0))
            screen.blit(canvas, (0,0))
            screen.blit(errorMess, (0,510))
            lines.graphic(background, 30,30,510,510,selectedLine)
            if preview:
                pygame.draw.line(screen, (100, 100, 100), lineStart, lineEnd, 1)

                                
         #All the events if the toolMenu is on                       
        elif toolMenu == True:
            for event in pygame.event.get():
                if str8Line.onClick(pygame.mouse.get_pos()):
                    selectedLine = "str8line.png"
                elif curvedLine.onClick(pygame.mouse.get_pos()):
                    selectedLine = "curvedline.png"

            tools.blit(bk, (0,0))
            screen.blit(errorMess, (0,510))
            str8Line.graphic(bk,30,30,15,15,"str8line.png")
            curvedLine.graphic(bk,30,30,50,15,"curvedline.png")


        pygame.display.flip()

if __name__ == "__main__": main()
