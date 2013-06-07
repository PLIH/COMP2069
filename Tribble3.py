#Source File Name: Tribble3.py
#Author's Name: Paige Harvey
#Last Modified By: Paige Harvey
#Last Modified On: 2012-06-06
#Program Description: Slot Machine based on Star Trek
#Revision History:
#  - Change Odds (favoured Win too much)
#  - Lowest Bet amount is now 5 (prev 1)

##    //////////////////////
##          IMPORTs 
##    //////////////////////

import pygame, Buttons, random

##                    Buttons.py was NOT written by Paige Harvey
##                        It was written by Simon H. Larsen,
##                        who then made it avaliable for download,
##                        which was linked to PYGAME.org.
##                    P Harvey downloaded it on June 3, 2013.
##
##                !~ REPEAT ~!
##                    P Harvey did NOT write Buttons.py

##    /////////////////////////////////////////////////////////////
##                          FUNCTION   AREA
##    /////////////////////////////////////////////////////////////
#               done in reverse order, b/c habit from C++

##    //////////////////////
##        REELS FUNCTION
##    //////////////////////
#       get&return 3 random strings in an array

def reels():
        # Variable initialization
    betline = [" "," "," "]
    outcome = [0,0,0]

    for spin in range(3):
        outcome[spin] = random.randrange(1,129,1)
        if outcome[spin] >= 1 and outcome[spin] <= 81:      # 63.28%
            betline[spin] = "Tribble.png"
        if outcome[spin] >= 82 and outcome[spin] <= 96:     # 11.72%
            betline[spin] = "Redshirt.png"
        if outcome[spin] >= 97 and outcome[spin] <= 108:    # 9.38%
            betline[spin] = "Tricorder.png"
        if outcome[spin] >= 109 and outcome[spin] <= 117:   # 7.03%
            betline[spin] = "Communicator.png"
        if outcome[spin] >= 118 and outcome[spin] <= 122:   # 3.91%
            betline[spin] = "Engineering.png"
        if outcome[spin] >= 123 and outcome[spin] <=125:    # 2.34%
            betline[spin] = "Science.png"
        if outcome[spin] >= 126 and outcome[spin] <=127:    # 1.56%
            betline[spin] = "Command.png"
        if outcome[spin] == 128:                            # 0.78%
            betline[spin] = "Enterprise.png"

    return betline
#           betline = array of 3 image file names
#               fed to handle_pull()

##    ///////////////////////
##     CHECK TRIPLE FUNCTION
##    ///////////////////////
#       count&check input betline for criteria
#       calculate&return winnings

def check_triple(line, bet):
        # Initial values
    winnings = 0
    howWin = " "
    win = False

# ~ Check the betline for THREE identical winning images
#     If line has a triple:
#       winnings - amount of money won (based on bet)
#       win      - True
    if line.count("Redshirt.png") == 3:
        winnings, win = (bet*20), True
        howWin = "Triple Redshirts!"
    elif line.count("Tricorder.png") == 3:
        winnings, win = (bet*30), True
        howWin = "Triple Tricorder"
    elif line.count("Communicator.png") == 3:
        winnings, win = (bet*40), True
        howWin = "Triple Communicator"
    elif line.count("Engineering.png") == 3:
        winnings, win = (bet*100), True
        howWin = "Triple Engineering"
    elif line.count("Science.png") == 3:
        winnings, win = (bet*200), True
        howWin = "Triple Science"
    elif line.count("Command.png") == 3:
        winnings, win = (bet*300), True
        howWin = "Triple Command"
    elif line.count("Enterprise.png") == 3:
        winnings, win = (bet*1000), True
        howWin = "Triple Enterprise"
        
    return winnings, win, howWin
#       winnings - money won (or the initial nothing)
#       win      - sentinel boolean
#       howWin   - String, What combination User won with (or nothing)
#           feeds into handle_pull()

