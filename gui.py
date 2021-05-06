import tkinter
from PIL import Image, ImageTk
from tkinter import Toplevel

master=tkinter.Tk()

opWindow = Toplevel(master)
opWindow.title("Make a pick!")
opWindow.geometry("200x500")

## FLAGS TO INSERT AS OPTIONS: 1-32, cavity, crowns, restorations, enamel ##

Checkbutton1 = tkinter.IntVar()  
Checkbutton2 = tkinter.IntVar()  
Checkbutton3 = tkinter.IntVar() 
Checkbutton4 = tkinter.IntVar()  
Checkbutton5 = tkinter.IntVar()  
Checkbutton6 = tkinter.IntVar()  
Checkbutton7 = tkinter.IntVar()  
Checkbutton8 = tkinter.IntVar() 
Checkbutton9 = tkinter.IntVar()  
Checkbutton10 = tkinter.IntVar()  
Checkbutton11 = tkinter.IntVar()  
Checkbutton12 = tkinter.IntVar()  
Checkbutton13 = tkinter.IntVar() 
Checkbutton14 = tkinter.IntVar()  
Checkbutton15 = tkinter.IntVar()  
Checkbutton16 = tkinter.IntVar()  
Checkbutton17 = tkinter.IntVar()  
Checkbutton18 = tkinter.IntVar() 
Checkbutton19 = tkinter.IntVar()  
Checkbutton20 = tkinter.IntVar()  
Checkbutton21 = tkinter.IntVar()  
Checkbutton22 = tkinter.IntVar()  
Checkbutton23 = tkinter.IntVar() 
Checkbutton24 = tkinter.IntVar()  
Checkbutton25 = tkinter.IntVar()  
Checkbutton26 = tkinter.IntVar()  
Checkbutton27 = tkinter.IntVar()  
Checkbutton28 = tkinter.IntVar() 
Checkbutton29 = tkinter.IntVar()  
Checkbutton30 = tkinter.IntVar()  
Checkbutton31 = tkinter.IntVar()  
Checkbutton32 = tkinter.IntVar()  
CheckbuttonCavity = tkinter.IntVar()  
CheckbuttonCrown = tkinter.IntVar()  
CheckbuttonRestoration = tkinter.IntVar()  
CheckbuttonEnamel = tkinter.IntVar()  


opList = []

