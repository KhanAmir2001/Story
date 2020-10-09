from tkinter import *

x = -1
y = 0
choice = 0

window = Tk()

window.title("Python Story")

window.geometry('700x400')

lbl = Label(window, text="Welcome to our story.")

lbl.pack()

def clicked():

    line = ["Loading...",
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

    global x
    x = x+1

    if x == 6:
        btn.pack_forget()
        choice1.pack()
        choice2.pack()

    print("x is ",x)
    res = line[x]

    lbl.configure(text= res)

def sidetrack():
    global y
    print("y =",y)
    if y == 2:
        global x
        x = 18
        btn2.pack_forget()
        btn.pack()
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
choice1 = Button(window, command=option1, text="Option 1")
choice2 = Button(window, command=option2, text="Option 2")


    

window.mainloop()
