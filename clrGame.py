#Loading
def Loading(pro, info):
    print('Process: ',pro, ' | info: ', info)

#Import
import tkinter as tk
import random
Loading('1%', 'Import')


root = tk.Tk()
Loading('2%', 'Root')

#window settings
root.geometry("400x400")
root.title('Color Game | By Mikkoᶻ')
root.minsize(width = 200, height = 200)
Loading('3%', 'Window')

#Global values
lenght = 2
anws = ''
num = ''
Loading('5%', 'Values')

#Buttons. Reason is button commands cant handle same method?
def g():
    ultimate('g')
def r():
    ultimate('r')
def y():
    ultimate('y')
def b():
    ultimate('b')
Loading('8%', 'Buttons')

#Randomizer
def randomize():
    global num
    global lenght
    for x in range(lenght):
            code = random.random()
            if code < 0.25 and code > 0:
                num = num + "G"
            if code < 0.5 and code > 0.25:
                num = num + "R"
            if code < 0.75 and code > 0.5 :
                num = num + "Y"
            if code > 0.75:
                num = num + "B"
    txtLabel.configure(text=num)
Loading('15%', 'Randomizer')

#Hearth
def ultimate(clrCode):
    global num
    global anws
    global lenght
    txtLabel.configure(text='')
    if clrCode == 'r':
        anws+='R'
    if clrCode == 'g':
        anws+='G'
    if clrCode == 'b':
        anws+='B'
    if clrCode == 'y':
            anws+='Y'
    if anws == num:
        num = ''
        anws = ''
        lenght+=1
        randomize()
    if len(anws) == len(num):
        anws = ''
        txtLabel.configure(text=num)
Loading('50%', 'Hearth')
        
#Help Popup
def helpMe():
    popup = tk.Tk()
    popup.wm_title("Help")
    label = tk.Label(popup, text="Instructions")
    label.pack(side="top", fill="x", pady=10)
    label2 = tk.Label(popup, text="G = Green\nR = Red\nB = Blue\nY = Yellow\n\nTutorial:\nText appears on an orange background.\nExample: GRY\nYou need to press first Green secondly Red than Yellow.\nYou will notice that you need to remember the code\nBecause it disappears")
    label2.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()
Loading('60%', 'Help me method')

#Frames
canvas = tk.Frame(root, bg="green")
canvas.place(relwidth=1, relheight=1, relx=0, rely=0)

frame = tk.Frame(canvas, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

bluFrame = tk.Frame(frame, bg="gray")
bluFrame.place(relwidth=0.98, relheight=0.5, relx=0.01, rely=0.49)

colorFrame = tk.Frame(frame, bg="orange")
colorFrame.place(relwidth=0.3, relheight=0.3, relx=0.4, rely=0.1)

helpFrame =tk.Frame(frame, bg="black")
helpFrame.place(relwidth=0.1, relheight=0.1, relx=0.01, rely=0.01)
Loading('70%', 'Frames')

#Button frames
greenFrame =tk.Frame(bluFrame, bg="green")
greenFrame.place(relwidth=0.1, relheight=0.6, relx=0.1, rely=0.2)

redFrame=tk.Frame(bluFrame, bg="red")
redFrame.place(relwidth=0.1, relheight=0.6, relx=0.325, rely=0.2)

blueFrame=tk.Frame(bluFrame, bg="blue")
blueFrame.place(relwidth=0.1, relheight=0.6, relx=0.575, rely=0.2)

yellowFrame=tk.Frame(bluFrame, bg="yellow")
yellowFrame.place(relwidth=0.1, relheight=0.6, relx=0.8, rely=0.2)
Loading('84%', 'Button frames')

#Code label
txtLabel = tk.Label(colorFrame, wraplength=50, padx=1, pady=1, text="", bg="orange", fg="black")
txtLabel.pack(expand=True)
Loading('85%', 'Code label')

#Credits
CreLabel = tk.Label(canvas, text="Mikkoᶻ (Mikko Jyrkäs)", bg="green", fg="black")
CreLabel.pack(side='bottom')

#Buttons
clrButtonGreen = tk.Button(greenFrame, padx = 1000, pady = 1000, bg="green", command=g)
clrButtonGreen.pack()

clrButtonRed = tk.Button(redFrame, padx = 1000, pady = 1000, bg="red", command=r)
clrButtonRed.pack()

clrButtonBlue = tk.Button(blueFrame, padx = 1000, pady = 1000, bg="blue", command=b)
clrButtonBlue.pack()

clrButtonYellow = tk.Button(yellowFrame, padx = 1000, pady = 1000, bg="yellow", command=y)
clrButtonYellow.pack()

helpButton = tk.Button(helpFrame, text='Help', fg='red', padx = 1000, pady = 1000, bg="black", command=helpMe)
helpButton.pack()
Loading('99%', 'Buttons')

#Start
ultimate('start')
Loading('100%', 'Starting')
print('Up and Running')
root.mainloop()
