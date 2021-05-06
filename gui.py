import tkinter
from PIL import Image, ImageTk
from tkinter import Toplevel

master=tkinter.Tk()

opWindow = Toplevel(master)
opWindow.title("Make a pick!")
opWindow.geometry("250x250")

Checkbutton1 = tkinter.IntVar()  
Checkbutton2 = tkinter.IntVar()  
Checkbutton3 = tkinter.IntVar() 
Checkbutton11 = tkinter.IntVar()  
Checkbutton12 = tkinter.IntVar()  

opList = []

def checker():
	if Checkbutton1.get() == 1:
		if "Cavity" not in opList:
			opList.append("Cavity")
	else:
		if "Cavity" in opList:
			opList.remove("Cavity")

	if Checkbutton2.get() == 1:
		if "Wisdom" not in opList:
			opList.append("Wisdom")
	else:
		if "Wisdom" in opList:
			opList.remove("Wisdom")

	if Checkbutton3.get() == 1:
		if "Molar" not in opList:
			opList.append("Molar")
	else:
		if "Molar" in opList:
			opList.remove("Molar")

	if Checkbutton11.get() == 1:
		if "Etc" not in opList:
			opList.append("Etc")
	else:
		if "Etc" in opList:
			opList.remove("Etc")

	if Checkbutton12.get() == 1:
		if "Etc.." not in opList:
			opList.append("Etc...")
	else:
		if "Etc.." in opList:
			opList.remove("Etc...")

def goToImages():
	opWindow.destroy()
	imWindow.deiconify()

	## Test the list ##
	for x in range(len(opList)):
		print(opList[x])

Button1 = tkinter.Checkbutton(opWindow, text = "Cavity", 
                      variable = Checkbutton1,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10,
                      command=checker)

Button2 = tkinter.Checkbutton(opWindow, text = "Wisdom",
                      variable = Checkbutton2,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10,
                      command=checker)
	  
Button3 = tkinter.Checkbutton(opWindow, text = "Molar",
                      variable = Checkbutton3,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10,
                      command=checker)  

Button11 = tkinter.Checkbutton(opWindow, text = "Etc", 
                      variable = Checkbutton11,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10,
                      command=checker)

Button12 = tkinter.Checkbutton(opWindow, text = "Etc...", 
                      variable = Checkbutton12,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10,
                      command=checker)

Button4=tkinter.Button(opWindow, text="Submit", command = goToImages, bg = 'gainsboro') 
    
Button1.pack()  
Button2.pack()  
Button3.pack()
Button11.pack()  
Button12.pack()
Button4.pack()	


imWindow = Toplevel(master)
imWindow.title("Images")
imWindow.geometry("850x650")
imWindow.configure(background = 'black')
l = tkinter.Label(imWindow, text = "Welcome!\n Here you can sift thru images as you please!",
		              fg = 'aquamarine2', bg = 'black', bd = 0)
l.config(font=("Courier", 18, "bold"))
l.pack(padx = 1, pady = 1)

master.withdraw()
imWindow.withdraw()

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

	button1=tkinter.Button(imWindow, text="<-- Previous", command = showImagePrev, bg = 'gainsboro') ## BUTTON 1 PREVIOUS ##
	button1.place(x=15, y=15)

	button2=tkinter.Button(imWindow, text="Next -->", command = showImageNext, bg = 'gainsboro') ## BUTTON 2 NEXT ##
	button2.place(x=780, y=15)

	button3=tkinter.Button(imWindow, text="QUIT", command = imWindow.destroy, fg = 'red', bg = 'gainsboro') ## BUTTON 3 QUIT ##
	button3.place(x=375, y=570)
	button3.config(font=("Helvetica", 22, "bold"))  # bigger sized font used #

	button4=tkinter.Button(imWindow, text="Skip To Last", command = showImageLast, bg = 'gainsboro') ## BUTTON 4 LAST ##
	button4.place(x=8, y=615)

	button5=tkinter.Button(imWindow, text="Return to First", command = showImageFirst, bg = 'gainsboro') ## BUTTON 5 FIRST ##
	button5.place(x=8, y=580)

	button6=tkinter.Button(imWindow, text="Go to Parent", command = goToParent, bg = 'gainsboro') ## BUTTON 6 PARENT ##
	button6.place(x=765,y=615)


def showImageNext():
	global imageNum ##### global variable

	### check in bounds ###
	if 0 <= imageNum+1 < len(imageList):
		imageNum = imageNum+1
		myImage = Image.open(imageList[imageNum]) ## open the images ##
		myImage = myImage.resize((650,450), Image.ANTIALIAS)
		test = ImageTk.PhotoImage(myImage)
		label1 = tkinter.Label(imWindow, image=test, bd = 0)
		label1.image = test
		label1.place(x=100, y=100)

def showImagePrev():
	global imageNum ##### global variable

	### check in bounds ###
	if 0 <= imageNum-1 < len(imageList):
		imageNum = imageNum-1
		myImage = Image.open(imageList[imageNum]) ## open the images ##
		myImage = myImage.resize((650,450), Image.ANTIALIAS)
		test = ImageTk.PhotoImage(myImage)
		label1 = tkinter.Label(imWindow, image=test, bd = 0)
		label1.image = test
		label1.place(x=100, y=100)

def showImageFirst():
	global imageNum ##### global variable

	imageNum = 0
	myImage = Image.open(imageList[imageNum]) ## open the images ##
	myImage = myImage.resize((650,450), Image.ANTIALIAS)
	test = ImageTk.PhotoImage(myImage)
	label1 = tkinter.Label(imWindow, image=test, bd = 0)
	label1.image = test
	label1.place(x=100, y=100)


def showImageLast():
	global imageNum ##### global variable

	imageNum = len(imageList)-1
	myImage = Image.open(imageList[imageNum]) ## open the images ##
	myImage = myImage.resize((650,450), Image.ANTIALIAS)
	test = ImageTk.PhotoImage(myImage)
	label1 = tkinter.Label(imWindow, image=test, bd = 0)
	label1.image = test
	label1.place(x=100, y=100)


def goToParent():
	## still need to write function based on our node tree ##
 	print("still needs to be worked on")

def main():
	addWidgets()
	master.mainloop()


if __name__ == '__main__':
    main()
