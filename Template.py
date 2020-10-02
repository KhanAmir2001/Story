import time
def part1():

    print("Loading...")
    time.sleep(1)
    print("...")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    print("...")
    time.sleep(1)
    print("SUCCESSFULLY LOADED")
    print("")
    time.sleep(1)
    print("You see a sign that says `Welcome to Utopia` and walk towards it...")
    print("")
    time.sleep(1)
    input("Press enter to continue...")
    print("")
    print("As you stare at the lonely sign, you notice a world start to evolve")
    time.sleep(1)
    print("")
    print("You watch in awe")
    print("")
    time.sleep(1)
    input("Press enter to continue...")
    print("")
    print("You watch the world slowly start to load in...")
    time.sleep(1)
    print("")
    print("You either stay with the sign or explore")
    print("")
    time.sleep(1)
    option = 0
    while option != "1" or option != "2":
        print("Press 1 to stay with the sign")
        print("Press 2 to explore")
        option = input(":")
        if option == "1" or option == "2":
            break
    if option == "1":
        loop1 = True
    else:
        loop1 = False
    if loop1 == True:
        time.sleep(0.5)
        print("You stay with the sign...")
        time.sleep(1)
        print("")
        print("You watch an entire forest grow before your very eyes.")
        time.sleep(2)
        print("")
        print("The trees grow tall and eventually the sign is entangled in the dense undergrowth of the forest floor.")
        time.sleep(4)
        print("")
        print("The lianas and creepers dominate the forest floor. The trees tower high above you as it were some sort of competition.")
        time.sleep(4)
        print("")
        print("Light is barely getting down to you, you start to feel worried...")
        print("")
        time.sleep(1)
        input("Press enter to continue...")
        print("")
        time.sleep(0.5)
        print("You see movement in the trees and you feel uncomfortable.")
        time.sleep(3)
        print("")
        print("You try to walk away but the forest seems to go on forever...")
        time.sleep(3)
        print("")
        print("Your walk turns into a run as you try to find an escape from this never-ending biome.")
        time.sleep(3)
        print("")
        print("You keep hearing life within the bushes and you run faster...")
        time.sleep(0.5)
        print("")
        input("Press enter to continue...")
        print("")
        time.sleep(1)
        print("Finally, an opening. You dive through the hole before the world closes it off from the rest of the universe.")
        time.sleep(4)
        print("")
        print("What you see before you amazes you... Beaches, rivers, rocky mountains, long open plains...")
        time.sleep(4)
        print("")
        print("You are frozen in awe as you continue to watch the world materialise in front of you...")
        time.sleep(1)
        print("")
        input("Press enter to continue...")
        print("")
    else:
        time.sleep(0.5)
        print("")
        print("You leave the sign behind to explore this new world growing before you.")
        time.sleep(1)
        print("")
        print("Trees, forests, beaches, rivers. You gaze in amazement as a whole ecosystem renders in around you.")
        time.sleep(1)
        print("")
        input("Press enter to continue...")
        print("")
    print("The world comes into view bit by bit.")
    time.sleep(2)
    print("")
    print("Large towering mountains, vast golden sands, largo open meadows... You've never seen such beauty...")
    print("")
    time.sleep(4)
    print("You have always wanted to live in a world like this... You feel happy.")
    print("")
    input("Press enter to continue...")
    time.sleep(0.5)
    print("")
    print("You feel honoured to live in a world as advanced as this.")
    time.sleep(3)
    print("")
    print("")
    print("")
    print("")
    print("")
    print("Many years later...")
    print("")
    time.sleep(2)
    print("The world still looks as new as when it was created.")
    print("")
    time.sleep(2)
    print(
        "The world still looks as new as when it was created. The rocky mountains still tower tall, the beaches are still golden, the meadows are still unspoiled.")
    time.sleep(2)
    print("")
    print("Nothing has changed... You feel as if the creators have given up on you...")
    time.sleep(4)
    print("")
    input("Press enter to continue...")
    time.sleep(1)
    print("")
    print("After years of nothingness, one day changes it all...")
    time.sleep(2)
    print("")
    print("Suddenly, the rocky mountains start to dissolve...")
    time.sleep(2)
    print("...the forests start to shrink...")
    time.sleep(2)
    print("...the golden sands start to recede...")
    time.sleep(2)
    print("...the meadow starts to turn into a wasteland...")
    print("")
    time.sleep(2)
    print("You look up and see those oh-so-familiar words emblazoned in the sky...")
    time.sleep(4)
    print("")
    print("")
    print("")
    print("")
    print("RESTARTING")

    return()

