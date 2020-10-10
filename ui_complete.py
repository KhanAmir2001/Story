from tkinter import *

x = -1
y = 0
choice = 0

window = Tk()

window.title("Python Story")

window.geometry('700x400')

lbl = Label(window, text="Welcome to our story.")

lbl.pack()

def clicked():# runs when button is clicked

    line = ["Loading...",
            "SUCCESSFULLY LOADED.",#contains all text of main routes note doesnt keep alternate choices
            "You see a sign that says `Welcome to Utopia` and walk towards it...",
            "As you stare at the lonely sign, you notice a world start to evolve.",
            "You watch in awe.",
            "You watch the world slowly start to load in...",
            "Stay with the sign, or explore?",
            "You stay with the sign...",
            "You watch an entire forest grow before your very eyes.",
            "The trees grow tall and eventually the sign is entangled in the dense undergrowth of the forest floor.",
            "The lianas and creepers dominate the forest floor. The trees tower high above you as it were some sort of competition.",
            "Light is barely getting down to you, you start to feel worried.",
            "You see movement in the trees and you feel uncomfortable.",
            "You try to walk away but the forest seems to go on forever.",
            "Your walk turns into a run as you try to find an escape from this never-ending biome.",
            "You keep hearing life within the bushes and you run faster.",
            "Finally, an opening. You dive through the hole before the world closes it off from the rest of the universe.",
            "What you see before you amazes you... Beaches, rivers, rocky mountains and long open plains.",
            "You are frozen in awe as you continue to watch the world materialise in front of you...",
            "The world comes into view bit by bit.",
            "Large towering mountains, vast golden sands, largo open meadows... You've never seen such beauty...",
            "You have always wanted to live in a world like this... You feel happy.",
            "You feel honoured to live in a world as advanced as this.",
            "Many years later...",
            "The world still looks as new as when it was created.",
            "The rocky mountains still tower tall, the beaches are still golden, the meadows are still unspoiled.",
            "Nothing has changed... You feel as if the creators have given up on you...",
            "After years of nothingness, one day changes it all...",
            "Suddenly, the rocky mountains start to dissolve...",
            "...the forests start to shrink...",
            "...the golden sands start to recede...",
            "...the meadow starts to turn into a wasteland...",
            "You look up and see those oh-so-familiar words emblazoned in the sky...",
            "...",
            "RESTARTING"]

    global x #uses global x to keep the list progressing when button is pressed
    x = x+1

    if x == 6: #use this part to create 2 buttons on the appropriate line change the number depending
        btn.pack_forget()
        choice1.pack()#shows 2 choice buttons
        choice2.pack()
    if x == 35:
        btn.pack_forget()
        p2btn.pack()
        x=-1
    if x < 36:
        print("x is ",x)#debug purposes tracks list
        res = line[x]
        lbl.configure(text= res)

def sidetrack():#run from alternate button follows alternate path then goes back to main story
    global y
    print("y =",y)
    if y == 2:
        global x
        x = 18
        btn2.pack_forget()
        btn.pack()
        y=0
        return()
    line = ["You leave the sign behind to explore this new world growing before you.",
            "Trees, forests, beaches, rivers. You gaze in amazement as a whole ecosystem renders in around you."]
    res = line[y]
    lbl.configure(text = res)
    y = y+1

btn = Button(window, text="Click Me", command=clicked,)
btn2 = Button(window, text="Click me", command=sidetrack)

def option1():
    global choice
    choice = 1
    btn.pack()
    choice1.pack_forget()
    choice2.pack_forget()
    global x
    x=7
    
def option2():
    
    global choice
    choice = 2
    btn2.pack()
    choice1.pack_forget()
    choice2.pack_forget()
    global x
    x=18
btn.pack()
choice1 = Button(window, command=option1, text="Stay with the sign")
choice2 = Button(window, command=option2, text="Explore")




#-----------------------------------------------------PART2-----------------------------------------------------