##    ///////////////////////
##     CHECK DOUBLE FUNCTION
##    ///////////////////////
#       count&check input betline for criteria
#       calculate&return winnings

def check_double(line, bet):
        #initial values
    winnings = 0
    howWin = " "
    win = False

# ~ Check the betline for lack of TRIBBLEs
#     If line has a DOUBLE and NO tribble:
#       winnings - amount of money won (based on bet)
#       win      - True
#       howWin   - What combination User won with
    if line.count("Tribble.png") == 0:
        if line.count("Redshirt.png") == 2:
            winnings, win = (bet*2), True
            howWin = "Double Redshirt"
        elif line.count("Tricorder.png") == 2:
            winnings, win = (bet*2), True
            howWin = "Double Tricorder"
        elif line.count("Communicator.png") == 2:
            winnings, win = (bet*3), True
            howWin = "Double Communicator"
        elif line.count("Engineering.png") == 2:
            winnings, win = (bet*4), True
            howWin = "Double Engineering"
        elif line.count("Science.png") == 2:
            winnings, win = (bet*5), True
            howWin = "Double Science"
        elif line.count("Command.png") == 2:
            winnings, win = (bet*10), True
            howWin = "Double Command"
        elif line.count("Enterprise.png") == 2:
            winnings, win = (bet*20), True
            howWin = "Double Enterprise"
                # Check for a SINGLE ENTERPRISE (no tribbles)
        elif line.count("Enterprise.png") == 1:
            winnings, win = (bet*10), True
            howWin = "One Enterprise"
                # Or just no tribble in general
        else:
            winnings, win = (bet*2), True
            howWin = "No Tribble"

    return winnings, win, howWin
#       winnings - money won (or the initial nothing)
#       win      - sentinel boolean
#       howWin   - String, What combination User won with (or nothing)
#           feeds into handle_pull()

##    //////////////////////
##       JACKPOT FUNCTION
##    //////////////////////
#       add to jackpot
#       determine if User won JACKPOT

def win_jackpot(jackpot, bet):
        #Initial values && draw new JACKPOT numbers
    jackwin = False
    jackpot_attempt = random.randrange(1,51,1)
    jackpot_win = random.randrange(1,51,1)

    
##          For debugging purposes
##    print("\n*   Jackpot Drawing   *")
##    print("Attempt:" + str(jackpot_attempt))
##    print("Win: " + str(jackpot_win))

        # Should the two random values match... JACKPOT!!!
    if jackpot_attempt == jackpot_win:
        jackwin = True
        print("You won the Jackpot")
        winnings = int(jackpot)     # Add POT to total winnings
        jackpot = 500               # Reset POT to Initial Values
    else:
        jackwin = False
        winnings = 0
        
    return jackpot, winnings, jackwin
#       jackpot     - current amount in the POT
#       winnings    - How much the User has won (usually 0)
#       jackwin     - Sentinel boolean, if the User WON the POT
#           feeds into main()

##    //////////////////////
##     HANDLE_PULL FUNCTION
##    //////////////////////
#       Creates the Reels; creates the Betlines
#       Determines Betline multiplier

def handle_pull(bet, credit):
        # Initial Values
    whichLine = "None"
    dia_left_line = [" "," "," "]
    dia_right_line = [" "," "," "]
    win = False
    winnings = 0
        
#  ~ Where all the betlines are given values.
        # Call reels() for HORIZONTAL lines
    top_line = reels()
    mid_line = reels()
    bottom_line = reels()
    
        # DIAGONAL lines are built using the horizntal lines
    dia_left_line[0] = top_line[0]
    dia_left_line[1] = mid_line[1]
    dia_left_line[2] = bottom_line[2]
    
    dia_right_line[0] = top_line[2]
    dia_right_line[1] = mid_line[1]
    dia_right_line[2] = bottom_line[0]

        #The Array of Arrays; hierarchical order
    all_lines = [mid_line, top_line, bottom_line, dia_left_line, dia_right_line]

    #Show the lines         - Debugging Purpose Code
    #mid_line = ["Redshirt", "Enterprise", "Tricorder"]