def part2():
        print("You awake in an area you dont seem to recognise")
        print("It's pitch black and filled with emptiness.")
        input()
        
        print("In the distance you hear scurrying - lots and lots of scurrying")
        print("getting closer and louder as the noise echoes off the walls.")
        input()
        
        print("Something about this feels as if its happened before.")
        print("You can not see... you decide you can either")
        input()
        
        option = 0
        while option != "1" or option != "2":
            print("Press 1 to attempt to run.")
            print("Press 2 to head towards the noise.")
            option = input("")
            if option == "1" or option == "2":
                break
        if option == "1":
            print("You attempt to navigate away from the sound however you realise nothing exists beyond this point.")
            print("You almost fall off the edge of whatever it is your standing on.")
            print("You face no choice but to head towards the noise")
            input()

        print("You head towards the scurrying. You can not see and it is your only sense of direction.")
        print("As you do you begin to notice a light but its not stationary - quite the opposite,")
        print("in fact it's rushing towards you.")
        input()

        print("The light reveals you are in a cave of some sorts")
        print("and seemingly quite deep in")
        input()

        print("Without much time to contemplate you are distracted,")
        print("the hoard of scurrying has arrived revealing itself to you.")
        input()

        print("Huge spiders at least 4 times the size of you are rushing")
        print("directly towards you all carrying large chunks of information")
        print("on their backs")
        input()

        while option != "1" or option != "2":
            print("Press 1 to attempt to run to cover.")
            print("Press 2 to attempt to fight.")
            option = input("")
            if option == "1" or option == "2":
                break
        if option == "2":
            print("You attempt to attack the spiders by grabbing something")
            print("off one of their backs and swinging it as hard as you can")
            input()
            print("However on impact the spider is completely unphased in fact")
            print("not a single one acknowledges anything you did nor even you")
            print("as a person")
            input()
            print("Some bardge into you on their way but it seems they dont care")
            print("at all what you do, they all focus on their larger cause")
            input()
            print("They are all constructing something... something beautiful")
            print("They are creating portals to other worlds but they all seem incomplete")
            input()
            print("The last thing you wonder is if you caused this what did you")
            print("take from them")
            input()
            print("As you wonder the whole world stops.")
            print("A command comes from above F5")
            input()
            part2()
        print("You hide behind some rocks and watch as the spider constructs")
        print("a series of portals using the information carried on their backs")
        input()
        print("There is something beautiful about the simple nature of their")
        print("dedication to their work.")
        input()
        print("You are able to watch as they work with amazing efficiency,")
        print("never once getting in eithers way.")
        input()
        print("Once they construct all of them there is a brief moment of nothing")
        print("before one glows as if it was selected")
        input()
        print("It seems as if your world is going into that portal,")
        print("what wouldve happened had you stopped the spiders.")
        print("Did you bless the world or curse it?")
        input()
        
        return()

def part3():
        option = 0
        print("Loading...")
        print("Loading...")
        print("Loading...")
        input("Press enter to continue...")
        print("")
        print("You awake in a darkened room with a single fluorescent light dangling from the ceiling from a bare wire, shining right over you, stinging your eyes. You squint as you look into the distance. You cannot see any walls or the ceiling. Piles upon piles of pre-owned objects are spread out as far as you can see.")
        input("Press enter to continue...")
        print("")
        print("A quiet roar of voices can be heard in the distance chanting numbers. You can't tell where they come from. Another sign stands tall in front of you, this one saying 'Sell your used items'.")
        print("")
        while option != "1" or option != "2":
            print("Press 1 to investigate the numbers.")
            print("Press 2 to investigate the site.")
            option = input("")
            if option == "1" or option == "2":
                break
        if option == "1":
            print("You look up, to see giant floating numbers, seemingly assigned to each object. They vanish as fast as they appear: '50', '100', '120'. With each disappearance, the voices grow louder.")
            input("Press enter to continue...")
            print("")
            print("Suddenly, the voices stop. The numbers stop appearing. A computer forces its way out of the mess and floats upwards. It keeps going until it cannot be seen. Once it's gone, vast numbers of objects clatter around you, most of which are technological. A TV, a fridge and a dishwasher land with a deafening crash.")
            input("Press enter to continue...")
            print("")
        if option == "2":
            print("You look around the area. Objects have been placed seemingly without a care. Some of these objects are surrounded by voices and prices. More objects pop into existence, and they don't stop coming.")
            input("Press enter to continue...")
            print("")
            print("Vast numbers of objects clatter around you, most of which are technological. A derelict car leaking oil sits next to a frayed and worn sofa. A TV, a fridge and a dishwasher land with a deafening crash next to you.")
            input("Press enter to continue...")
            print("")
        print("And with them, the voices grew louder. Price values grow larger and more frequent, more objects fall and crash from all directions as others soar upwards.")
        input("Press enter to continue...")
        print("")
        print("Your head spins. The endless cacophony buries itself into your head and clutches you, refusing to let go. You don't want to be here anymore, you don't belong here in a place for the dead and unwanted.")
        print("The already dark room grows black along with a feeling that you are no longer alone, as you slowly lose consciousness once more.")
        input("Press enter to continue...")
        print("")
        print("RESTARTING")

        return()

def part4():

    return()

def part5():

        print('\n"Loading"')
        print('"Loading"')
        print('"Loading"\n')
        print('"Successfully loaded"')

        input("\nPress enter to continue...\n")

        print("You open your eyes onto a new World.\nIt says welcome to Fackbook.com.\nYou look around only to find there's no room - it's absolutely crowded\n")

        input("Press enter to continue...\n")

        print("You see all sorts of stuff in this world.\nThere are a lot pictures with text on them - they call them memes or something of the sort.\nYou can hear people talking to each other from all over the world - it's really impressive.\n")

        input("Press enter to continue...\n")

        print("Wait what is happening? The world is slowing down, you can see empty boxes - they used to be images of people.\n")
        print("What is going on?!\n") 
        print("I'm frozen!\n")

        print("Some kind of message appears...\n")
        print('"Warning: the site is experiencing some technical difficulties.\nPlease hold on while our engineers work to fix the issue - :D\n"')
        input("Press enter to continue...\n")
        print("You wait for a bit\n")
        input("Press enter to continue...\n")
        print('"Warning: the site has officially shut down due to a DDOS attack.\nWe are sorry of the inconvenience.\nPlease accept our apologies and try later today or tomorrow"')
        

        return()

part1()
part2()
part3()
part4()
part5()
