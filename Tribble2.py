#Source File Name: Tribble2.py
#Author's Name: Paige Harvey
#Last Modified By: Paige Harvey
#Last Modified On: 2012-06-05
#Program Description: Slot Machine based on Star Trek
#Revision History:
#  - GUI integration

import pygame, Buttons, random

##                    Buttons.py was NOT written by Paige Harvey
##                        It was written by Simon H. Larsen,
##                        who then made it avaliable for download,
##                        which was linked to PYGAME.org.
##                    P Harvey downloaded it on June 3, 2013.
##
##                !~ REPEAT ~!
##                    P Harvey did NOT write Buttons.py

def reels():
    betline = [" "," "," "]
    outcome = [0,0,0]

    for spin in range(3):
        outcome[spin] = random.randrange(1,129,1)
        if outcome[spin] >= 1 and outcome[spin] <= 26:
            betline[spin] = "Tribble.png"
        if outcome[spin] >= 27 and outcome[spin] <= 36:
            betline[spin] = "Redshirt.png"
        if outcome[spin] >= 37 and outcome[spin] <= 45:
            betline[spin] = "Tricorder.png"
        if outcome[spin] >= 46 and outcome[spin] <= 53:
            betline[spin] = "Communicator.png"
        if outcome[spin] >= 54 and outcome[spin] <= 58:
            betline[spin] = "Engineering.png"
        if outcome[spin] >= 59 and outcome[spin] <=61:
            betline[spin] = "Science.png"
        if outcome[spin] >= 62 and outcome[spin] <=63:
            betline[spin] = "Command.png"
        if outcome[spin] == 64:
            betline[spin] = "Enterprise.png"

    return betline

def check_triple(reel, bet):
    winnings = 0
    howWin = " "
    win = False
    if reel.count("Redshirt.png") == 3:
        winnings, win = (bet*20), True
        howWin = "Triple Redshirts!"
    elif reel.count("Tricorder.png") == 3:
        winnings, win = (bet*30), True
        howWin = "Triple Tricorder"
    elif reel.count("Communicator.png") == 3:
        winnings, win = (bet*40), True
        howWin = "Triple Communicator"
    elif reel.count("Engineering.png") == 3:
        winnings, win = (bet*100), True
        howWin = "Triple Engineering"
    elif reel.count("Science.png") == 3:
        winnings, win = (bet*200), True
        howWin = "Triple Science"
    elif reel.count("Command.png") == 3:
        winnings, win = (bet*300), True
        howWin = "Triple Command"
    elif reel.count("Enterprise.png") == 3:
        winnings, win = (bet*1000), True
        howWin = "Triple Enterprise"
        
    return winnings, win, howWin

def check_double(reel, bet):
    winnings = 0
    howWin = " "
    win = False
    if reel.count("Tribble.png") == 0:
        if reel.count("Redshirt.png") == 2:
            winnings, win = (bet*2), True
            howWin = "Double Redshirt"
        elif reel.count("Tricorder.png") == 2:
            winnings, win = (bet*2), True
            howWin = "Double Tricorder"
        elif reel.count("Communicator.png") == 2:
            winnings, win = (bet*3), True
            howWin = "Double Communicator"
        elif reel.count("Engineering.png") == 2:
            winnings, win = (bet*4), True
            howWin = "Double Engineering"
        elif reel.count("Science.png") == 2:
            winnings, win = (bet*5), True
            howWin = "Double Science"
        elif reel.count("Command.png") == 2:
            winnings, win = (bet*10), True
            howWin = "Double Command"
        elif reel.count("Enterprise.png") == 2:
            winnings, win = (bet*20), True
            howWin = "Double Enterprise"
        elif reel.count("Enterprise.png") == 1:
            winnings, win = (bet*10), True
            howWin = "One Enterprise"
        else:
            winnings, win = (bet*2), True
            howWin = "No Tribble"

    return winnings, win, howWin

def win_jackpot(jackpot, bet, credit):
    jackwin = False
    jackpot_attempt = random.randrange(1,51,1)
    jackpot_win = random.randrange(1,51,1)

    jackpot += int(bet*.15)

    print("\n*   Jackpot Drawing   *")

