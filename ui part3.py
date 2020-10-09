from tkinter import *

x = -1
y = 0
choice = 0

window = Tk()

window.title("Python Story")

window.geometry('700x400')

lbl = Label(window, text="Welcome to our story.")

lbl.pack()

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
        btn.pack_forget()
        choice1.pack()
        choice2.pack()

    print("x is ",x)
    res = line[x]

    lbl.configure(text= res)

def sidetrack_p3():
    global y
    print("y =",y)
    if y == 6:
        global x
        x = 13
        btn2.pack_forget()
        btn.pack()
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

btn = Button(window, text="Click Me", command=clicked_p3,)
btn2 = Button(window, text="Click me", command=sidetrack_p3)



def option1_p3():
    global choice
    choice = 1
    btn.pack()
    choice1.pack_forget()
    choice2.pack_forget()
    global x
    x=7
def option2_p3():
    
    global choice
    choice = 2
    btn2.pack()
    choice1.pack_forget()
    choice2.pack_forget()
    global x
    x=18
btn.pack()
choice1 = Button(window, command=option1_p3, text="Option 1")
choice2 = Button(window, command=option2_p3, text="Option 2")

window.mainloop()
