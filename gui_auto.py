from auto import press_user_defined_key, countdown, main
from constants import HEIGHT,WIDTH,BLACK,GRAY,WHITE,RED,YELLOW,GREEN,PURPLE,BLUE,TEAL
from tkinter import *
from tkinter import ttk
import pyautogui
import pydirectinput
import time


class AutoClickerGUI:
    def __init__(self, master) -> None:
        self.master = master
        master.title("FiveM Auto Clicker GUI")
        
        self.label = Label(master, text="FiveM Auto Clicker GUI")
        self.label.pack()
        
        self.one_meth_button = Button(master, text="One Meth Bag", command=self.single_meth_bag)
        self.one_meth_button.pack()
        
        self.two_meth_button = Button(master, text="Two Meth Bags", command=self.two_meth_bags)
        self.two_meth_button.pack()
        
        self.full_meth_button = Button(master, text="Until Full (CMD)", command=self.meth_until_full)
        self.full_meth_button.pack()
        
        self.input_button = Button(master, text="Input in CMD Prompt", command=main)
        self.input_button.pack()
        
        self.button2 = Button(master, text="Quit", command=self.quit)
        self.button2.pack()
        
        
    def autoclick(self, key, time_between, amount):
        x = 0
        while x < amount:
            print("Starting in 5 seconds")
            time.sleep(5)
            pydirectinput.press(key)
            time.sleep(time_between)
            print(f"{key} has been pressed {x} times.")
            x += 1

    
    
    def single_meth_bag(self):
        self.autoclick("e", 16, 30)
    
    
    def two_meth_bags(self):
        self.autoclick("e", 16, 60)
    
    
    def meth_until_full(self):
        weight = input("How much can you carry? Round down to the nearest Kg (if you have 16.5kg left, we can fill 16kg).")
        self.autoclick("e", 16, (.5*weight))


    def quit(self):
        quit()
    
    
# Run the window
root = Tk()
auto_clicker_gui = AutoClickerGUI(root)
root.mainloop()