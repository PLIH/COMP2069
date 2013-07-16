#Source File Name: CanvasTest.py
#Author's Name: Paige Harvey
#Last Modified By: Paige Harvey
#Last Modified On: 2012-06-10
#Program Description: Paint Program
#Revision History:
#  - 

import pygame, Buttons

def main():
    pygame.init()

##    The creation information for the main Screen

    screen = pygame.display.set_mode((550,550))

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255,0,0))

    canvas = pygame.Surface((500,500))
    canvas = canvas.convert()
    canvas.fill((255,255,255))

##    #buttons
    lines = Buttons.Button()
##    shapes = Buttons.Button()
##    colour1 = Buttons.Button()
##    colour2 = Buttons.Button()

##        The creation information for the tools Screen

    tools = pygame.display.set_mode((550,550))

    bk = pygame.Surface(tools.get_size())
    bk = bk.convert()
    bk.fill((0,0,255))

    #Buttons for Lines
    str8Line = Buttons.Button()
    curveLine = Buttons.Button()
    

    #Buttons for shapes

    

##        Initial Variables

    clock = pygame.time.Clock()
    preview = False
    toolMenu = False
    keepGoing = True
    LineStart = (0,0)
    LineEnd = (0,0)

    selectedLine = "Straight"
    selectedShape = "FillSquare"
    
    while (keepGoing):
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif toolMenu == False:
                if lines.onClick(pygame.mouse.get_pos()):
                    if selectedLine == "Straight":
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            lineStart = pygame.mouse.get_pos()
                            preview = True
                        elif event.type == pygame.MOUSEBUTTONUP:
                            lineEnd = pygame.mouse.get_pos()
                            pygame.draw.line(canvas, (0, 0, 0), lineStart, lineEnd, 3)
                            preview = False
                        elif event.type == pygame.MOUSEMOTION:
                            lineEnd = pygame.mouse.get_pos()
                    elif selectedLine == "Curved":
                        if event.type == pygame.MOUSEMOTION:
                            lineEnd = pygame.mouse.get_pos()
                            if pygame.mouse.get_pressed() == (1,0,0):
                                pygame.draw.line(canvas, (0,0,0), lineStart, lineEnd, 1)
                                lineStart = lineEnd
                                
         #All the events if the toolMenu is on                       
            elif toolMenu == True:
                if str8Line.onClick(pygame.mouse.get_pos()):
                    selectedLine = "Straight"
                elif curved.onClick(pygame.mouse.get_pos()):
                    selectedLine = "Curved"


        #Switch between the Screens
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    if toolMenu:
                        toolMenu = False
                    else:
                        toolMenu = True                
            
        
        if toolMenu:
            tools.blit(bk, (0,0))
            str8Line.square(bk, (255,255,255), 30,15,50,50)
            curveLine.square(bk, (255,255,255), 30,15,100,100)
        else:
            screen.blit(background, (0, 0))
            screen.blit(canvas, (0,0))
            lines.labeledButton(screen, (255,255,255), 30,15,510,510,0,"Lines",(0,0,0))
            if preview:
                pygame.draw.line(screen, (100, 100, 100), lineStart, lineEnd, 1)

        pygame.display.flip()

if __name__ == "__main__": main()
