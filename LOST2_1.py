#Source File Name: LOST2_1.py
#Author's Name: Paige Harvey
#Last Modified By: Paige Harvey
#Last Modified On: 2012-05-22
#Program Description: Choose your own adventure.
#Revision History:
#  - StoryLine input

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
    print("You have been following a tree lined foot-path")
    time.sleep(2)
    print("which just split in two.")
    time.sleep(2)
    print
    print("One path leads into the forest (1),")
    time.sleep(2)
    print("The other goes down along a ridge (2).")
    time.sleep(2)
    
    chosenPath = choosePath()
    if(chosenPath == 1):
        node1()
    else:
        node2()

def node1():
    print("Entering the forest ... ")
    time.sleep(2)
    print("You stumble across an old farmhouse.")
    time.sleep(1)
    print("There are dim lights filtering out through the thread-bare curtains.")
    print("The untended garden looks uninviting.")
    print
    time.sleep(4)
    print("Do you attempt to bypass the house unnoticed (1),")
    time.sleep(2)
    print("Or knock on the door? (2) ")
    time.sleep(2)

    chosenPath = choosePath()
    if(chosenPath == 1):
        node3()
    else:
        node4()

def node2():
    print("Stumbling down the ridge path ...")
    time.sleep(2)
    print("You manage to catch youself before tumbling into a dark, wide river.")
    time.sleep(2)
    print("A few metres downriver you think you see a ford.")
    print
    time.sleep(4)
    print("Do you attempt to ford the river (1), ")
    time.sleep(2)
    print("Or follow the river? (2)")
    time.sleep(2)

    chosenPath = choosePath()
    if(chosenPath == 1):
        node5()
    else:
        node6()

def node3():
    print("Quietly, carefully you walk around the house and find their driveway.")
    time.sleep(2)
    print("A driveway means a sure path to civilization!")
    time.sleep(2)
    print("Just as you set your foot on the drive the looming clouds open and a downpour begins.")
    print
    time.sleep(4)
    print("You can walk directly in the rain on the drive (1),")
    time.sleep(2)
    print("Or walk beside the drive under tree cover. (2)")
    time.sleep(2)
    
    chosenPath = choosePath()
    if(chosenPath == 1):
        outcomes(1)
    else:
        outcomes(2)

def node4():
    print("Summoning up your courage you gingerly step up the dilapidated porch steps.")
    time.sleep(2)
    print("Hesitating for only a moment you confidently rap upon the front door.")
    time.sleep(2)
    print("Slowly, foot steps are heard heading towards to door.")
    time.sleep(2)
    print("A look of surprise covers the face of a kindly lady.")
    time.sleep(2)
    print("Behind her you can see a young man, obviously her son.")
    print
    time.sleep(3)
    print("After explaining your situation she invites you in for shelter and food.")
    time.sleep(2)
    print("She seems kind, but the house still doesn't seem right.")
    print
    time.sleep(4)
    print("Do you ignore your gut and enter (1),")
    time.sleep(2)
    print("Or insist on waiting outside and using their phone? (2)")
    time.sleep(2)

    chosenPath = choosePath()
    if(chosenPath == 1):
        outcomes(3)
    else:
        outcomes(4)

def node5():
    print("As you get closer to the ford you notice a series of rocks just ")
    print("above the water line leading directly across.")
    print
    time.sleep(4)
    print("Do you jump from rock to rock, (1)")
    time.sleep(2)
    print("Or wade through the shallow water? (2)")
    time.sleep(2)

    chosenPath = choosePath()
    if(chosenPath == 1):
        outcomes(5)
    else:
        outcomes(6)

def node6():
    print("Mindful of the river bank and the near full dark you walk carefully.")
    time.sleep(2)
    print("In the dark you hear a sound behind you.")
    time.sleep(2)
    print("Turning slowly, you glimpse in the dim moonlight two eyes.")
    time.sleep(3)
    print("A cougar!")
    print
    time.sleep(3)
    print("Do you make a mad dash for the river, (1)")
    time.sleep(2)
    print("Or attempt the trees lining the bank? (2)")
    time.sleep(2)

    chosenPath = choosePath()
    if(chosenPath == 1):
        outcomes(7)
    else:
        outcomes(8)