##    print(top_line[0] +" - "+ top_line[1] +" - "+ top_line[2])
##    print(mid_line[0] +" - "+ mid_line[1] +" - "+ mid_line[2])
##    print(bottom_line[0] +" - "+ bottom_line[1] +" - "+ bottom_line[2])


#  ~ Check the Lines for WIN COMBINATIONS
#       Check combinations in HIERARCHICAL order [External Documentation]
        # Call check_triple for all lines (in a for-loop)
    for line in all_lines:
        winnings, win, howWin = check_triple(line, bet)
            # Which line won? Calculate Multiplier Bonus
        if win == True:
            if line == mid_line:
                whichLine = "Middle Line"
                winnings = winnings * 2     #Center lines x2 multiplier
            elif line == dia_left_line: 
                whichLine = "Diagonal Left"
                winnings = int(winnings / 2)    #Diagonal lines x.5 multiplier
            elif line == dia_right_line:
                whichLine = "Diagonal Right"
                winnings = int(winnings / 2)    #Diagonal lines x.5 multiplier
            elif line == top_line:
                whichLine = "Top Line"
            else:
                whichLine = "Bottom Line"
            return winnings, win, all_lines, whichLine, howWin
                    # (return breakdown at bottom of function)
        
    for line in all_lines:
        winnings, win, howWin = check_double(line, bet)
        if win == True:
                # Which line won? Calculate Multiplier Bonus
            if line == mid_line:
                whichLine = "Middle Line"
                winnings = winnings * 2     #Center line x2 multiplier
            elif line == dia_left_line:
                whichLine = "Diagonal Left"
                winnings = int(winnings / 2)    #Diagonal lines x.5 multiplier
            elif line == dia_right_line:
                whichLine = "Diagonal Right"
                winnings = int(winnings / 2)    #Diagonal lines x.5 multiplier
            elif line == top_line:
                whichLine = "Top Line"
            else:
                whichLine = "Bottom Line"
            return winnings, win, all_lines, whichLine, howWin
                    # (return breakdown at bottom of function)
        
    return winnings, win, all_lines, whichLine, howWin
#       winnings  - amount won by User (can be 0)
#       win       - sentinel boolean; did User win?
#       all_lines - Array of arrays; for image.load purposes
#       whichLine - label purposes; which betline User won with
#       howWin    - label purposes; what combination User won with
#               feeds main()

##    //////////////////////
##        LABEL FUNCTION
##    //////////////////////
        # Take input, process it for labeling
def labels(toPrint):
    font = pygame.font.Font("ArchitectsDaughter.ttf", 20)
    label = font.render(toPrint, 1, (0,0,0))
    return label
        # feeds main()


##    //////////////////////
##        MAIN FUNCTION
##    //////////////////////    

def main():
  #initialize pygame
    pygame.init()
    
    #Colours will never change values. Required for Button Creation
    activeButton = (185,0,255)
    disableButton = (150,150,150)
    currentButton = (0,205,0)
    
  #Defining screen   
    screen = pygame.display.set_mode((1120, 750))
    pygame.display.set_caption("Trouble with Tribbles: Slot Machine")

  #Entities Creation
    #background image
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background = pygame.image.load("background.png")

    #Message box/rectangle/label
    messBox = pygame.Surface((300,100))
    messBox = messBox.convert()
    messBox.fill((255,0,0))

    #Jackpot light
    jackLight = pygame.Surface((354,101))
    jackLight = jackLight.convert_alpha()
    jackLight = pygame.image.load("jackpot.png")

    #Slot images