def p2clicked():# runs when button is clicked
    line = ["You awake in an area you dont seem to recognise", #contains all text of main routes note doesnt keep alternate choices
            "It's pitch black and filled with emptiness.",
            "In the distance you hear scurrying - lots and lots of scurrying",
            "getting closer and louder as the noise echoes off the walls.",
            "You can not see... you decide you can either",
            "You head towards the scurrying. You can not see and it is your only sense of direction.", #5 choice 
            "As you do you begin to notice a light but its not stationary - quite the opposite,",
            "The light reveals you are in a cave of some sorts",
            "and seemingly quite deep in",
            "Without much time to contemplate you are distracted,",
            "the hoard of scurrying has arrived revealing itself to you.",
            "Huge spiders at least 4 times the size of you are rushing",
            "directly towards you all carrying large chunks of information",
            "on their backs",
            "Your walk turns into a run as you try to find an escape from this never-ending biome.", #14 choice 2
            "You hide behind some rocks and watch as the spider constructs",
            "a series of portals using the information carried on their backs",
            "There is something beautiful about the simple nature of their",
            "dedication to their work.",
            "You are able to watch as they work with amazing efficiency,",
            "never once getting in eithers way.",
            "Once they construct all of them there is a brief moment of nothing",
            "before one glows as if it was selected",
            "It seems as if your world is going into that portal,",
            "what wouldve happened had you stopped the spiders.",
            "Did you bless the world or curse it?",]

    global x #uses global x to keep the list progressing when button is pressed
    x = x+1

    if x == 5: #use this part to create 2 buttons on the appropriate line change the number depending
        p2btn.pack_forget()
        p2choice1.pack() #shows 2 choice buttons
        p2choice2.pack()
    if x == 14:
        p2btn.pack_forget()
        p2choice3.pack()
        p2choice4.pack()
    if x == 26:
        p2btn.pack_forget()
        p3btn.pack()
        x=-1
    if x<27:
        print("x is ",x)#debug purposes tracks list
        res = line[x]
        lbl.configure(text= res)

def p2sidetrack(): #run from alternate button follows alternate path then goes back to main story
    global y
    print("y =",y) #debug purposes tracks list
    if y == 3: #change the y value to when the alternate story ends
        global x
        x = 5 #change the x value to where in the main story you want to call back to
        p2btn2.pack_forget()
        p2btn.pack()
        y=0
        return()
    line = ["You attempt to navigate away from the sound however you realise nothing exists beyond this point.",
            "You almost fall off the edge of whatever it is your standing on..",
            "You face no choice but to head towards the noise"] #keep all alternate text choices here
    res = line[y] # idk why we did this
    lbl.configure(text = res) # changes the text
    y = y+1 # increments y to contintue progress

def p2loop():
    global y
    print("y =",y) #debug purposes tracks list
    if y == 12: #change the y value to when the alternate story ends
        global x
        x = -1 #change the x value to where in the main story you want to call back to
        p2btn3.pack_forget()
        p2btn.pack()
        y=0
        return()
    line = ["You attempt to attack the spiders by grabbing something",
            "off one of their backs and swinging it as hard as you can",
            "However on impact the spider is completely unphased in fact",
            "not a single one acknowledges anything you did nor even you",
            "as a person",
            "Some bardge into you on their way but it seems they dont care",
            "at all what you do, they all focus on their larger cause",
            "They are all constructing something... something beautiful",
            "They are creating portals to other worlds but they all seem incomplete",
            "The last thing you wonder is if you caused this what did you",
            "take from them",
            "As you wonder the whole world stops.",
            "A command comes from above F5"] #keep all alternate text choices here
    res = line[y] # idk why we did this
    lbl.configure(text = res) # changes the text
    y = y+1 # increments y to contintue progress

p2btn = Button(window, text="Click Me", command=p2clicked,) #calls function when pressed
p2btn2 = Button(window, text="Click me", command=p2sidetrack) #creates the illusion of the same button but actually runs different function
p2btn3 = Button(window, text="Click me", command=p2loop)

