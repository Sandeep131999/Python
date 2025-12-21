import tkinter
from tkinter import Button

##Remeber **Kwarg usage
window =tkinter.Tk()
window.title("My first gui program ")
window.minsize(500,500)

#Label
my_label = tkinter.Label(text = "Iam a label",font=("Arial",24,"bold"))
my_label.pack(side="left")


def button_click ():
    print("I got clicked ")
    my_label.config(text="Button Got Clicked")

#Button
button = tkinter.Button(text = "Click me",command=button_click)
button.pack()


#Entry
in_put= tkinter.Entry(width=30)
in_put.pack()


#Make a visible in the screen
window.mainloop()


#Tkinter was no use in the terms of ai developer