##    print("Attempt:" + str(jackpot_attempt))
##    print("Win: " + str(jackpot_win))

    if jackpot_attempt == jackpot_win:
        jackwin = True
        print("You won the Jackpot")
        credit += jackpot
        jackpot = 500
    else:
        print("You have not won the jackpot")
    return jackpot, credit, jackwin

def handle_pull(bet, credit):
    whichReel = "None"
    dia_left_reel = [" "," "," "]
    dia_right_reel = [" "," "," "]
    credit -= bet
    
    win = False
    winnings = 0

    #Where all the betlines are given values.
    #The three horizontal reels are randomized with the reels()
    top_reel = reels()
    #mid_reel = ["Redshirt", "Enterprise", "Tricorder"]
    mid_reel = reels()
    bottom_reel = reels()
    #The diagonal reels are based on the horizontal reels
    dia_left_reel[0] = top_reel[0]
    dia_left_reel[1] = mid_reel[1]
    dia_left_reel[2] = bottom_reel[2]
    dia_right_reel[0] = top_reel[2]
    dia_right_reel[1] = mid_reel[1]
    dia_right_reel[2] = bottom_reel[0]

    all_reels = [mid_reel, top_reel, bottom_reel, dia_left_reel, dia_right_reel]

    #Show the reels
    print(top_reel[0] +" - "+ top_reel[1] +" - "+ top_reel[2])
    print(mid_reel[0] +" - "+ mid_reel[1] +" - "+ mid_reel[2])
    print(bottom_reel[0] +" - "+ bottom_reel[1] +" - "+ bottom_reel[2])

    for reel in all_reels:
        winnings, win, howWin = check_triple(reel, bet)
        if win == True:
            if reel == mid_reel:
                whichReel = "Middle Reel"
                winnings = winnings * 2     #Center reel x2 multiplier
            elif reel == dia_left_reel: 
                whichReel = "Diagonal Left"
                winnings = int(winnings / 2)    #Diagonal reels x.5 multiplier
            elif reel == dia_right_reel:
                whichReel = "Diagonal Right"
                winnings = int(winnings / 2)    #Diagonal reels x.5 multiplier
            elif reel == top_reel:
                whichReel = "Top Reel"
            else:
                whichReel = "Bottom Reel"
            return winnings, win, all_reels, whichReel, howWin
        
    for reel in all_reels:
        winnings, win, howWin = check_double(reel, bet)
        if win == True:
            if reel == mid_reel:
                whichReel = "Middle Reel"
                winnings = winnings * 2     #Center reel x2 multiplier
            elif reel == dia_left_reel:
                whichReel = "Diagonal Left"
                winnings = int(winnings / 2)    #Diagonal reels x.5 multiplier
            elif reel == dia_right_reel:
                whichReel = "Diagonal Right"
                winnings = int(winnings / 2)    #Diagonal reels x.5 multiplier
            elif reel == top_reel:
                whichReel = "Top Reel"
            else:
                whichReel = "Bottom Reel"
            return winnings, win, all_reels, whichReel, howWin
        
    return winnings, win, all_reels, whichReel, howWin

def labels(toPrint):
    font = pygame.font.Font("ArchitectsDaughter.ttf", 20)
    label = font.render(toPrint, 1, (0,0,0))
    return label

def main():
    pygame.init()
    #Global local variables(?) [Colours will never change values.]
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
    betButtons = Buttons.Button()
    bet1 = Buttons.Button()
    bet1Color = activeButton
    bet25 = Buttons.Button()
    bet25Color = activeButton
    bet50 = Buttons.Button()
    bet50Color = activeButton
    bet100 = Buttons.Button()
    bet100Color = activeButton
    bet250 = Buttons.Button()
    bet250Color = activeButton
    spin = Buttons.Button()
    reset = Buttons.Button()
    close = Buttons.Button()

