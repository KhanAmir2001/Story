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
            "...",
            "New world has successfully loaded",
            "You wake up in a dark room, you decide to get up and look around",
            "You scan the room. You noticed that there is a list of instructions not too far from you. You decide to pick them up",
            "This list of instructions tell you what your next task is. Your creator wants you to mine bitcoin. But you have to search for a tool that you can use",
            "You go left, or go right",
            "You decide to turn left, you see a box and decide to open it.",
            "Its exactly what you've been looking for, the tool needed to mine the bitcoin! Now you head back the way you came",
            "Now that you have the tool that you need to mine the bitcoin, you get started.",
            "Whilst you're working you noticed that it has gotten easier for you to mine bitcoin instead of endlessly searching. Could you have been updated by your creator?",
            "It's been about 2 weeks since you've started working. No new updates and now you're starting to feel sluggish",
            "The lights are getting dim. Maybe you should rest and go into sleep mode"]
    global x
    x = x + 1

    if x == 6:
        btn.pack_forget()
        choice1.pack()
        choice2.pack()

    print("x is ", x)
    res = line[x]

    lbl.configure(text=res)


def sidetrack():
    global y
    print("y =", y)
    if y == 2:
        global x
        x = 9
        btn2.pack_forget()
        btn.pack()
        return ()
    line = ["You decide to turn right, the path seems to go on forever. It looks as if its been blocked off.",
            "Out of frustration you head back the way you came",
            "This time you go down the left path and find what you are looking for. Eager to start, you head back"]
    res = line[y]
    lbl.configure(text=res)
    y = y + 1


btn = Button(window, text="Click Me", command=clicked, )
btn2 = Button(window, text="Click me", command=sidetrack)


def option1():
    global choice
    choice = 1
    btn.pack()
    choice1.pack_forget()
    choice2.pack_forget()
    global x
    x = 6


def option2():
    global choice
    choice = 2
    btn2.pack()
    choice1.pack_forget()
    choice2.pack_forget()
    global x
    x = 18


btn.pack()
choice1 = Button(window, command=option1, text="Option 1")
choice2 = Button(window, command=option2, text="Option 2")

window.mainloop()
