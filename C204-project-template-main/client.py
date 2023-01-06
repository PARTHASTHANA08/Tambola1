import socket
from tkinter import *
from threading import Thread 
import random
from PIL import ImageTk, Image

def setup():
    global SERVER , PORT , IP_ADDRESS
    PORT = 6000
    IP_ADDRESS = "127.0.0.1"

    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS,PORT))
    thread = Thread(target=recievedMsg)
    thread.start()

def askName():
    global PlayerName
    global NameEntry
    global NameWindow
    global Canvas1 

    NameWindow = Tk()
    NameWindow.title("Tambola Fun Game")
    NameWindow.geometry("800x600")
    screenWidth = NameWindow.winfo_screenwidth()
    screenHeight = NameWindow.winfo_screenheight()
    bg = ImageTk.photoImage(file = "./assets/background.png")
    Canvas1 = Canvas(NameWindow,width=500,height=500)
    Canvas1.pack(fill="both",exand=True)
    Canvas1.create_image(0,0, image = bg , anchor="nw")
    Canvas1.create_Text(screenWidth/4.5 ,screenHeight/8,text="Enter Name",font=("Chalkboard SE",60),fill="black")
    NameEntry = Entry(NameWindow, justify="center",font=("Chalkboard SE",30),width=15,bg="white")
    NameEntry.place(x = screenWidth/7,y = screenHeight/5.5)
    button = Button(NameWindow, text="Save",font=("Chalkboard SE",30),width=11,command=saveName,height=2,bg="#80deea",bd=3)
    button.place(x = screenWidth/6 , y = screenHeight/4)
    NameWindow.resizable(True,True)
    NameWindow.mainloop()

def saveName():
    global SERVER
    global PlayerName
    global NameWindow 
    global NameEntry

    PlayerName = NameEntry.get()
    NameEntry.delete(0,END)
    NameWindow.destroy()
    SERVER.send(PlayerName.encode())
    