def p2option1():
    global choice
    choice = 1
    p2btn.pack()
    p2choice1.pack_forget() #creates new button and hides choices
    p2choice2.pack_forget()
    
def p2option2():
    
    global choice
    choice = 2
    p2btn2.pack()
    p2choice1.pack_forget() #creates new button and hides choices
    p2choice2.pack_forget()
    global x
    x=6

def p2option3():
    p2btn.pack()
    p2choice3.pack_forget()
    p2choice4.pack_forget()

def p2option4():
    p2btn3.pack()
    p2choice3.pack_forget()
    p2choice4.pack_forget()


p2choice1 = Button(window, command=p2option1, text="Head towards the sound") #option buttons
p2choice2 = Button(window, command=p2option2, text="Navigate away from the sound")
p2choice3 = Button(window, command=p2option3, text="Run from the spiders")
p2choice4 = Button(window, command=p2option4, text="Fight the spiders")

    

#-----------------------------------------------------PART3-----------------------------------------------------
def clicked_p3():
    line = ["Loading...",
            "You awake in a darkened room with a single fluorescent light dangling from the ceiling from a bare wire.",
            "It shines right over you, stinging your eyes.",
            "You squint as you look into the distance. You cannot see any walls or the ceiling.",
            "Piles upon piles of pre-owned objects are spread out as far as you can see.",
            "A quiet roar of voices can be heard in the distance chanting numbers.",
            "You can't tell where they come from. Another sign stands tall in front of you, this one saying 'Sell your used items'.",
            "Investigate the numbers, or the site?",
            "You look up, to see giant floating numbers, seemingly assigned to each object.",
            "They vanish as fast as they appear: '50', '100', '120'. With each disappearance, the voices grow louder.",
            "Suddenly, the voices stop. The numbers stop appearing.",
            "A computer forces its way out of the mess and floats upwards. It keeps going until it cannot be seen.",
            "Once it's gone, vast numbers of objects clatter around you, most of which are technological.",
            "A TV, a fridge and a dishwasher land with a deafening crash.",
            "And with them, the voices grew louder.",
            "Price values grow larger and more frequent, more objects fall and crash from all directions as others soar upwards.",
            "Your head spins. The endless cacophony buries itself into your head and clutches you, refusing to let go.",
            "You don't want to be here anymore, you don't belong here in a place for the dead and unwanted.",
            "The already dark room grows black along with a feeling that you are no longer alone, as you slowly lose consciousness once more.",
            "...",
            "RESTARTING"]

    global x
    x = x+1
    if x == 7:
        p3btn.pack_forget()
        p3choice1.pack()
        p3choice2.pack()
    if x == 21:
        p3btn.pack_forget()
        p4btn.pack()
        x=-1
    if x<22:
        print("x is ",x)#debug purposes tracks list
        res = line[x]
        lbl.configure(text= res)

def sidetrack_p3():
    global y
    print("y =",y)
    if y == 6:
        global x
        x = 13
        p3btn2.pack_forget()
        p3btn.pack()
        y=0
        return()
    line = ["You look around the area. Objects have been placed seemingly without a care.",
            "Some of these objects are surrounded by voices and prices.",
            "More objects pop into existence, and they don't stop coming.",
            "Vast numbers of objects clatter around you, most of which are technological.",
            "A derelict car leaking oil sits next to a frayed and worn sofa.",
            "A TV, a fridge and a dishwasher land with a deafening crash next to you."]
    res = line[y]
    lbl.configure(text = res)
    y = y+1

p3btn = Button(window, text="Click Me", command=clicked_p3,)
p3btn2 = Button(window, text="Click me", command=sidetrack_p3)



def option1_p3():
    global choice
    choice = 1
    p3btn.pack()
    p3choice1.pack_forget()
    p3choice2.pack_forget()
    global x
    x=7
