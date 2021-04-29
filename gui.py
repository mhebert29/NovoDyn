import tkinter
import tkinter.font as font
from PIL import Image, ImageTk

NAME = "Maddie"

master=tkinter.Tk()
master.title("Preternship Trial GUI")
master.geometry("850x650")
master.configure(background = 'black')

## list of images --- data received from Mr. McMillan (NovoDynamics) ##
imageList = ["composite-1.png", "composite-2.jpg", "composite-3.jpg", "composite-4.jpg", "composite-5.jpg", "composite-6.jpg", 
		     "composite-7.jpg", "composite-8.png", "composite-9.png", "composite-10.jpg", "composite-11.jpg", "composite-12.jpg",
		     "composite-13.jpg", "composite-14.jpg", "composite-15.jpg", "composite-16.jpg", "composite-17.jpg", "composite-18.jpg",
			 "composite-19.jpg", "composite-20.jpg", "composite-21.jpg", "composite-22.jpg", "composite-23.jpg", "composite-24.jpg",
			 "composite-25.jpg", "composite-26.jpg", "composite-27.png", "composite-28.PNG", "composite-29.jpg", "composite-30.jpg",
			 "composite-31.jpg", "composite-32.jpg", "composite-33.jpg", "composite-34.jpg", "composite-35.jpg", "composite-36.jpg",
			 "composite-37.jpg", "composite-38.jpg", "composite-39.jpg", "composite-40.jpg", "composite-41.png", "composite-42.jpg",
			 "composite-43.png", "composite-44.jpg", "composite-45.jpg"]
imageNum = -1

def addWidgets():
	myFont = font.Font(size=30)

	button1=tkinter.Button(master, text="<-- Previous", command = showImagePrev, bg = 'white') ## BUTTON 1 PREVIOUS ##
	button1.place(x=15, y=15)

	button2=tkinter.Button(master, text="Next -->", command = showImageNext, bg = 'white') ## BUTTON 2 NEXT ##
	button2.place(x=780, y=15)

	button3=tkinter.Button(master, text="QUIT", command = master.destroy, fg = 'red', bg = 'white') ## BUTTON 3 QUIT ##
	button3.place(x=375, y=570)
	button3['font'] = myFont   # bigger sized font used #

def showImageNext():
	global imageNum ##### global variable

	### check in bounds ###
	if 0 <= imageNum+1 < len(imageList):
		imageNum = imageNum+1
		myImage = Image.open(imageList[imageNum]) ## open the images ##
		myImage = myImage.resize((650,450), Image.ANTIALIAS)
		test = ImageTk.PhotoImage(myImage)
		label1 = tkinter.Label(master, image=test, bd = 0)
		label1.image = test
		label1.place(x=100, y=90)

def showImagePrev():
	global imageNum ##### global variable

	### check in bounds ###
	if 0 <= imageNum-1 < len(imageList):
		imageNum = imageNum-1
		myImage = Image.open(imageList[imageNum]) ## open the images ##
		myImage = myImage.resize((650,450), Image.ANTIALIAS)
		test = ImageTk.PhotoImage(myImage)
		label1 = tkinter.Label(master, image=test, bd = 0)
		label1.image = test
		label1.place(x=100, y=90)

def welcome():
	text1 = tkinter.Text(master, height = 5, width = 40)
	l = tkinter.Label(master, text = "Welcome {}!\n Here you can sift thru images as you please!".format(NAME),
		              fg = 'yellow', bg = 'black')
	l.config(font=("Courier", 18))
	l.place(x = 110, y = 10)


def main():
	welcome()
	addWidgets()
	master.mainloop()


if __name__ == '__main__':
    main()
