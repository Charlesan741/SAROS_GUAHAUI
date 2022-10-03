# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 19:39:16 2022

@author: David Alejandro Charry Bonilla
@Team: SAROS G
"""

import tkinter as tk
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import  matplotlib.backends.backend_tkagg  
from matplotlib.figure import Figure


#functions
def close(window):
    window.destroy()
def savename(uName,campo):
    #change the name and close the popup
            Namepop.destroy()
            campo.config(text=uName)
def nameintro(window, campo):
        
        global Namepop
        #here we create the logic process to insert names.
        Namepop=tk.Toplevel(window)
        Namepop.title("STAR NAME")
        Namepop.geometry("400x100")
        Namepop.resizable(False,False)
        instruc1 = tk.Label(Namepop,text="Introduce your star name")
        instruc1.pack()
        userName=tk.Entry(Namepop,width=50)
        userName.pack()
        #uName=userName.get()
        bt=tk.Button(Namepop,text="SAVE",command=lambda: savename(userName.get(), campo))
        bt.place(x=100,y=50)
        
def savestar(window):
    #here we create the process of saving the user star
    global spop
    spop=tk.Toplevel(window)
    spop.title("SAVE STAR")
    spop.geometry("700x170")
    spop.resizable(False,False)
    tx=tk.Label(spop, text="Congratulations! you've created a star\n star saved"
                ,font=("Helvetica",24,"bold"))
    tx.pack()
    okBTN=tk.Button(spop, text="OK", font=("Helvetica",18) ,command=lambda:closeCreate(window))
    okBTN.config(width=40)
    okBTN.place(x=60,y=100)

def closeCreate(window):
    #here is the action of the exit option
    window.destroy()

def makeGraph(window):
    #Here we try to graph the light curve
    #NOTE: make position an size changes
    f= Figure(figsize=(5,5),dpi=100)
    a = f.add_subplot(111)
    x=np.arange(0,4*np.pi,0.1)
    y=np.sin(x)
    a.plot(x,y)
    canvas=FigureCanvasTkAgg(f,self)
    canvas.show()
    canvas.get_tk_widget().pack(side=window.BOTTOM, fill=tk.BOTH,expand=False)
    toolbar = NavegationToolbar2TkAgg(canvas,self)
    toolbar.update()
    canvas._tkcanvas.pack()
def openCreate():
    #Here we create a new window in order to show the design view
    #Create Window parameters
   
    CreateWindow=tk.Tk()
    CreateWindow.title("GUAHAÜI-CREATE")
    CreateWindow.geometry("1024x640")
    CreateWindow.resizable(False,False)
    #name space
    nombre=tk.Label(CreateWindow,text="INSERT NAME", font="Helvetica 36")
    nombre.place(x=350,y=30)
    #Back-home button
    HomeBTN= tk.Button(CreateWindow,text='MENU',command=CreateWindow.destroy)
    HomeBTN.place(x=50,y=20)

    #Name button
    NAME_BTN = tk.Button(CreateWindow, text="NAME", command=lambda: nameintro(CreateWindow, nombre))
    NAME_BTN.place(x=60,y=100)
    #play button
    PLAY_BTN=tk.Button(CreateWindow,text="PLAY")
    PLAY_BTN.place(x=50,y=600)
    #save star
    SAVE_BTN=tk.Button(CreateWindow, text="SAVE STAR", command=lambda: savestar(CreateWindow))
    SAVE_BTN.place(x=900,y=100)
    #create light curve graph
    #makeGraph(CreateWindow)
    
    #================Star variables settings===============
    VARSECTION =tk.Label(CreateWindow,text="STAR SETTINGS")
    VARSECTION.place(x=60,y=160)
    #=========MASS SETTINGS
    MASS_LBL=tk.Label(CreateWindow,text="MASS:")
    MASS_LBL.place(x=80,y=180)
    MASS_IN=tk.Entry(CreateWindow,width=10)
    MASS_IN.place(x=125,y=182)
    #=========AGE SETTINGS
    AGE_LBL=tk.Label(CreateWindow,text="STAR AGE:" )
    AGE_LBL.place(x=60,y=210)
    AGE_IN=tk.Entry(CreateWindow,width=10)
    AGE_IN.place(x=125,y=212)
    
    #=========SIZE SETTINGS
    SIZE_LBL=tk.Label(CreateWindow,text="SIZE: ")
    SIZE_LBL.place(x=90,y=240)
    SIZE_IN=tk.Entry(CreateWindow,width=10)
    SIZE_IN.place(x=125,y=242)
    
    #======================Heavenly bodies settings
    #=============EXOPLANET DOUBLE STARS
    LIST_LBL=tk.Label(CreateWindow,text="OPTION: ")
    LIST_LBL.place(x=70,y=270)
    VAR=tk.StringVar(CreateWindow)
    VAR.set('EXOPLANETS')
    options=['EXOPLANETS','DOUBLE STARS']
    choice=tk.OptionMenu(CreateWindow,VAR, *options)
    choice.config(width=20)
    choice.place(x=125,y=270)
    #====================settings
    RADIUS_LBL=tk.Label(CreateWindow,text="RADIUS: ")
    RADIUS_LBL.place(x=70,y=320)
    RADIUS_IN=tk.Entry(CreateWindow,width=10)
    RADIUS_IN.place(x=125,y=320)
    
    DISTANCE_LBL=tk.Label(CreateWindow,text="DISTANCE (au): ")
    DISTANCE_LBL.place(x=30,y=350)
    DISTANCE_IN=tk.Entry(CreateWindow,width=10)
    DISTANCE_IN.place(x=125,y=350)
    
    CreateWindow.mainloop()

   

    #CreateWindow.mainloop()
    
def openMap():
    #Here we create a new window in order to show the roadmap
    #Map window parameters
    MapWindow=tk.Toplevel()
    MapWindow.title("GUAHAÜI-MAP")
    MapWindow.geometry("1024x640")
    MapWindow.resizable(False,False)

    #Back-Home button
    HomeBTN= tk.Button(MapWindow,text='MENU',command=MapWindow.destroy)
    HomeBTN.place(x=100,y=30)

    
    # MapWindow.mainloop()
# Home Window Variables
GUI = tk.Tk()
GUI.title("GUAHAÜI - MENU")
# Home Window configuration parameters
GUI.geometry("1024x640")
GUI.resizable(False,False)
GUI.config(bg="#1D1514")
GUI.title("GUAHAÜI")
Title=tk.Label(GUI,text="GUAHAÜI", padx=500,pady=20)
Title.config(font=('Helvetica',36), fg="#FFFFFF",bg="#1D1514")
Title.pack()

#Home Menu
CreateBTN= tk.Button(GUI,text='Create Star',command=openCreate)
CreateBTN.config(font=('Helvetica',20))
CreateBTN.config(height=1,width=10,fg='#FFFFFF',bg='#1D1514')
CreateBTN.place(x=450,y=300)

MapBTN = tk.Button(GUI,text='Map', font='Helvetica 20', command=openMap)
MapBTN.config(height=1,width=10, fg='#FFFFFF',bg='#1D1514')
MapBTN.place(x=450,y=400)

ExitBTN = tk.Button(GUI, text='Exit',font='Helvetica 20', command=lambda: close(GUI))
ExitBTN.config(height=1,width=10, fg='#FFFFFF',bg='#1D1514')
ExitBTN.place(x=450,y=500)

# GUI loop function
GUI.mainloop()

