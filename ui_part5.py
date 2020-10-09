from tkinter import *

x = -1
y = 0
choice = 0

window = Tk()

window.title("Python Story")

window.geometry('700x400')

lbl = Label(window, text="Welcome to our story.")

lbl.pack()

def clickedPart5():

    line = ["Loading..",
            "Loading....",
            "Loading.....",
            "Successfully loaded.",
            "You open your eyes onto a new World.\nIt says welcome to Fackbook.com.\nYou look around only to find there's no room - it's absolutely crowded",
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



    print("x is ",x)
    res = line[x]

    lbl.configure(text= res)


btn = Button(window, text="Click Me", command=clickedPart5,)


btn.pack()



    

window.mainloop()



