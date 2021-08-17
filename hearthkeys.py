import tkinter
from pyautogui import *
from pynput import *
from tkinter import *
import sys

# L - End Turn
# K - Hero Power
# Z X C V B N M , . / - Hand Cards
# A S D F G H J - Player's Table
# Q W E R T Y U - Opponent's Table
# P - Player Hero
# O - Opponent Hero

keys = {
    "L": [1564, 520],
    "K": [1138, 848],
    "Z": [650, 1000], "X": [710, 1000], "C": [765, 1000], "V": [808, 1000], "B": [868, 1000], "N": [903, 1000], "M": [967, 1000], ",": [1024, 1000], ".": [1075, 1000], "/": [1153, 1000],
    "A": [605, 600], "S": [725, 600], "D": [845, 600], "F": [965, 600], "G": [1085, 600], "H": [1205, 600], "J": [1325, 600], 
    "Q": [605, 420], "W": [725, 420], "E": [845, 420], "R": [965, 420], "T": [1085, 420], "Y": [1205, 420], "U": [1325, 420], 
    "P": [965, 850], "O": [960, 220],
}

lastKey = "F"
class main_window:
    def __init__(self, master):
        self.master = master
        self.frame = tkinter.Frame(self.master)
        self.start_button = tkinter.Button(self.frame, text='start hearthkeys', command=self.new_window)
        self.close_button = tkinter.Button(self.frame, text='close hearthkeys', command=self.close_window)
        self.start_button.pack()
        self.close_button.pack()
        self.frame.pack()
    
    def new_window(self):
        self.newWindow = tkinter.Toplevel(self.master)
        self.app = hearthkeys_window(self.newWindow)

    def close_window(self):
        self.master.destroy()

class hearthkeys_window:
    def __init__(self, master):
        self.master = master

        width= master.winfo_screenwidth()
        height= master.winfo_screenheight()

        master.wm_attributes('-transparentcolor', 'red')

        self.frame = tkinter.Frame(self.master, width=width, height=height, background='red')
        for key in keys:
            self.label = tkinter.Label(self.frame, text=key, background='white', font=("Consolas", 20, "bold"), foreground='black')
            self.label.place(x=keys[key][0], y=keys[key][1]-height*0.07)

        self.frame.pack()

        master.attributes('-topmost', True)
        master.overrideredirect(1)

    def on_press(key):
        global lastKey

        if(key == keyboard.Key.esc): # close script if 'esc' is pressed
            print("Closing script...")
            sys.exit()
        try:
            moveTo(keys[key.char.upper()], duration=0.1) # if key is in keys, move the cursor
            print("You pressed {0}".format(key.char))

            if(lastKey == key.char): # verify if the key is pressed twice
                print('You pressed {0} twice'.format(key.char))
                click()
            lastKey = key.char
        except (KeyError, AttributeError) as errors: # if key is not in keys, show error
            print("no keybind " + str(errors))
        
    listener = keyboard.Listener(on_press=on_press) # start keyboard listener 
    listener.start()

def main(): 
    root = tkinter.Tk()
    app = main_window(root)
    root.mainloop()

if __name__ == '__main__':
    main()