#Source File Name: BigIf.py
#Author's Name: Paige Harvey
#Last Modified By: Paige Harvey
#Last Modified On: 2012-07-04
#Program Description: Paint Program
#Revision History:
#  - Using one big If as the top of the tree
#  - Has working buttons, and everything

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
    clear = Buttons.Button()
    save = Buttons.Button()
    load = Buttons.Button()
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
    sqrOutline = Buttons.Button()
    crOutline = Buttons.Button()

    

##        Initial Variables

    clock = pygame.time.Clock()
    preview = False
    toolMenu = False
    keepGoing = True
    LineStart = (0,0)
    lineEnd = (0,0)

    activeEvent = "line"
    selectedLine = "str8line.png"
    selectedShape = "square.png"
    
    while (keepGoing):
        clock.tick(30)

        errorMess = text(str(lineEnd))

        if toolMenu:
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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if str8Line.onClick(pygame.mouse.get_pos()):
                        selectedLine = "str8line.png"
                    elif curvedLine.onClick(pygame.mouse.get_pos()):
                        selectedLine = "curvedline.png"
                    elif sqrOutline.onClick(pygame.mouse.get_pos()):
                        selectedShape = "sqaure.png"
                    elif crOutline.onClick(pygame.mouse.get_pos()):
                        selectedShape = "circle.png"
                        
            tools.blit(bk, (0,0))
            screen.blit(errorMess, (0,510))
            str8Line.graphic(bk,30,30,15,15,"str8line.png")
            curvedLine.graphic(bk,30,30,50,15,"curvedline.png")
            sqrOutline.graphic(bk,30,30,15,50,"square.png")
            crOutline.graphic(bk,30,30,50,50,"circle.png")

        else:
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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if clear.onClick(pygame.mouse.get_pos()):
                        canvas.fill((255,255,255))
                    elif save.onClick(pygame.mouse.get_pos()):
                        pygame.image.save(canvas, "painting.bmp")
                    elif load.onClick(pygame.mouse.get_pos()):
                        canvas = pygame.image.load("painting.bmp")
                    elif lines.onClick(pygame.mouse.get_pos()):
                        activeEvent = "line"
                    elif shapes.onClick(pygame.mouse.get_pos()):
                        activeEvent = "shape"

                        
                if activeEvent == "line":
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
                                pygame.draw.line(canvas,(0,0,0),lineStart,lineEnd,1)
                            lineStart = lineEnd
                                
                elif activeEvent == "shape":
                    if selectedShape == "square.png":
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            lineStart = pygame.mouse.get_pos()
                            lineEnd = (0,0)
                            preview = True
                        elif event.type == pygame.MOUSEBUTTONUP:
                            currentPos = pygame.mouse.get_pos()
                            lineEnd = (currentPos[0]-lineStart[0], currentPos[1]-lineStart[1])
                            pygame.draw.rect(canvas,(0,0,0),(lineStart,lineEnd),3)
                            preview = False
                        elif event.type == pygame.MOUSEMOTION:
                            currentPos = pygame.mouse.get_pos()
                            lineEnd = (currentPos[0]-lineStart[0], currentPos[1]-lineStart[1])
                    elif selectedShape == "circle.png":
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            lineStart = pygame.mouse.get_pos()
                            preview = True
                        elif event.type == pygame.MOUSEBUTTONUP:
                            currentPos = pygame.mouse.get_pos()
                            lineEnd = (currentPos[0]-lineStart[0], currentPos[1]-lineStart[1])
                            pygame.draw.ellipse(canvas,(0,0,0),(lineStart,lineEnd),1)
                            preview = False
                        elif event.type == pygame.MOUSEMOTION:
                            currentPos = pygame.mouse.get_pos()
                            lineEnd = (currentPos[0]-lineStart[0], currentPos[1]-lineStart[1])
                        

                            
            screen.blit(background, (0, 0))
            screen.blit(canvas, (0,0))
            screen.blit(errorMess, (0,510))
            clear.graphic(background, 30,30,510,5,"clear.png")
            save.graphic(background, 30,30,510,40,"save.png")
            load.graphic(background, 30,30,510,75,"load.png")
            lines.graphic(background, 30,30,510,510,selectedLine)
            shapes.graphic(background,30,30,510,475,selectedShape)
            if (preview and activeEvent == "line"):
                pygame.draw.line(screen, (100, 100, 100), lineStart, lineEnd, 1)
            elif (preview and selectedShape == "square.png"):
                pygame.draw.rect(screen, (100,100,100),(lineStart,lineEnd),1)
            elif (preview and selectedShape == "circle.png"):
                pygame.draw.ellipse(screen, (100,100,100),(lineStart,lineEnd),1) 

        pygame.display.flip()

if __name__ == "__main__": main()




            
