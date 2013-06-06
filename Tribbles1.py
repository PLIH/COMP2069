#Source File Name: TribbleTroubles1.py
#Author's Name: Paige Harvey
#Last Modified By: Paige Harvey
#Last Modified On: 2012-05-29
#Program Description: Slot Machine based on Star Trek
#Revision History:
#  - NonGUI working model

import random

def reels():
    betline = [" "," "," "]
    outcome = [0,0,0]

    for spin in range(3):
        outcome[spin] = random.randrange(1,65,1)
        if outcome[spin] >= 1 and outcome[spin] <= 26:
            betline[spin] = "Tribble"
        if outcome[spin] >= 27 and outcome[spin] <= 36:
            betline[spin] = "Redshirt"
        if outcome[spin] >= 37 and outcome[spin] <= 45:
            betline[spin] = "Tricorder"
        if outcome[spin] >= 46 and outcome[spin] <= 53:
            betline[spin] = "Communicator"
        if outcome[spin] >= 54 and outcome[spin] <= 58:
            betline[spin] = "Engineering"
        if outcome[spin] >= 59 and outcome[spin] <=61:
            betline[spin] = "Science"
        if outcome[spin] >= 62 and outcome[spin] <=63:
            betline[spin] = "Command"
        if outcome[spin] == 64:
            betline[spin] = "Enterprise"

    return betline

def check_triple(reel, bet):
    winnings = 0
    win = False
    if reel.count("Redshirt") == 3:
        winnings, win = (bet*20), True
        print("Triple Redshirts!")
    elif reel.count("Tricorder") == 3:
        winnings, win = (bet*30), True
        print("Triple Tricorder")
    elif reel.count("Communicator") == 3:
        winnings, win = (bet*40), True
        print("Triple Communicator")
    elif reel.count("Engineering") == 3:
        winnings, win = (bet*100), True
        print("Triple Engineering")
    elif reel.count("Science") == 3:
        winnings, win = (bet*200), True
        print("Triple Science")
    elif reel.count("Command") == 3:
        winnings, win = (bet*300), True
        print("Triple Command")
    elif reel.count("Enterprise") == 3:
        winnings, win = (bet*1000), True
        print("Triple Enterprise")
        
    return winnings, win

def check_double(reel, bet):
    winnings = 0
    win = False
    if reel.count("Tribble") == 0:
        if reel.count("Redshirt") == 2:
            winnings, win = (bet*2), True
            print("Double Redshirt")
        elif reel.count("Tricorder") == 2:
            winnings, win = (bet*2), True
            print("Double Tricorder")
        elif reel.count("Communicator") == 2:
            winnings, win = (bet*3), True
            print("Double Communicator")
        elif reel.count("Engineering") == 2:
            winnings, win = (bet*4), True
            print("Double Engineering")
        elif reel.count("Science") == 2:
            winnings, win = (bet*5), True
            print("Double Science")
        elif reel.count("Command") == 2:
            winnings, win = (bet*10), True
            print("Double Command")
        elif reel.count("Enterprise") == 2:
            winnings, win = (bet*20), True
            print("Double Enterprise")
        else:
            winnings, win = (bet*2), True   #This is a problem
            print("Line without a Tribble")

    return winnings, win


##########Put this in double_check: will not occur as is.
def check_high(reel, bet):
    winnings = 0
    win = False
    if reel.count("Tribble") == 0:
        if reel.count("Enterprise") == 1:
            winnings, win = (bet*10), True
            print("A Single Enterprise without Tribble")

    return winnings, win
 
def is_num(bet):
    try:
        int(bet)
        return True
    except ValueError:
        print("Please enter a valid number or Q to quit")
        return False

def handle_pull(bet, credit):
    dia_left_reel = [" "," "," "]
    dia_right_reel = [" "," "," "]
    credit -= bet
    
    win = False
    winnings = 0

    #Where all the betlines are given values.
    #The three horizontal reels are randomized with the reels()
    top_reel = reels()
    #mid_reel = ["Enterprise", "Enterprise", "Enterprise"]
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
        winnings, win = check_triple(reel, bet)
        if win == True:
            if reel == mid_reel:
                print("mid reel")
                winnings = winnings * 2     #Center reel x2 multiplier
            elif reel == dia_left_reel or reel == dia_right_reel:
                print("diagonal reels")
                winnings = int(winnings / 2)    #Diagonal reels x.5 multiplier
            return winnings, win
    for reel in all_reels:
        winnings, win = check_double(reel, bet)
        if win == True:
            if reel == mid_reel:
                print("mid reel")
                winnings = winnings * 2     #Center reel x2 multiplier
            elif reel == dia_left_reel or reel == dia_right_reel:
                print("diagonal reels")
                winnings = winnings = int(winnings / 2)    #Diagonal reels x.5 multiplier
            return winnings, win
    for reel in all_reels:
        winnings, win = check_high(reel, bet)
        if win == True:
            if reel == mid_reel:
                print("mid reel")
                winnings = winnings * 2     #Center reel x2 multiplier
            elif reel == dia_left_reel or reel == dia_right_reel:
                print("diagonal reels")
                winnings = winnings = int(winnings / 2)    #Diagonal reels x.5 multiplier
            return winnings, win
    
    return winnings, win

def win_jackpot(jackpot, bet, credit):
    jackpot_attempt = random.randrange(1,51,1)
    jackpot_win = random.randrange(1,51,1)

    jackpot += int(bet*.15)

    print("\n*   Jackpot Drawing   *")

##    print("Attempt:" + str(jackpot_attempt))
##    print("Win: " + str(jackpot_win))

    if jackpot_attempt == jackpot_win:
        print("You won the Jackpot")
        credit += jackpot
        jackpot = 500
    else:
        print("You have not won the jackpot")
    return jackpot, credit


def main():
    winnings = 0
    credit = 1000
    jackpot = 500
    turn = 1
    bet = 0
    prev_bet = 0
    keep_going = True

    while keep_going == True:
        win = False

        #Show the player's information before bet
        print("Credit: " + str(credit))
        print("PrevBet " + str(prev_bet))
        print("Turn " + str(turn))

        #Ask for the bet amount
        prompt = raw_input("Bet amount or 'q' to quit.")
        if (prompt == 'q' or prompt == 'Q'):
            keep_going = False
            break

        #Using the same bet as last turn
        if prompt == "" and turn > 1:
            bet = prev_bet
            print("Using the previous amount")
            if bet > credit:
                print("There's not enough money for this bet.")
            elif bet <= credit:
                credit -= bet
                turn += 1
                prev_bet = bet
                winnings, win = handle_pull(bet, credit)     ##HANDLEPULL()
                credit += winnings
                if win:
                    jackpot, credit = win_jackpot(jackpot, bet, credit)
                
        elif is_num(prompt):
            bet = int(prompt)
            if bet > credit:
                print("There's not enough money for this bet.")
            elif bet <= credit:
                credit -= bet
                turn += 1
                prev_bet = bet
                winnings, win = handle_pull(bet, credit)     ##HANDLEPULL()
                credit += winnings
                if win:
                    jackpot, credit = win_jackpot(jackpot, bet, credit)

        print("\n***************************************\n\n")
        
                
if __name__ == "__main__": main()
