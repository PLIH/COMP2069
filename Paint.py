#Source File Name: Paint.py
#Author's Name: Paige Harvey
#Last Modified By: Paige Harvey
#Last Modified On: 2013-07-13
#Program Description: Paint Program
#Revision History:
#  - Added an Eraser
#  - Added Internal code, cleaned it up a bit

import pygame, Buttons

def text(toPrint):
    font = pygame.font.SysFont("None", 30)
    label = font.render(toPrint, 1, (255,255,255))
    return label

def main():
    pygame.init()
##   -------------------------------------------- 
##    The creation information for the Screens
##   --------------------------------------------
##      This is for the background and the canvas of the main screen
    screen = pygame.display.set_mode((550,550))
    pygame.display.set_caption("NGwKs Paint: A Paint Program")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((150,150,150))

    canvas = pygame.Surface((500,500))
    canvas = canvas.convert()
    canvas.fill((255,255,255))

##    This is the for the tool selection screen

    tools = pygame.display.set_mode((550,550))

    bk = pygame.Surface(tools.get_size())
    bk = bk.convert()
    bk.fill((150,150,150))

##   -------------------------------------------- 
##    Button Creation for both screens (some are shared)
##   --------------------------------------------    

    #Main Screen - functionality Buttons
    lines = Buttons.Button()
    shapes = Buttons.Button()
    eraser = Buttons.Button()
    clear = Buttons.Button()
    save = Buttons.Button()
    load = Buttons.Button()
    widthBtn = Buttons.Button()

  # Tool Screen - funcationality Buttons
    #Buttons for Lines
    str8Line = Buttons.Button()
    curvedLine = Buttons.Button()
    #Buttons for shapes
    sqrOutline = Buttons.Button()
    crOutline = Buttons.Button()
    sqrFill = Buttons.Button()
    crFill = Buttons.Button()

    #colour Buttons
    colourArea = Buttons.Button()
    colourPicker = Buttons.Button()
    colourViewer = pygame.Surface((100,100))
    colourViewer = colourViewer.convert()
    colour1 = Buttons.Button()
    colour2 = Buttons.Button()
    redBtn = Buttons.Button()
    greenBtn = Buttons.Button()
    blueBtn = Buttons.Button()
    #Preset colour buttons
    clRed = Buttons.Button()
    clGrn = Buttons.Button()
    clBlu = Buttons.Button()
    clOrg = Buttons.Button()
    clYel = Buttons.Button()
    clPur = Buttons.Button()
    clBlk = Buttons.Button()
    clWht = Buttons.Button()
    


##        Initial Variables

    #Those that keep the program running
    clock = pygame.time.Clock()
    keepGoing = True

    #Those that require initialization
    selectedWidth = 3
    selectedValue = ""
    println = ""
    activeEvent = "line"
    selectedLine = "str8line.png"
    selectedShape = "square.png"
    colourOutline = (0,0,0)
    colourFill = (255,255,255)
    redVal = 0
    greenVal = 0
    blueVal = 0
    chosenColour = (redVal,greenVal,blueVal)
    LineStart = (0,0)
    lineEnd = (0,0)

    #Those for default settings of processes
    colourChoice = False
    widthChoice = False
    preview = False
    toolMenu = False