def checker():
	if Checkbutton1.get() == 1:
		if "1" not in opList:
			opList.append("1")
	else:
		if "1" in opList:
			opList.remove("1")

	if Checkbutton2.get() == 1:
		if "2" not in opList:
			opList.append("2")
	else:
		if "2" in opList:
			opList.remove("2")

	if Checkbutton3.get() == 1:
		if "3" not in opList:
			opList.append("3")
	else:
		if "3" in opList:
			opList.remove("3")

	if Checkbutton4.get() == 1:
		if "4" not in opList:
			opList.append("4")
	else:
		if "4" in opList:
			opList.remove("4")

	if Checkbutton5.get() == 1:
		if "5" not in opList:
			opList.append("5")
	else:
		if "5" in opList:
			opList.remove("5")
	if Checkbutton6.get() == 1:
		if "6" not in opList:
			opList.append("6")
	else:
		if "6" in opList:
			opList.remove("6")

	if Checkbutton7.get() == 1:
		if "7" not in opList:
			opList.append("7")
	else:
		if "7" in opList:
			opList.remove("7")

	if Checkbutton8.get() == 1:
		if "8" not in opList:
			opList.append("8")
	else:
		if "8" in opList:
			opList.remove("8")

	if Checkbutton9.get() == 1:
		if "9" not in opList:
			opList.append("9")
	else:
		if "9" in opList:
			opList.remove("9")

	if Checkbutton10.get() == 1:
		if "10" not in opList:
			opList.append("10")
	else:
		if "10" in opList:
			opList.remove("10")		

	if Checkbutton11.get() == 1:
		if "11" not in opList:
			opList.append("11")
	else:
		if "11" in opList:
			opList.remove("11")

	if Checkbutton12.get() == 1:
		if "12" not in opList:
			opList.append("12")
	else:
		if "12" in opList:
			opList.remove("12")

	if Checkbutton13.get() == 1:
		if "13" not in opList:
			opList.append("13")
	else:
		if "13" in opList:
			opList.remove("13")

	if Checkbutton14.get() == 1:
		if "14" not in opList:
			opList.append("14")
	else:
		if "14" in opList:
			opList.remove("14")

	if Checkbutton15.get() == 1:
		if "15" not in opList:
			opList.append("15")
	else:
		if "15" in opList:
			opList.remove("15")

	if Checkbutton16.get() == 1:
		if "16" not in opList:
			opList.append("16")
	else:
		if "16" in opList:
			opList.remove("16")

	if Checkbutton17.get() == 1:
		if "17" not in opList:
			opList.append("17")
	else:
		if "17" in opList:
			opList.remove("17")

	if Checkbutton18.get() == 1:
		if "18" not in opList:
			opList.append("18")
	else:
		if "18" in opList:
			opList.remove("18")

	if Checkbutton19.get() == 1:
		if "19" not in opList:
			opList.append("19")
	else:
		if "19" in opList:
			opList.remove("19")

	if Checkbutton20.get() == 1:
		if "20" not in opList:
			opList.append("20")
	else:
		if "20" in opList:
			opList.remove("20")

	if Checkbutton21.get() == 1:
		if "21" not in opList:
			opList.append("21")
	else:
		if "21" in opList:
			opList.remove("21")

	if Checkbutton22.get() == 1:
		if "22" not in opList:
			opList.append("22")
	else:
		if "22" in opList:
			opList.remove("22")

	if Checkbutton23.get() == 1:
		if "23" not in opList:
			opList.append("23")
	else:
		if "23" in opList:
			opList.remove("23")

	if Checkbutton24.get() == 1:
		if "24" not in opList:
			opList.append("24")
	else:
		if "24" in opList:
			opList.remove("24")

	if Checkbutton23.get() == 1:
		if "23" not in opList:
			opList.append("23")
	else:
		if "23" in opList:
			opList.remove("23")

	if Checkbutton24.get() == 1:
		if "24" not in opList:
			opList.append("24")
	else:
		if "24" in opList:
			opList.remove("24")

	if Checkbutton25.get() == 1:
		if "25" not in opList:
			opList.append("25")
	else:
		if "25" in opList:
			opList.remove("25")

	if Checkbutton26.get() == 1:
		if "26" not in opList:
			opList.append("26")
	else:
		if "26" in opList:
			opList.remove("26")

	if Checkbutton27.get() == 1:
		if "27" not in opList:
			opList.append("27")
	else:
		if "27" in opList:
			opList.remove("27")

	if Checkbutton28.get() == 1:
		if "28" not in opList:
			opList.append("28")
	else:
		if "28" in opList:
			opList.remove("28")

	if Checkbutton29.get() == 1:
		if "29" not in opList:
			opList.append("29")
	else:
		if "29" in opList:
			opList.remove("29")

	if Checkbutton30.get() == 1:
		if "30" not in opList:
			opList.append("30")
	else:
		if "30" in opList:
			opList.remove("30")

	if Checkbutton31.get() == 1:
		if "31" not in opList:
			opList.append("31")
	else:
		if "31" in opList:
			opList.remove("31")

	if Checkbutton32.get() == 1:
		if "32" not in opList:
			opList.append("32")
	else:
		if "32" in opList:
			opList.remove("32")

	if CheckbuttonCavity.get() == 1:
		if "cavity" not in opList:
			opList.append("cavity")
	else:
		if "cavity" in opList:
			opList.remove("cavity")

	if CheckbuttonCrown.get() == 1:
		if "crown" not in opList:
			opList.append("crown")
	else:
		if "crown" in opList:
			opList.remove("crown")

	if CheckbuttonRestoration.get() == 1:
		if "restoration" not in opList:
			opList.append("restoration")
	else:
		if "restoration" in opList:
			opList.remove("restoration")

	if CheckbuttonEnamel.get() == 1:
		if "enamel" not in opList:
			opList.append("enamel")
	else:
		if "enamel" in opList:
			opList.remove("enamel")

def goToImages():
	opWindow.destroy()
	imWindow.deiconify()

	## Test the list ##
	for x in range(len(opList)):
		print(opList[x])

Button1 = tkinter.Checkbutton(opWindow, text = "1", variable = Checkbutton1, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker)

Button2 = tkinter.Checkbutton(opWindow, text = "2", variable = Checkbutton2, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker)
	  
Button3 = tkinter.Checkbutton(opWindow, text = "3", variable = Checkbutton3, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker) 

Button4 = tkinter.Checkbutton(opWindow, text = "4", variable = Checkbutton4, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker)

Button5 = tkinter.Checkbutton(opWindow, text = "5", variable = Checkbutton5, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker)

Button6 = tkinter.Checkbutton(opWindow, text = "6", variable = Checkbutton6, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker)

Button7 = tkinter.Checkbutton(opWindow, text = "7", variable = Checkbutton7, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker)
	  
Button8 = tkinter.Checkbutton(opWindow, text = "8", variable = Checkbutton8, onvalue = 1,
                    		  offvalue = 0, height = 1, width = 10, command=checker) 

Button9 = tkinter.Checkbutton(opWindow, text = "9", variable = Checkbutton9, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker)

Button10 = tkinter.Checkbutton(opWindow, text = "10", variable = Checkbutton10, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker)

Button11 = tkinter.Checkbutton(opWindow, text = "11", variable = Checkbutton11, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker)

Button12 = tkinter.Checkbutton(opWindow, text = "12", variable = Checkbutton12, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker)
	  