def outcomes(whichOutcome):
    if(whichOutcome == 1):
        print("Mustering your determination you walk down the drive in the rain.")
        time.sleep(2)
        print("After some time you reach the end of the drive.")
        time.sleep(2)
        print("Following the road...")
        time.sleep(2)
        print("the first car that passes you is a police car.")
        time.sleep(2)
        print("You have been FOUND!")
        time.sleep(2)
    elif(whichOutcome == 2):
        print("Dashing into the trees, you keep the drive in sight and slowly continue on.")
        time.sleep(2)
        print("The drive is long, winding and in ill repair.  Over the thunder you")
        print("can hear what sounds like a truck engine barreling down the drive.")
        time.sleep(4)
        print("Stumbling away from the drive something catches your foot.")
        time.sleep(2)
        print("Looking down you stare unbelievingly at a rusted old bear trap!")
        time.sleep(3)
        print("Your foot is stuck; there is no way to get free.")
        time.sleep(2)
        print("It's full dark, and the truck has long passed you by.")
        time.sleep(2)
        print("In the late autumn rain you are frozen, tired, hungry and now you are bleeding out.")
        time.sleep(2)
        print("Your loss of consciousness is slow and inevitable.")
        time.sleep(2)
        print("You will never be found.  You will remain LOST forever.")
        
    elif(whichOutcome == 3):
        print("Entering the house she informs you that her husband is ")
        print("expected home within the hour, and as such has some warm food ready.")
        time.sleep(3)
        print("Thanking her, you dig in.")
        print
        time.sleep(3)
        print("After the excellent dinner you begin to feel quite tired.")
        time.sleep(2)
        print("She offers an extra bed and a lift into town in the morning.")
        time.sleep(2)
        print("You agree, following her upstairs only to collapse on a soft bed.")
        print
        time.sleep(2)
        print("You open your groggy eyes to an unfamiliar room.")
        time.sleep(2)
        print("Your bed is quite uncomfortable, and for some reason")
        print("you can't move your arms or legs.")
        time.sleep(2)
        print("The kind lady approaches the circle of light in which you are encased.")
        time.sleep(2)
        print("A man, it must be her husband, is at her side.")
        time.sleep(2)
        print("He is wearing a butcher's apron. ")
        time.sleep(2)
        print("They ignore your questions, but your situation soon becomes apparent.")
        time.sleep(2)
        print("They begin to bicker between themselves regarding the ")
        print("best way to prepare and store the 'meat'.")
        print
        time.sleep(4)
        print("As you the man raises his knife you accept that no one is going to ")
        print("know what happened; you'll be missing, LOST forever.")
        
    elif(whichOutcome == 4):
        print("Declining her offer you ask to use their phone and remain on the porch.")
        time.sleep(2)
        print("Waiting on her return you are startled by the sudden appearance of her son.")
        time.sleep(3)
        print("He's in forest camo and holding a hunting rifle.")
        time.sleep(2)
        print("'Run', he says and to motivate you he shoots at your feet. ")
        time.sleep(3)
        print("Shocked, you dash off into the woods around the house.")
        time.sleep(2)
        print("The son following, laughing madly before growing silent at the forest's edge.")
        print
        time.sleep(4)
        print("You zig and zag in the near dark.")
        time.sleep(2)
        print("Near freezing rain begins to fall.")
        time.sleep(2)
        print("The rain, sapping what strength you retain, blurs the landscape, disguising")
        print("the rabbit hole that twists your ankle.")
        time.sleep(4)
        print("A branch cracks behind you, you turn...")
        print
        time.sleep(3)
        print("The son raises his rifle, grinning manically, and shoots your stomach.")
        time.sleep(2)
        print("You put presure on the wound, but your death is inenvitable.")
        time.sleep(2)
        print("The son sits and watches over you, staring avidly.")
        print
        time.sleep(2)
        print("Suddenly, you hear approaching steps.")
        time.sleep(2)
        print("Hope rises within you. Help is coming! You draw breath to yell out...")
        print
        time.sleep(4)
        print("but are cut short when the kind old lady promptly begins to admoish her ")
        print("son for 'spoiling the meat' with an 'unclean shot'.")
        time.sleep(4)
        print("She takes the rifle, and aims it at your head.")
        time.sleep(2)
        print("'They're only good to feed the pigs now. The bones will be LOST amid the muck.'")
        
    elif(whichOutcome == 5):
        print("In the dimming light, you carefully place your foot on each rock.")
        time.sleep(2)
        print("The rocks are slipperier than you first thought, as you begin to lose your balance.")
        time.sleep(3)
        print("Quickly shifting you manage to retain your footing!")
        print
        time.sleep(2)
        print("However, you stretch out too far to make the next rock and slip!")
        time.sleep(2)
        print("Falling, your head collides with one of the stepping rocks.")
        time.sleep(2)
        print("Your unconscious (and soon to be dead) body is LOST down the river.")
        time.sleep(2)
    elif(whichOutcome == 6):
        print("Not trusting the rocks you begin to wade through the cloudy river.")
        time.sleep(2)
        print("While the riverbed is sandy, the river itself is much deeper than you thought.")
        time.sleep(3)
        print("At its deepest the water reaches your chest and worse, it begins to rain.")
        print
        time.sleep(2)
        print("You eventually make it across.")
        time.sleep(2)
        print("But you are so very cold.")
        time.sleep(2)
        print("Perhaps attempting to cross a river this late in November was a poor idea.")
        time.sleep(2)
        print("With the freezing temperatures of the river and rain, ")
        time.sleep(2)
        print("and the dark and cold of night,")
        time.sleep(2)
        print("you begin to feel slow and tired.")
        print
        time.sleep(2)
        print("Knowing the dangers of hypothermia you try to keep moving,")
        time.sleep(2)
        print("but eventually you collapse on the ground...")
        time.sleep(2)
        print("and sleep")
        time.sleep(2)
        print("Somewhere, LOST in your dreams you never wake again.")
        
    elif(whichOutcome == 7):
        print("The sun has fully set and the sky threatens rain.")
        time.sleep(2)
        print("You can hardly see, but you can hear the roaring of the river.")
        time.sleep(3)
        print("The great cat is gaining...")
        time.sleep(2)
        print("you chance a look behind...")
        time.sleep(2)
        print("and trip!")
        time.sleep(1)
        print("Tumbling down and down, head over heels, you crash into the water.")
        time.sleep(4)
        print("The roaring is louder now.")
        time.sleep(3)
        print("The water is moving faster...")
        time.sleep(2)
        print("and faster")
        time.sleep(1)
        print("andfaster")
        print("FASTER")
        time.sleep(3)
        print("WATERFALL")
        time.sleep(4)
        print("With no light, up is down ")
        time.sleep(1)
        print("is right is inside is ")
        time.sleep(1)
        print("rain and rocks and currents and ")
        time.sleep(1)
        print("NOairnoAIRneedSOMEair!!!")
        time.sleep(4)
        print
        print("You are LOST in the basin, caught under the water in the dark.")
        print
        
    else:
        print("The trees!")
        time.sleep(2)
        print("Cougars can't climb trees....  ")
        time.sleep(1)
        print("can't they?")
        print
        time.sleep(2)
        print("You run and run (andrunandrunandrun)")
        time.sleep(2)
        print("The sun is gone and the moon is lost behind rain laden clouds.")
        time.sleep(2)
        print("In the pitch dark you lose your tree.")
        time.sleep(2)
        print("Incrimentally you slow, trying to get your bearings")
        time.sleep(2)
        print("Too slow.")
        time.sleep(2)
        print
        print("The cougar lands on your back, it's teeth at your neck")
        time.sleep(2)
        print("Your aborted scream is LOST upon the desolate forest.")
        print
        


#######################################
def main():
    playAgain = "yes"

    while playAgain == "yes" or playAgain == "y":
        node0()
        time.sleep(5)
    #When round is over, display    
        print("Play Again? (yes or no) ")
        playAgain = raw_input()

if __name__ == "__main__": main()


    
