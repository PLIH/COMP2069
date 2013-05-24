#Source File Name: LOST_0.3.py
#Author's Name: Paige Harvey
#Last Modified By: Paige Harvey
#Last Modified On: 2012-05-16
#Program Description:
#Revision History:

import random
import time


#######INTRODUCTION#############
def displayIntro():
    print("In the growing dark you are lost in the woods.")
    print("You have been following a tree lined foot-path,")
    print("which has split in two.")

##########PRESENT SCENARIOS AND TEXT############
def scenarios(nodeNumber):
    switch(nodeNumber) {
    case 0:
        print("One path leads into the forest (1),")
        print("The other goes down along a ridge (2)")
    break;
    case 1:
        print("Do you attempt to bypass the house unnoticed (1),")
        print("Or knock on the door? (2) ")
    break;
    case 2:
        print("Do you attempt to ford the river (1), ")
        print("Or follow the river? (2)")
    break;
    case 3:
        print("You can walk directly in the rain on the drive (1),")
        print("Or walk beside the drive under tree cover. (2)")
    break;
    case 4:
        print("Do you ignore your gut and enter (1),")
        print("Or insist on waiting outside and using their phone? (2)")
    break;
    case 5:
        print("Do you jump from rock to rock, (1)")
        print("Or wade through the shallow water? (2)")
    break;
    case 6:
        print("Do you make a mad dash for the river, (1)")
        print("Or attempt the trees lining the bank? (2)")
    break;
    }
    #And then the player makes their decision.
    path = ""
    while path != "1" and path != "2":
        print ("What will you do? (1 or 2) ")
        path = raw_input()
    return path

##########CONSEQUENCES###################
def checkPath(chosenPath, nodeNumber, isGood):
    switch(nodeNumber) {
        case 0:
            if(chosenPath == 1):
                print("Entering the forest ... ")
            else:
                print("Heading down the ridge path ...")
            if(isGood == 1):
                print("You stumble across an old farmhouse. There")
                print("are dim lights filtering out through the ")
                print("thread-bare curtains. The untended garden looks")
                print("uninviting.")
                newNode = 1
            else:
                print("You continue along, stumbling in the growing dark. You ")
                print("manage to catch youself before walking into a dark, wide ")
                print("river.  A few metres downriver you think you see a ford.")
                newNode = 2
        break;
        case 1:
            if(chosenPath == 1):
                print("Quietly, carefully you walk around the house and find their driveway.")
                print("A driveway means a sure path to civilization!  Just as you set your ")
                print("foot on the drive the looming clouds open and a downpour begins.")
                newNode = 3
            else:
                print("Summoning up your courage you gingerly step up the dilapidated")
                print("porch steps.  Hesitating for only a moment you confidently rap")
                print("upon the front door.")
                time.sleep(2)
                print("Slowly foot steps are heard heading towards to door. Which then")
                print("begins to swing open.  A look of surprise covers the face of a ")
                print("kindly lady. Behind her you can see a young man, obviously her son.")
                time.sleep(2)
                print("After explaining your situation she invites you in for shelter and ")
                print("food. She seems kind, but the house still doesn't seem right.")
                newNode = 4
        break;
        case 2:
            if(chosenPath == 1):
                print("As you get closer to the ford you notice a series of rocks just ")
                print("above the water line leading directly across.")
                newNode = 5
            else:
                print("Mindful of the river bank and the near full dark you walk slowly,")
                print("following the river downstream. In the dark you hear a sound behind ")
                print("you.  Turning slowly, you glimpse in the dim moonlight two eyes.")
                time.sleep(2)
                print("A cougar!")
                newNode = 6
        break;
        case 3: #The outcomes in this node are RANDOMIZED.
            if(chosenPath == 1):
                print("Mstering you determination you walk down the drive in the rain.")
            else:
                print("Dashing into the trees, you keep the drive in sight and continue.")
        #The one good outcome.
            if(isGood == 1):
                print("After some time you reach the end of the drive.  Following the road")
                print("the first car that passes you is a police car.")
                print("You have been FOUND!")
                time.second(2)
            else:
                print("The drive is long, winding and in ill repair.  Over the thunder you")
                print("can hear what sounds like a truck engine barreling down the drive.")
                print("Stumbling away from the drive something catches your foot.")
                print("Looking down you stare unbelievingly at a rusted old bear trap!")
                time.second(4)
                print("Your foot is stuck; there is no way to get free. It's full dark,")
                print("and the truck has long passed you by.  In the late autumn rain ")
                print("you are frozen, tired, hungry and now you are bleeding out.")
                time.second(2)
                print("Your loss of consciousness is slow and inevitable.  You will never")
                print("be able to be found.  You will remain LOST forever.")
            newNode = 7
        break;
        case 4:
            if(chosenPath == 1):
                print("Surely this kind old lady has no nefarious purpose. Entering the ")
                print("house she informs you that her husband is expected home within the ")
                print("hour, and as such has some warm food ready.  Thanking her, you dig ")
                print("in. After the excellent dinner you begin to feel quite tired. She")
                print("offers an extra bed and a lift into town in the morning.")
                time.second(4)
                print("You open your groggy eyes to an unfamiliar room. Your bed is quite")
                print("uncomfortable, and for some reason you can't move your arms or legs.")
                time.second(2)
                print("The kind lady approaches the circle of light in which you are encased.")
                print("A man, it must be her husband, is at her side.  He is wearing a butcher's")
                print("apron. They ignore your questions, but an idea of your situation grows in")
                print("your mind when they begin to bicker between themselves regarding the ")
                print("best way to prepare and store the 'meat'.")
                time.second(4)
                print("As you the man raises his knife you accept that no one is going to ")
                print("know what happened; you'll be missing, LOST forever.")
            else:
                    #Son hunts for sport, mother and father admonish for 'spoiling' the meat.
                print("Declining her offer you ask to use their phone and remain on the porch.")
                print("Waiting on her to return you are startled by the sudden appearance ")
                print("of her son. He's in forest camo and holding a hunting rifle.")
                time.seond(2)
                print("'Run', he says and to motivate you he shoots at your feet. Shocked")
                print("you dash off into the woods around the house. The son following, ")
                print("laughing madly before growing silent at the forest's edge.")
                time.second(4)
                print("You zig and zag in the near dark.  Near freezing rain begins to fall.")
                print("The rain, sapping what strength you retain, blurs the landscape, disguising")
                print("the rabbit hole that twists your ankle. 
    }

    return newNodeNumber

##############OUTCOMES#################
def outcomes(nodeNumber, isGood):
    

        
       

############MAIN#####################
def main():
    playAgain = "yes"
    
    while playAgain == "yes" or playAgain == "y":
        displayIntro()
        nodeNumber = 0
        while gameplay == "yes":
    #scenarios displays decisions, and takes the player's choice        
            chosenPath = scenarios(nodeNumber)
    #isGood decides if the situation will be 'good' or 'bad'
            isGood = random.randint(0,1)
    #And the outcome of the decision is dispayed.  Player advances to next node
            nodeNumber = checkPath(chosenPath, nodeNumber, isGood)
            
#When round is over, display    
        print("Play Again? (yes or no) ")
        playAgain = raw_input()

if __name__ == "__main__": main()
