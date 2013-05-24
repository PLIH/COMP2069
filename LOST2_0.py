#Source File Name: LOST_2.0.py
#Author's Name: Paige Harvey
#Last Modified By: Paige Harvey
#Last Modified On: 2012-05-22
#Program Description:
#Revision History:
#  - Brand new structure for game
#  - basic skeletal structure (no storyline)

import time

def choosePath():
    path = ""
    while path != "1" and path != "2":
        print ("What will you do? (1 or 2) ")
        path = raw_input()
    return int(path)

#######INTRODUCTION#############
def node0():
    print("In the growing dark you are lost in the woods.")
    time.sleep(2)
    print("You have been following a tree lined foot-path,")
    time.sleep(2)
    print("which has split in two.")
    time.sleep(2)
    print
    print("One path leads into the forest (1),")
    print("The other goes down along a ridge (2).")
    
    chosenPath = choosePath()
    if(chosenPath == 1):
        node1()
    else:
        node2()

def node1():
    print("Finds the house")

    chosenPath = choosePath()
    if(chosenPath == 1):
        node3()
    else:
        node4()

def node2():
    print("Finds the river")

    chosenPath = choosePath()
    if(chosenPath == 1):
        node5()
    else:
        node6()

def node3():
    print("Bypass the house")

    chosenPath = choosePath()
    if(chosenPath == 1):
        outcomes(1)
    else:
        outcomes(2)

def node4():
    print("Enter the house")

    chosenPath = choosePath()
    if(chosenPath == 1):
        outcomes(3)
    else:
        outcomes(4)

def node5():
    print("Ford the River")

    chosenPath = choosePath()
    if(chosenPath == 1):
        outcomes(5)
    else:
        outcomes(6)

def node6():
    print("Run from Cougar")

    chosenPath = choosePath()
    if(chosenPath == 1):
        outcomes(7)
    else:
        outcomes(8)

def outcomes(whichOutcome):
    if(whichOutcome == 1):
        print("Found")
    elif(whichOutcome == 2):
        print("Bear trap")
    elif(whichOutcome == 3):
        print("butchered")
    elif(whichOutcome == 4):
        print("hunted")
    elif(whichOutcome == 5):
        print("sliped")
    elif(whichOutcome == 6):
        print("hypothermia")
    elif(whichOutcome == 7):
        print("washed away")
    else:
        print("rundown")


#######################################
def main():
    playAgain = "yes"

    while playAgain == "yes" or playAgain == "y":
        node0()

    #When round is over, display    
        print("Play Again? (yes or no) ")
        playAgain = raw_input()

if __name__ == "__main__": main()


    