#Define run variables
    clock = pygame.time.Clock()
    top_reel = ["","",""]
    mid_reel = ["","",""]
    bottom_reel = ["","",""]
    all_reels = [0,0,0,0,0]
    keepGoing = True
    jackwin = False
    error = False
    bet = 0
    credit = 100
    jackpot = 500
    winnings = 0
    whichReel = " "
    howWin = " "
    errorMess = " "

    slot00 = pygame.image.load("spin.png")
    slot01 = pygame.image.load("spin.png")
    slot02 = pygame.image.load("spin.png")
    slot10 = pygame.image.load("spin.png")
    slot11 = pygame.image.load("spin.png")
    slot12 = pygame.image.load("spin.png")
    slot20 = pygame.image.load("spin.png")
    slot21 = pygame.image.load("spin.png")
    slot22 = pygame.image.load("spin.png")
    

    while keepGoing:
        win = False
        clock.tick(30)

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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                winnings = 0
                if close.pressed(pygame.mouse.get_pos()):
                    keepGoing = False
                elif betButtons.pressed(pygame.mouse.get_pos()):
                    bet1Color = activeButton
                    bet25Color = activeButton
                    bet50Color = activeButton
                    bet100Color = activeButton
                    bet250Color = activeButton
                    if bet1.pressed(pygame.mouse.get_pos()):
                        bet = 1
                        bet1Color = currentButton
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
                elif reset.pressed(pygame.mouse.get_pos()):
                    bet = 0
                    credit = 100
                    error = False
                    jackpot = 500
                    
                    slot00 = pygame.image.load("spin.png")
                    slot01 = pygame.image.load("spin.png")
                    slot02 = pygame.image.load("spin.png")
                    slot10 = pygame.image.load("spin.png")
                    slot11 = pygame.image.load("spin.png")
                    slot12 = pygame.image.load("spin.png")
                    slot20 = pygame.image.load("spin.png")
                    slot21 = pygame.image.load("spin.png")
                    slot22 = pygame.image.load("spin.png")
                    
                    bet1Color = activeButton
                    bet25Color = activeButton
                    bet50Color = activeButton
                    bet100Color = activeButton
                    bet250Color = activeButton
            #When the SPIN is pressed the program RUNS!!!
                elif spin.pressed(pygame.mouse.get_pos()):
                #If no Bet has been selected a message appears
                    if bet == 0:
                        error = True
                        errorMess = "Choose Bet Amount"
                    else:
                #The program runs
                        if bet > credit:
                            error = True
                            errorMess = "Not enough Credit"
                        elif bet <= credit:
                            error = False
                            credit -= bet
                            winnings, win, all_reels, whichReel, howWin = handle_pull(bet, credit)
                            credit += winnings 
                            
                            top_reel = all_reels[1]
                            mid_reel = all_reels[0]
                            bottom_reel = all_reels[2]

                            #image creation here.
                            slot00 = pygame.image.load(top_reel[0])
                            slot01 = pygame.image.load(top_reel[1])
                            slot02 = pygame.image.load(top_reel[2])
                            slot10 = pygame.image.load(mid_reel[0])
                            slot11 = pygame.image.load(mid_reel[1])
                            slot12 = pygame.image.load(mid_reel[2])
                            slot20 = pygame.image.load(bottom_reel[0])
                            slot21 = pygame.image.load(bottom_reel[1])
                            slot22 = pygame.image.load(bottom_reel[2])
                            
                            if win:
                                jackpot, credit, jackwin = win_jackpot(jackpot, bet, credit)
        
        
        errorLabel = labels(errorMess)
        betLabel = labels("Bet: $" + str(bet))
        creditLabel = labels("Credit: " + str(credit))
        winningsLabel = labels("You won $" + str(winnings))
        winningReelLabel = labels("Winning Reel: ")
        combinationLabel = labels(howWin)
        whichReelLabel = labels(whichReel)
        currentJackLabel = labels("Current Jackpot: ")
        jackLabel = labels("$" + str(jackpot))
        jackWinLabel = labels("! ! ! JACKPOT ! ! !")

    #Blitting background
        betButtons.create_button(screen, bet1Color, 220, 540, 310, 75, 0, " Bets ", (0,0,0))
        screen.blit(background, (0, 0))

    #Blitting bet buttons    
        bet1.create_button(screen, bet1Color, 220, 540, 50, 25, 0, " 1 ", (0,0,0))
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
        if winnings != 0:
            screen.blit(winningReelLabel, (890, 225))
            screen.blit(combinationLabel, (870, 255))
            screen.blit(whichReelLabel, (910, 280))
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