##   -------------------------------------------- 
##   Program Start
##   --------------------------------------------    
    while (keepGoing):
        clock.tick(30)

        #Setting the text for labels
        userTips = text(println)
        rgbValue = text(str(chosenColour))

    # -------------------------------------
    #  If the tool Screen has been selected
    # -------------------------------------
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
            #If statements for Button clicks
                #User selects what shows on the icon bar in Canvas Screen
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if colourChoice == False and widthChoice == False:
                        if str8Line.onClick(pygame.mouse.get_pos()):
                            selectedLine = "str8line.png"
                        elif curvedLine.onClick(pygame.mouse.get_pos()):
                            selectedLine = "curvedline.png"
                        elif sqrOutline.onClick(pygame.mouse.get_pos()):
                            selectedShape = "sqaure.png"
                        elif crOutline.onClick(pygame.mouse.get_pos()):
                            selectedShape = "circle.png"
                        elif sqrFill.onClick(pygame.mouse.get_pos()):
                            selectedShape = "squareFill.png"
                        elif crFill.onClick(pygame.mouse.get_pos()):
                            selectedShape = "circleFill.png"
                        elif widthBtn.onClick(pygame.mouse.get_pos()):
                            #Program locks in width choice mode
                            widthChoice = True
                        elif colourArea.onClick(pygame.mouse.get_pos()):
                            #User cannot change a colour until a colour to change is chosen
                            println = "Please select a colour to edit"
                        elif colour1.onClick(pygame.mouse.get_pos()):
                            #Program locks into colour choice mode
                            #Program will only change Outline colour
                            colourChoice = True
                            selectedColour = "outline"
                            chosenColour = colourOutline
                            println = str(colourOutline)
                        elif colour2.onClick(pygame.mouse.get_pos()):
                            colourChoice = True
                            selectedColour = "fill"
                            chosenColour = colourFill
                            println = str(colourFill)

                            
        #  When program locks into colour choice mode, only clicks within
        #    the colour area will apply
                if colourChoice:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if colourArea.onClick(pygame.mouse.get_pos()):
                                #If user wants a colour already on canvas
                            if colourPicker.onClick(pygame.mouse.get_pos()):
                                toolMenu = False
                                activeEvent = "Colour Picker"
                                
                            if selectedColour == "outline":
                                println = "Editing the outline colour"
                            elif selectedColour == "fill":
                                println = "Editing the fill colour"
                                
                            #For pre-set colours
                            if clRed.onClick(pygame.mouse.get_pos()):
                                chosenColour = (255,0,0)
                            elif clGrn.onClick(pygame.mouse.get_pos()):
                                chosenColour = (0,255,0)
                            elif clBlu.onClick(pygame.mouse.get_pos()):
                                chosenColour = (0,0,255)
                            elif clOrg.onClick(pygame.mouse.get_pos()):
                                chosenColour = (255,165,0)
                            elif clYel.onClick(pygame.mouse.get_pos()):
                                chosenColour = (255,255,0)
                            elif clPur.onClick(pygame.mouse.get_pos()):
                                chosenColour = (128,0,128)
                            elif clBlk.onClick(pygame.mouse.get_pos()):
                                chosenColour = (0,0,0)
                            elif clWht.onClick(pygame.mouse.get_pos()):
                                chosenColour = (255,255,255)

                                #Getting the individual values from the tuple
                            redVal = chosenColour[0]
                            greenVal = chosenColour[1]
                            blueVal = chosenColour[2]

                                #to allow the User to adjust each value
                            if redBtn.onClick(pygame.mouse.get_pos()):
                                selectedValue = "red"
                                println = "Up or Down to edit the Red Value"
                            elif greenBtn.onClick(pygame.mouse.get_pos()):
                                selectedValue = "green"
                                println = "Up or Down to edit the Green Value"
                            elif blueBtn.onClick(pygame.mouse.get_pos()):
                                selectedValue = "blue"
                                println = "Up or Down to edit the Blue Value"
                            else:
                                selectedValue = ""
                        else:
                            println = "Press 'Enter' to set Colour Choice"

                    #Adjust the colour values
                    if event.type == pygame.KEYDOWN:
                        if selectedValue != "":
                            if event.key == pygame.K_UP:
                                if selectedValue == "red":
                                    redVal += 5
                                elif selectedValue == "green":
                                    greenVal += 5
                                elif selectedValue == "blue":
                                    blueVal += 5
                            elif event.key == pygame.K_DOWN:
                                if selectedValue == "red":
                                    redVal -= 5
                                elif selectedValue == "green":
                                    greenVal -= 5
                                elif selectedValue == "blue":
                                    blueVal -= 5

                                #Ensure that the colour values do not exceed or
                                # are under colour range
                            if redVal > 255:
                                redVal = 255
                            elif redVal < 0:
                                redVal = 0
                            elif greenVal > 255:
                                greenVal = 255
                            elif greenVal < 0:
                                greenVal = 0
                            elif blueVal > 255:
                                blueVal = 255
                            elif blueVal < 0:
                                blueVal = 0

                        #Set the chosen colour of the User's
                            chosenColour = (redVal,greenVal,blueVal)
                        if event.key == pygame.K_RETURN:
                            println = ""
                            colourChoice = False
                            if selectedColour == "outline":
                                colourOutline = chosenColour
                            elif selectedColour == "fill":
                                colourFill = chosenColour
                                
            # Program locks in line width choice
                if widthChoice:
                    println = "Up or Down to change line Width. Enter to Set"
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            selectedWidth += 1
                        elif event.key == pygame.K_DOWN:
                            selectedWidth -= 1
                        elif event.key == pygame.K_RETURN:
                            widthChoice = False

                #Ensures that width does not exceed or is under range
                        if selectedWidth > 9:
                            selectedWidth = 9
                        elif selectedWidth < 1:
                            selectedWidth = 1

    # ---------------------------------------
    #  Everything on the Tool Screen is blit
    # ---------------------------------------
                        
            tools.blit(bk, (0,0))
            screen.blit(userTips, (0,510))
            
            #Drawing tools Buttons
            lines.graphic(bk, 30,30,510,125,selectedLine)
            shapes.graphic(bk,30,30,510,165,selectedShape)
            str8Line.graphic(bk,30,30,420,125,"str8line.png")
            curvedLine.graphic(bk,30,30,460,125,"curvedline.png")
            sqrOutline.graphic(bk,30,30,340,165,"square.png")
            crOutline.graphic(bk,30,30,380,165,"circle.png")
            sqrFill.graphic(bk,30,30,420,165,"squareFill.png")
            crFill.graphic(bk,30,30,460,165,"circleFill.png")
            widthBtn.labeledButton(bk,(150,150,150),30,30,510,260,str(selectedWidth),(0,0,0))


            #Everything for colour choice area
            screen.blit(rgbValue, (100,275))
            colour1.square(bk,colourOutline,30,30,510,300)
            colour2.square(bk,colourFill,30,30,510,340)
            colourArea.invisiSquare(bk,295,155,90,290," ",(0,0,0))
            colourViewer.fill(chosenColour)
            screen.blit(colourViewer, (100,300))
            redBtn.labeledButton(bk,(255,0,0),50,25,250,300," R",(0,0,0))
            greenBtn.labeledButton(bk,(0,255,0),50,24,250,335," G",(0,0,0))
            blueBtn.labeledButton(bk,(0,0,255),50,25,250,370," B",(0,0,0))
            colourPicker.graphic(bk,30,30,325,310,"dropper.png")
            #Including preset colours
            clRed.square(bk,(255,0,0),30,30,100,405)
            clGrn.square(bk,(0,255,0),30,30,135,405)
            clBlu.square(bk,(0,0,255),30,30,170,405)
            clOrg.square(bk,(255,165,0),30,30,205,405)
            clYel.square(bk,(255,255,0),30,30,240,405)
            clPur.square(bk,(128,0,128),30,30,275,405)
            clBlk.square(bk,(0,0,0),30,30,310,405)
            clWht.square(bk,(255,255,255),30,30,345,405)
            
    # ---------------------------------------
    #  If the main Screen (Canvas is showing)
    # ---------------------------------------

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
                    elif event.key == pygame.K_RETURN:
                        activeEvent = ""

                    #If the icon Bar is clicked, a tool changed,...
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos() > (500,500):
                        activeEvent = ""
                        println = ""
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
                    elif eraser.onClick(pygame.mouse.get_pos()):
                        activeEvent = "eraser"
                    #These next three buttons auto-switch to Tool Menu
                    elif widthBtn.onClick(pygame.mouse.get_pos()):
                        toolMenu = True
                        widthChoice = True
                    elif colour1.onClick(pygame.mouse.get_pos()):
                        toolMenu = True
                        colourChoice = True
                        selectedColour = "outline"
                    elif colour2.onClick(pygame.mouse.get_pos()):
                        toolMenu = True
                        colourChoice = True
                        selectedColour = "fill"
         ## -------------------------------------------------------------------
            # The active events are what determine what drawing tool is in use
         ## -------------------------------------------------------------------
                if activeEvent == "line":
                  # User can draw a straight line
                    if selectedLine == "str8line.png":
                        println = "Draw a straight line"
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            lineStart = pygame.mouse.get_pos()
                            preview = True
                        elif event.type == pygame.MOUSEBUTTONUP:
                            lineEnd = pygame.mouse.get_pos()
                            pygame.draw.line(canvas, colourOutline, lineStart,lineEnd, selectedWidth)
                            preview = False
                        elif event.type == pygame.MOUSEMOTION:
                            lineEnd = pygame.mouse.get_pos()
                  #  or a Curved Line
                    elif selectedLine == "curvedline.png":
                        println = "Draw a curved line"
                        if event.type == pygame.MOUSEMOTION:
                            lineEnd = pygame.mouse.get_pos()
                            if pygame.mouse.get_pressed() == (1,0,0):
                                pygame.draw.line(canvas,colourOutline,lineStart,lineEnd,selectedWidth)
                            lineStart = lineEnd
                                
                elif activeEvent == "shape":
                  # User can draw a square outline
                    if selectedShape == "square.png":
                        println = "Draw an outline of a rectangle"
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            lineStart = pygame.mouse.get_pos()
                            lineEnd = (0,0)
                            preview = True
                        elif event.type == pygame.MOUSEBUTTONUP:
                            currentPos = pygame.mouse.get_pos()
                            lineEnd = (currentPos[0]-lineStart[0], currentPos[1]-lineStart[1])
                            pygame.draw.rect(canvas,colourOutline,(lineStart,lineEnd),selectedWidth)
                            preview = False
                        elif event.type == pygame.MOUSEMOTION:
                            currentPos = pygame.mouse.get_pos()
                            lineEnd = (currentPos[0]-lineStart[0], currentPos[1]-lineStart[1])
                    elif selectedShape == "circle.png":
                      # A circle outline
                        println = "Draw an outline of a circle"
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            lineStart = pygame.mouse.get_pos()
                            lineEnd = (0,0)
                            preview = True
                        elif event.type == pygame.MOUSEBUTTONUP:
                            currentPos = pygame.mouse.get_pos()
                            lineEnd = (currentPos[0]-lineStart[0], currentPos[1]-lineStart[1])
                            if lineEnd > (1,1):
                                pygame.draw.ellipse(canvas,colourOutline,(lineStart,lineEnd),selectedWidth)
                                preview = False
                        elif event.type == pygame.MOUSEMOTION:
                            currentPos = pygame.mouse.get_pos()
                            lineEnd = (currentPos[0]-lineStart[0], currentPos[1]-lineStart[1])
                    elif selectedShape == "squareFill.png":
                      # A square filled with a colour
                        println = "Draw a rectangle filled with colour"
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            lineStart = pygame.mouse.get_pos()
                            lineEnd = (0,0)
                            preview = True
                        elif event.type == pygame.MOUSEBUTTONUP:
                            currentPos = pygame.mouse.get_pos()
                            lineEnd = (currentPos[0]-lineStart[0], currentPos[1]-lineStart[1])
                            pygame.draw.rect(canvas,colourFill,(lineStart,lineEnd),0)
                            pygame.draw.rect(canvas,colourOutline,(lineStart,lineEnd),selectedWidth)
                            preview = False
                        elif event.type == pygame.MOUSEMOTION:
                            currentPos = pygame.mouse.get_pos()
                            lineEnd = (currentPos[0]-lineStart[0], currentPos[1]-lineStart[1])
                    elif selectedShape == "circleFill.png":
                      # A circle filled with colour
                        println = "Draw a circle filled with colour"
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            lineStart = pygame.mouse.get_pos()
                            lineEnd = (0,0)
                            preview = True
                        elif event.type == pygame.MOUSEBUTTONUP:
                            currentPos = pygame.mouse.get_pos()
                            lineEnd = (currentPos[0]-lineStart[0], currentPos[1]-lineStart[1])
                            if lineEnd > (1,1):
                                pygame.draw.ellipse(canvas,colourFill,(lineStart,lineEnd),0)
                                pygame.draw.ellipse(canvas,colourOutline,(lineStart,lineEnd),selectedWidth)
                                preview = False
                        elif event.type == pygame.MOUSEMOTION:
                            currentPos = pygame.mouse.get_pos()
                            lineEnd = (currentPos[0]-lineStart[0], currentPos[1]-lineStart[1])
                    
                elif activeEvent == "eraser":
                  # Or they can erase
                    println = "Eraser"
                    if event.type == pygame.MOUSEMOTION:
                        lineEnd = pygame.mouse.get_pos()
                        if pygame.mouse.get_pressed() == (1,0,0):
                            pygame.draw.line(canvas,(255,255,255),lineStart,lineEnd,(selectedWidth*2))
                        lineStart = lineEnd

            # This lives here rather than in the Tool Menu because it functions here
                elif activeEvent == "Colour Picker":
                    println = "Select a colour to work with"
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        chosenColour = tuple(canvas.get_at(pygame.mouse.get_pos()))
                        redVal = chosenColour[0]
                        greenVal = chosenColour[1]
                        blueVal = chosenColour[2]
                        println = "("+str(redVal)+","+str(greenVal)+","+str(blueVal)+")"
                        toolMenu = True                   
                    
    # ---------------------------------------
    #  Everything on the Main Screen is blit
    # ---------------------------------------
                            
            screen.blit(background, (0, 0))
            screen.blit(canvas, (0,0))
            screen.blit(userTips, (0,510))

            #The functionality buttons
            clear.graphic(background, 30,30,510,5,"clear.png")
            save.graphic(background, 30,30,510,40,"save.png")
            load.graphic(background, 30,30,510,75,"load.png")
            lines.graphic(background, 30,30,510,125,selectedLine)
            shapes.graphic(background,30,30,510,165,selectedShape)
            eraser.graphic(background,30,30,510,205,"eraser.png")

            #The adjustment Buttons
            widthBtn.labeledButton(background,(150,150,150),30,30,510,260,str(selectedWidth),(0,0,0))
            colour1.square(background,colourOutline,30,30,510,300)
            colour2.square(background,colourFill,30,30,510,340)

            #And the previews of al lines and shapes
            if (preview and activeEvent == "line"):
                pygame.draw.line(screen, (100, 100, 100), lineStart, lineEnd, 1)
            elif (preview and (selectedShape == "square.png" or selectedShape == "squareFill.png")):
                pygame.draw.rect(screen, (100,100,100),(lineStart,lineEnd),1)
            elif (preview and selectedShape == "circle.png"):
                if lineEnd > (1,1):
                    pygame.draw.ellipse(screen, (100,100,100),(lineStart,lineEnd),1) 

        pygame.display.flip()

if __name__ == "__main__": main()




            
