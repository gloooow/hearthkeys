import pyautogui
import pynput 

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
    "Z": [650, 1021],
    "Z": [650, 1000], "X": [710, 1000], "C": [765, 1000], "V": [808, 1000], "B": [868, 1000], "N": [903, 1000], "M": [967, 1000], ",": [1024, 1000], ".": [1075, 1000], "/": [1153, 1000],
    "A": [605, 600], "S": [725, 600], "D": [845, 600], "F": [965, 600], "G": [1085, 600], "H": [1205, 600], "J": [1325, 600], 
    "Q": [605, 420], "W": [725, 420], "E": [845, 420], "R": [965, 420], "T": [1085, 420], "Y": [1205, 420], "U": [1325, 420], 
    "P": [965, 825], "O": [960, 220],
}

lastKey = "F"
pressed = 0

def on_press(key):
    global lastKey, pressed
    print("You pressed {0}".format(key.char))
    pyautogui.moveTo(keys[key.char.upper()], duration=0.3)
    if(lastKey == key.char):
        print("You pressed {0} twice".format(key.char))
        pyautogui.click()
    lastKey = key.char
    

def on_release(key):
    # print("You released {0}".format(key.char))
    
    
    if key == pynput.keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = pynput.keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()