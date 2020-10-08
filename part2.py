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
part2()
