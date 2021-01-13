#!/bin/python3


# .......Basic Macro for Knight Online .......
# Functions
#-----------
# Slide vision bug macro(made for 1024*768 screen res)
# Assasin minor macro (Better fps better minor)
#-----------
# *Maybe you could be the new Domenico*


import pyautogui
import win32api,win32con
import keyboard
import time



def minor():
	x = 3
	while x <= 3:
		win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
		time.sleep(0.01)
		win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
		time.sleep(0.01)
		win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
		time.sleep(0.01)
		win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
		time.sleep(0.01)
		win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
		time.sleep(0.01)
		win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
		time.sleep(0.01)
		win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
		time.sleep(0.01)
		win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
		time.sleep(0.01)
		win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)

def slide():
	pyautogui.moveTo(512, 600)
	pyautogui.dragTo(512, 120, 0.5, button='left')
	keyboard.send('s')
	pyautogui.dragTo(512,600, 0.5, button='left')

time.sleep(0.2)
print("ok!...")
time.sleep(0.2)
print("""
CAPSLOCK for minor
SHIFT for slide
INSERT is the killswitch it will close the program
	""")

while keyboard.is_pressed('insert') == False: # insert is the killswitch
	while keyboard.is_pressed('capslock') == True: 
		minor()

	while keyboard.is_pressed('shift') == True:
		slide()

