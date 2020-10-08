from tkinter import *

x = -1
y = -1
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
            ]

    global x
    x = x+1

    if x == 6:
        btn.pack_forget()
        choice1.pack()
        choice2.pack()


    res = line[x]

    lbl.configure(text= res)

def sidetrack():
    global y
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