Button13 = tkinter.Checkbutton(opWindow, text = "13", variable = Checkbutton13, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker) 

Button14 = tkinter.Checkbutton(opWindow, text = "14", variable = Checkbutton14, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker)

Button15 = tkinter.Checkbutton(opWindow, text = "15", variable = Checkbutton15, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker)

Button16 = tkinter.Checkbutton(opWindow, text = "16", variable = Checkbutton16, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker)

Button17 = tkinter.Checkbutton(opWindow, text = "17", variable = Checkbutton17, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker)
	  
Button18 = tkinter.Checkbutton(opWindow, text = "18", variable = Checkbutton18, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker) 

Button19 = tkinter.Checkbutton(opWindow, text = "19", variable = Checkbutton19, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker)

Button20= tkinter.Checkbutton(opWindow, text = "20", variable = Checkbutton20, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker)

Button21 = tkinter.Checkbutton(opWindow, text = "21", variable = Checkbutton21, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker)

Button22 = tkinter.Checkbutton(opWindow, text = "22", variable = Checkbutton22, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker)
	  
Button23 = tkinter.Checkbutton(opWindow, text = "23", variable = Checkbutton23, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker) 

Button24 = tkinter.Checkbutton(opWindow, text = "24", variable = Checkbutton24, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker)

Button25 = tkinter.Checkbutton(opWindow, text = "25", variable = Checkbutton25, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker)

Button26 = tkinter.Checkbutton(opWindow, text = "26", variable = Checkbutton26, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker)

Button27 = tkinter.Checkbutton(opWindow, text = "27", variable = Checkbutton27, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker)
	  
Button28 = tkinter.Checkbutton(opWindow, text = "28", variable = Checkbutton28, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker) 

Button29 = tkinter.Checkbutton(opWindow, text = "29", variable = Checkbutton29, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker)

Button30 = tkinter.Checkbutton(opWindow, text = "30", variable = Checkbutton30, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker)

Button31 = tkinter.Checkbutton(opWindow, text = "31", variable = Checkbutton31, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker)

Button32 = tkinter.Checkbutton(opWindow, text = "32", variable = Checkbutton32, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker)
	  
ButtonCavity = tkinter.Checkbutton(opWindow, text = "Cavity", variable = CheckbuttonCavity, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker) 

ButtonCrown = tkinter.Checkbutton(opWindow, text = "Crown", variable = CheckbuttonCrown, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker)

ButtonRestoration = tkinter.Checkbutton(opWindow, text = "Restoration", variable = CheckbuttonRestoration, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker)

ButtonEnamel = tkinter.Checkbutton(opWindow, text = "Enamel", variable = CheckbuttonEnamel, onvalue = 1,
                      		  offvalue = 0, height = 1, width = 10, command=checker)

ButtonSubmit=tkinter.Button(opWindow, text="SUBMIT", command = goToImages, bg = 'gainsboro') 
    
Button1.grid(row=1, column=1)
Button2.grid(row=1, column=2)  
Button3.grid(row=2, column=1)
Button4.grid(row=2, column=2)  
Button5.grid(row=3, column=1)  
Button6.grid(row=3, column=2)
Button7.grid(row=4, column=1)
Button8.grid(row=4, column=2)
Button9.grid(row=5, column=1)
Button10.grid(row=5, column=2) 
Button11.grid(row=6, column=1)
Button12.grid(row=6, column=2)
Button13.grid(row=7, column=1)
Button14.grid(row=7, column=2)  
Button15.grid(row=8, column=1)
Button16.grid(row=8, column=2)
Button17.grid(row=9, column=1)
Button18.grid(row=9, column=2)
Button19.grid(row=10, column=1)  
Button20.grid(row=10, column=2)
Button21.grid(row=11, column=1)
Button22.grid(row=11, column=2) 
Button23.grid(row=12, column=1) 
Button24.grid(row=12, column=2)
Button25.grid(row=13, column=1)
Button26.grid(row=13, column=2)
Button27.grid(row=14, column=1)
Button28.grid(row=14, column=2)  
Button29.grid(row=15, column=1)
Button30.grid(row=15, column=2)
Button31.grid(row=16, column=1)
Button32.grid(row=16, column=2)
ButtoneCavity.grid(row=17, column=1)
ButtonCrown.grid(row=17, column=2)
ButtonRestoration.grid(row=18, column=1)
ButtonEnamel.grid(row=18, column=2)
ButtonSubmit.grid(row=19, column=1, sticky="")


imWindow = Toplevel(master)
imWindow.title("Images")
imWindow.geometry("850x650")
imWindow.configure(background = 'black')
l = tkinter.Label(imWindow, text = "Welcome!\n Here you can sift thru images as you please!",
		              fg = 'aquamarine2', bg = 'black', bd = 0)
l.config(font=("Courier", 18, "bold"))
l.place(x=425,y=50,anchor="center")

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