##                Each 'slot##' is holds one image place
##                Image files will be dropped into image.load later
##      Name scheme is a 2D Martix          
    slot00 = pygame.Surface((97, 75))
    slot00 = slot00.convert_alpha()
    slot01 = pygame.Surface((97,75))
    slot01 = slot01.convert_alpha()
    slot02 = pygame.Surface((97,75))
    slot02 = slot02.convert_alpha()
    slot10 = pygame.Surface((97,75))
    slot10 = slot10.convert_alpha()
    slot11 = pygame.Surface((97,75))
    slot11 = slot11.convert_alpha()
    slot12 = pygame.Surface((97,75))
    slot12 = slot12.convert_alpha()
    slot20 = pygame.Surface((97,75))
    slot20 = slot20.convert_alpha()
    slot21 = pygame.Surface((97,75))
    slot21 = slot21.convert_alpha()
    slot22 = pygame.Surface((97,75))
    slot22 = slot22.convert_alpha()
    

    #Buttons?
##            Buttons using Button.py[see import]
##            Button Colours are initialized here
##    ~ Bet Buttons
##        BetButton groups all bet buttons
    betButtons = Buttons.Button()
    bet5 = Buttons.Button()
    bet5Color = activeButton
    bet25 = Buttons.Button()
    bet25Color = activeButton
    bet50 = Buttons.Button()
    bet50Color = activeButton
    bet100 = Buttons.Button()
    bet100Color = activeButton
    bet250 = Buttons.Button()
    bet250Color = activeButton

#      ~ Operation Buttons
    spin = Buttons.Button()
    reset = Buttons.Button()
    close = Buttons.Button()

  #Define page load variables
    clock = pygame.time.Clock()
    keepGoing = True
    
#      ~ Important initial settings variables    
    win = False
    jackwin = False
    error = False
    credit = 100
    jackpot = 500

#      ~ Ensuring all_reels will be an array
    all_lines = [0,0,0,0,0]
    
#      ~ Empty Variables (b/c program breaks without) 
    top_line = ["","",""]
    mid_line = ["","",""]
    bottom_line = ["","",""]
    bet = 0
    winnings = 0
    whichLine = " "
    howWin = " "
    errorMess = " "
    
    # Dropping default image into slot##s
    slot00 = pygame.image.load("spin.png")
    slot01 = pygame.image.load("spin.png")
    slot02 = pygame.image.load("spin.png")
    slot10 = pygame.image.load("spin.png")
    slot11 = pygame.image.load("spin.png")
    slot12 = pygame.image.load("spin.png")
    slot20 = pygame.image.load("spin.png")
    slot21 = pygame.image.load("spin.png")
    slot22 = pygame.image.load("spin.png")
    
#  GamePlay Loop
    while keepGoing:
        clock.tick(30)

        
##            ~ Disable and Enable Bet Buttons
##      (Function Half) --> Error Messages down in if event decision area
##      (Colour Half)
##        If credit below bet amount then disable
##        If credit above bet amount then enable
##            So that the current bet button isn't changed
##            check that it isn't Green (currentButton)
        if credit < 250:
            bet250Color = disableButton
        elif credit >= 250 and bet250Color != currentButton:
            bet250Color = activeButton
        if credit < 100:
            bet100Color = disableButton
        elif credit >= 100 and bet100Color != currentButton:
            bet100Color = activeButton
        if credit < 50:
            bet50Color = disableButton
        elif credit >= 50 and bet50Color != currentButton:
            bet50Color = activeButton
        if credit < 25:
            bet25Color = disableButton
        elif credit >= 25 and bet25Color != currentButton:
            bet25Color = activeButton
        if credit < 5:
            bet5Color = disableButton
        elif credit >= 5 and bet5Color != currentButton:
            bet5Color = activeButton


