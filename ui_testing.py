from tkinter import *

x = -1
choice = 0

window = Tk()

window.title("Python Story")

window.geometry('700x400')

lbl = Label(window, text="Welcome to the story click next to continue")

lbl.pack()



def clicked():

    line = ["You stay with the sign...",
            "You watch an entire forest grow before your very eyes.",
            "The trees grow tall and eventually the sign is entangled in the dense undergrowth of the forest floor.",
            "The lianas and creepers dominate the forest floor. The trees tower high above you as it were some sort of competition."]

    global x
    x = x+1

    if x == 3:
        choice1.pack()
        choice2.pack()
    
    res = line[x]

    lbl.configure(text= res)

btn = Button(window, text="Click Me", command=clicked,)

def option1():
    global choice
    choice = 1

def option2():
    global choice
    choice = 2

btn.pack()
choice1 = Button(window, command=option1, text="Option 1")
choice2 = Button(window, command=option2, text="Option 2")


    

window.mainloop()
