# -*- coding: utf-8 -*-
"""
Created on Sat May  7 10:43:44 2022

@author: Ace
"""

from tkinter import *
import random
root = Tk()

root.title("Picnic_bag_list")
root.geometry("400x400")

label_display=Label(root, text="Listed_items:  " )
label_random_numbers=Label(root)




def Picnic():
    display=label_display
    
    list="Listed Items","Apples","Cookies","Picnic_Blanket", "Unbrella"
    label_display['text'] = str(list)
    ran1=random.randint(1,4)
    label_random_numbers["text"]="Put item no " + str(ran1) + " in bag"
    



btn = Button(root,text=" Random number", command= Picnic)  
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
label_random_numbers.place(relx=0.5,rely=0.6,anchor=CENTER)
label_display.place(relx=0.5,rely=0.4,anchor=CENTER)
root.mainloop()