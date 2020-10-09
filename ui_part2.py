from tkinter import *
# name all variables and functions with px depeding on your part
x = -1 #list pointer 
y = 0 #side story pointer
choice = 0 #keeps track of what option the user selects

window = Tk()

window.title("Python Story")

window.geometry('700x400') #declares window size ignore

lbl = Label(window, text="Welcome to our story.")

lbl.pack()

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

    print("x is ",x) #debug purposes tracks list
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

p2btn.pack()
p2choice1 = Button(window, command=p2option1, text="Head towards the sound") #option buttons
p2choice2 = Button(window, command=p2option2, text="Navigate away from the sound")
p2choice3 = Button(window, command=p2option3, text="Run from the spiders")
p2choice4 = Button(window, command=p2option4, text="Fight the spiders")


    

window.mainloop()
