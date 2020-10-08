from tkinter import *

x = -1

window = Tk()

window.title("Python Story")

window.geometry('700x400')

lbl = Label(window, text="Hello")

lbl.pack()



def clicked():

    line = ["You stay with the sign...",
            "You watch an entire forest grow before your very eyes.",
            "The trees grow tall and eventually the sign is entangled in the dense undergrowth of the forest floor.",
            "The lianas and creepers dominate the forest floor. The trees tower high above you as it were some sort of competition."]

    global x
    x = x+1
    
    res = line[x]

    lbl.configure(text= res)

btn = Button(window, text="Click Me", command=clicked,)

btn.pack()

window.mainloop()
