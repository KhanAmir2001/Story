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

def clicked():# runs when button is clicked

    line = ["Loading...", #contains all text of main routes note doesnt keep alternate choices
            "SUCCESSFULLY LOADED.",
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
        choice1.pack() #shows 2 choice buttons
        choice2.pack()

    print("x is ",x) #debug purposes tracks list
    res = line[x]

    lbl.configure(text= res)

def sidetrack(): #run from alternate button follows alternate path then goes back to main story
    global y
    print("y =",y) #debug purposes tracks list
    if y == 2: #change the y value to when the alternate story ends
        global x
        x = 18 #change the x value to where in the main story you want to call back to
        btn2.pack_forget()
        btn.pack()
        return()
    line = ["You leave the sign behind to explore this new world growing before you.",
            "Trees, forests, beaches, rivers. You gaze in amazement as a whole ecosystem renders in around you."] #keep all alternate text choices here
    res = line[y] # idk why we did this
    lbl.configure(text = res) # changes the text
    y = y+1 # increments y to contintue progress

btn = Button(window, text="Click Me", command=clicked,) #calls function when pressed
btn2 = Button(window, text="Click me", command=sidetrack) #creates the illusion of the same button but actually runs different function

def option1():
    global choice
    choice = 1
    btn.pack()
    choice1.pack_forget() #creates new button and hides choices
    choice2.pack_forget()
    global x
    x=7
    
def option2():
    
    global choice
    choice = 2
    btn2.pack()
    choice1.pack_forget() #creates new button and hides choices
    choice2.pack_forget()
    global x
    x=18
btn.pack()
choice1 = Button(window, command=option1, text="Option 1") #option buttons
choice2 = Button(window, command=option2, text="Option 2")


    

window.mainloop()