##          ~ Where decisions are made when things happen!
        for event in pygame.event.get():
                # If the window closes:  stop looping
            if event.type == pygame.QUIT:
                keepGoing = False
        #///////////////////////
        #   MOUSE PRESS EVENT
        #///////////////////////    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                    # If click happens on CLOSE, stop looping
                if close.pressed(pygame.mouse.get_pos()):
                    keepGoing = False

                    # If click occurs in bet button group...
                elif betButtons.pressed(pygame.mouse.get_pos()):
                        # Colour all buttons Purple (default setting)
                    bet5Color = activeButton
                    bet25Color = activeButton
                    bet50Color = activeButton
                    bet100Color = activeButton
                    bet250Color = activeButton
                        # Depending on which button clicked
                        #   The bet matches the button
                        #   & the colour becomes GREEN (current)
                    if bet5.pressed(pygame.mouse.get_pos()):
                        bet = 5
                        bet5Color = currentButton
                    elif bet25.pressed(pygame.mouse.get_pos()):
                        bet = 25
                        bet25Color = currentButton
                    elif bet50.pressed(pygame.mouse.get_pos()):
                        bet = 50
                        bet50Color = currentButton
                    elif bet100.pressed(pygame.mouse.get_pos()):
                        bet = 100
                        bet100Color = currentButton
                    elif bet250.pressed(pygame.mouse.get_pos()):
                        bet = 250
                        bet250Color = currentButton

                    # If click is on RESET...
                elif reset.pressed(pygame.mouse.get_pos()):
                        # Initial Variables reset
                    bet = 0
                    credit = 100
                    jackpot = 500
                    error = False
                    win = False
                    
                        # Default image dropped into slot##s
                    slot00 = pygame.image.load("spin.png")
                    slot01 = pygame.image.load("spin.png")
                    slot02 = pygame.image.load("spin.png")
                    slot10 = pygame.image.load("spin.png")
                    slot11 = pygame.image.load("spin.png")
                    slot12 = pygame.image.load("spin.png")
                    slot20 = pygame.image.load("spin.png")
                    slot21 = pygame.image.load("spin.png")
                    slot22 = pygame.image.load("spin.png")

                        # Bet Buttons return to default (purple)
                    bet5Color = activeButton
                    bet25Color = activeButton
                    bet50Color = activeButton
                    bet100Color = activeButton
                    bet250Color = activeButton
                    
                    # Click on SPIN runs...
                elif spin.pressed(pygame.mouse.get_pos()):

                        # An Error appears if NO BET SELECTED
                    if bet == 0:
                            # error makes error items blit
                        error = True
                        errorMess = "Choose Bet Amount"

                        # If A BET SELECTED ...
                    else:
                            # but NO CREDIT --> error
                        if bet > credit:
                            error = True
                            errorMess = "Not enough Credit"

                            # SUFFICIENT CREDIT --> continue on
                        elif bet <= credit:
                                # Wipes error and win messages off screen
                            error = False
                            win = False
                            jackwin = False

                    #  ~ Initial calculations
                                # Pay the machine
                            credit -= bet
                                # increase JACKPOT by 15% of BET
                            jackpot += bet*.15
                            # is double so 15% of low bets increase the POT
                            

            #////////////////////////////
            #        Spin the Reels
            #////////////////////////////
            # winnings  - prize money from the spin
            # win       - sentinel boolean, runs win_jackpot(), blits win message
            # all_lines - array of arrays, needed for image links
            # whichLine - For output, Tells User which betline they won on
            # howWin    - For output, Tells User which combination they won on
                            winnings, win, all_lines, whichLine, howWin = handle_pull(bet, credit)

                        # ~ Determine the images to be loaded
                                # Split slot Matrix into Rows
                            top_line = all_lines[1]
                            mid_line = all_lines[0]
                            bottom_line = all_lines[2]

                                # Drop file name into image.load
                                # based on Corresponding Index Value
                            slot00 = pygame.image.load(top_line[0])
                            slot01 = pygame.image.load(top_line[1])
                            slot02 = pygame.image.load(top_line[2])
                            slot10 = pygame.image.load(mid_line[0])
                            slot11 = pygame.image.load(mid_line[1])
                            slot12 = pygame.image.load(mid_line[2])
                            slot20 = pygame.image.load(bottom_line[0])
                            slot21 = pygame.image.load(bottom_line[1])
                            slot22 = pygame.image.load(bottom_line[2])
                            
                            if win:
                            #  ~ Call WIN_JACKPOT()
                    # jackpot - is the value of jackpot
                    # jackWinnings - how much User won in win_jackpot() [can be 0]
                    # jackwin - sentinel boolean, blits jackpot win items
                                jackpot, jackWinnings, jackwin = win_jackpot(jackpot, bet)
                                    # (jackWinnings can be 0)
                                winnings += jackWinnings
                                    # Add total Spin Winnings to Credit
                                credit += winnings
    #////////////////////////////////////////////////////////////////
    #               End of If Event run sequence
    #////////////////////////////////////////////////////////////////

    #///////////////////////////////
    #       BLIT EVERYTHING!!!
    #///////////////////////////////

