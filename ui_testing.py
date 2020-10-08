from tkinter import *

x = -1
choice = 0

window = Tk()

window.title("Python Story")

window.geometry('700x400')

lbl = Label(window, text="Welcome to the story click next to continue")

lbl.pack()



def clicked():

    line = ["Loading...",
            "SUCCESSFULLY LOADED.",
            "You see a sign that says `Welcome to Utopia` and walk towards it...",
            "As you stare at the lonely sign, you notice a world start to evolve.",
            "You watch in awe.",
            "You watch the world slowly start to load in...",
            "Stay with the sign, or explore?"]

    global x
    x = x+1

    if x == 6:
        btn.pack_forget()
        choice1.pack()
        choice2.pack()
    
    res = line[x]

    lbl.configure(text= res)

btn = Button(window, text="Click Me", command=clicked,)

def option1():
    global choice
    choice = 1
    btn.pack()
    choice1.pack_forget()
    choice2.pack_forget()

def option2():
    global choice
    choice = 2

btn.pack()
choice1 = Button(window, command=option1, text="Option 1")
choice2 = Button(window, command=option2, text="Option 2")


    

window.mainloop()
