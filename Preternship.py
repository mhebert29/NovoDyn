#!/usr/bin/env python3
import tkinter
from PIL import Image, ImageTk

NAME = "Maddie"

master=tkinter.Tk()
master.title("Preternship Trial GUI")
master.geometry("850x650")


def addWidgets():
	button1=tkinter.Button(master, text="<-- Previous")
	button1.place(x=15, y=15)

	button2=tkinter.Button(master, text="Next -->", command=showImageNext)
	button2.place(x=780, y=15)

	button3=tkinter.Button(master, text="QUIT", command = master.destroy, fg = 'red')
	button3.place(x=415, y=600)

def showImageNext():
	myImage = Image.open("parrot.jpg")
	test = ImageTk.PhotoImage(myImage)
	label1 = tkinter.Label(image=test)
	label1.image = test
	label1.place(x=110, y=10)


def welcome():
	text1 = tkinter.Text(master, height = 5, width = 40)
	l = tkinter.Label(master, text = "Welcome {}!\n Here you can sift thru images as you please!".format(NAME), fg = 'blue')
	l.config(font=("Courier", 18))
	l.place(x = 110, y = 10)

welcome()
addWidgets()
master.mainloop()