#   ~ Produce text 'labels' by feeding Labels()
            # Dynamic Permanent labels (constant change; always onscreen)
        betLabel = labels("Bet: $" + str(bet))
        creditLabel = labels("Credit: " + str(credit))
        currentJackLabel = labels("Current Jackpot: ")
        jackLabel = labels("$" + str(int(jackpot)))
            # Situational Labels - Any Win
        winningsLabel = labels("You won $" + str(winnings))
        winningLineLabel = labels("Winning Line: ")
        combinationLabel = labels(howWin)
        whichLineLabel = labels(whichLine)
            # Situtaional Labels - JackPot
        jackWinLabel = labels("! ! ! JACKPOT ! ! !")
            # Situational Label - error Message
        errorLabel = labels(errorMess)

    #Blitting background
        betButtons.create_button(screen, bet5Color, 220, 540, 310, 75, 0, " Bets ", (0,0,0))
        screen.blit(background, (0, 0))

    #Blitting bet buttons    
        bet5.create_button(screen, bet5Color, 220, 540, 50, 25, 0, " 5 ", (0,0,0))
        bet25.create_button(screen, bet25Color, 350, 540, 50, 25, 0, " 25", (0,0,0))
        bet50.create_button(screen, bet50Color, 480, 540, 50, 25, 0, " 50", (0,0,0))
        bet100.create_button(screen, bet100Color, 285, 590, 50, 25, 0, "100", (0,0,0))
        bet250.create_button(screen, bet250Color, 415, 590, 50, 25, 0, "250", (0,0,0))

    #Blitting operational buttons
        reset.create_button(screen, (155,255,0), 575, 590, 75, 30, 0, "reset", (0,0,0))
        close.create_button(screen, (255,0,0), 675, 535, 75, 30, 0, "close", (0,0,0))
        spin.create_button(screen, (0,0,255), 940, 530, 100, 100, 0, "SPIN", (0,0,0))

    #Blitting Text
        screen.blit(betLabel, (910,130))
        screen.blit(creditLabel, (900,180))
        if win:
            screen.blit(winningLineLabel, (890, 225))
            screen.blit(combinationLabel, (870, 255))
            screen.blit(whichLineLabel, (910, 280))
            screen.blit(winningsLabel, (910, 350))

    #Jackpot blit area
        screen.blit(currentJackLabel, (890,400))
        screen.blit(jackLabel, (950,430))
        if jackwin:
            screen.blit(jackLight, (420,0))
            screen.blit(jackWinLabel, (500, 30))
            

    #Blitting Slot Images
        screen.blit(slot00, (360,160))
        screen.blit(slot01, (525,160))
        screen.blit(slot02, (690,160))
        screen.blit(slot10, (350,260))
        screen.blit(slot11, (525,260))
        screen.blit(slot12, (700,260))
        screen.blit(slot20, (340,360))
        screen.blit(slot21, (525,360))
        screen.blit(slot22, (710,360))

    #Blit Error Messagebox and Message
        if error:
            screen.blit(messBox, (450,250))
            screen.blit(errorLabel, (490,270))
    
        pygame.display.flip()

if __name__ == "__main__": main()
