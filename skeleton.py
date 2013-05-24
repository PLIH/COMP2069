#Name: Paige Harvey
#Assignment 1: Document the Dragon

import random
import time

#NOTE: Make sure you are not using 3.3
#               (Also change input to raw_input)


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
    }

    
##########DECISION ENTRY###################
def choosePath():
    path = ""
    while path != "1" and path != "2":
        print ("What will you do? (1 or 2) ")
        path = input()
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
                print("Quietly, carefully you walk around the house to follow their drive.")
                newNode = 3
            else:
                print("Summoning up your courage you gingerly step up the dilapidated")
                print("porch steps.  Hesitating for only a moment you confidently rap")
                print("upon the front door.")
                newNode = 4

#########isGood for node3
            if(isGood == 1):
                print("It is just as long and twisting, but you know it will")
                print("lead to a road, then to civilization.")
        break;
        case 2:
            if(chosenPath == 1):
                print("Cautiously you approach the natural ford and begin to cross...")
                newNode = 5
            else:
                print("Mindful of the river bank and the near full dark you walk slowly,")
                print("following the river downstream.")
                newNode = 6
        break;
        case 3:
    }

    return newNodeNumber


        
       

############MAIN#####################
def main():
    playAgain = "yes"
    nodeNumber = 0
    
    while playAgain == "yes" or playAgain == "y":
        displayIntro()
        scenarios(nodeNumber)
        chosenPath = choosePath()
        isGood = random.randint(0,1)
        nodeNumber = checkPath(chosenPath, nodeNumber, isGood)


#When round is over, display    
        print("Play Again? (yes or no) ")
        playAgain = input()

if __name__ == "__main__": main()