def option2_p3():
    
    global choice
    choice = 2
    p3btn2.pack()
    p3choice1.pack_forget()
    p3choice2.pack_forget()
    global x
    x=18
p3choice1 = Button(window, command=option1_p3, text="Investigate the numbers")
p3choice2 = Button(window, command=option2_p3, text="Investigate the site")




#-----------------------------------------------------PART4-----------------------------------------------------




def p4clicked():
    line = ["Loading...",
            "...",
            "New world has successfully loaded",
            "You wake up in a dark room, you decide to get up and look around",
            "You scan the room. You noticed that there is a list of instructions not too far from you. You decide to pick them up",
            "This list of instructions tell you what your next task is. Your creator wants you to mine bitcoin.",
            "But you have to search for a tool that you can use",
            "You go left, or go right",
            "You decide to turn left, you see a box and decide to open it.",
            "Its exactly what you've been looking for, the tool needed to mine the bitcoin! Now you head back the way you came",
            "Now that you have the tool that you need to mine the bitcoin, you get started.",
            "Whilst you're working you noticed that it has gotten easier for you to mine bitcoin instead of endlessly searching.",
            "Could you have been updated by your creator?",
            "It's been about 2 weeks since you've started working. No new updates and now you're starting to feel sluggish",
            "The lights are getting dim. Maybe you should rest and go into sleep mode"]
    global x
    x = x + 1

    if x == 7:
        p4btn.pack_forget()
        p4choice1.pack()
        p4choice2.pack()
    if x == 13:
        p4btn.pack_forget()
        p5btn.pack()
        x=-1
    if x <14:
        print("x is ",x)
        res = line[x]
        lbl.configure(text=res)

def p4sidetrack():
    global y
    print("y =", y)
    if y == 3:
        global x
        x = 10
        p4btn2.pack_forget()
        p4btn.pack()
        y=0
        return ()
    line = ["You decide to turn right, the path seems to go on forever. It looks as if its been blocked off.",
            "Out of frustration you head back the way you came",
            "This time you go down the left path and find what you are looking for. Eager to start, you head back"]
    res = line[y]
    lbl.configure(text=res)
    y = y + 1


p4btn = Button(window, text="Click Me", command=p4clicked)
p4btn2 = Button(window, text="Click me", command=p4sidetrack)


def p4option1():
    global choice
    choice = 1
    p4btn.pack()
    p4choice1.pack_forget()
    p4choice2.pack_forget()
    global x
    x = 8


def p4option2():
    global choice
    choice = 2
    p4btn2.pack()
    p4choice1.pack_forget()
    p4choice2.pack_forget()
    global x
    x = 18



p4choice1 = Button(window, command=p4option1, text="Turn Left")
p4choice2 = Button(window, command=p4option2, text="Turn Right")




#-----------------------------------------------------PART5-----------------------------------------------------




def clickedPart5():

    line = ["Loading..",
            "Loading....",
            "Loading.....",
            "Successfully loaded.",
            "You open your eyes onto a new World.\nIt says welcome to Facebook.com.\nYou look around only to find there's no room - it's absolutely crowded",
            "You see all sorts of stuff in this world.\nThere are a lot pictures with text on them - they call them memes or something of the sort.\nYou can hear people talking to each other from all over the world - it's really impressive.",
            "Wait what is happening? The world is slowing down, you can see empty boxes - they used to be images of people.",
            "What is going on?!",
            "I'm frozen!",
            "Some kind of message appears...",
            "Warning: the site is experiencing some technical difficulties.\nPlease hold on while our engineers work to fix the issue - :D",
            "You wait for a bit",
            "Warning: the site has officially shut down due to a DDOS attack.\nWe are sorry of the inconvenience.\nPlease accept our apologies and try later today or tomorrow"]

    global x
    x = x+1
    if x ==12:
        p5btn.pack_forget()
    if x<13:
        print("x is ",x)
        res = line[x]
        lbl.configure(text= res)


p5btn = Button(window, text="Click Me", command=clickedPart5,)

window.mainloop()
