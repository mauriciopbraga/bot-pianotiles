'''
instalar bibliotecas

pip install pywin32
pip install keyboard
pip install pyautogui
pip install opencv-python
'''

#libs
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#funcao
def clique(largura, altura):
    win32api.SetCursorPos((largura, altura))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

#loop
while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(581, 400)[0] == 0:
        clique(581, 400)
    if pyautogui.pixel(682, 400)[0] == 0:
        clique(682, 400)
    if pyautogui.pixel(770, 400)[0] == 0:
        clique(770, 400)
    if pyautogui.pixel(869, 400)[0] == 0:
        clique(869, 400)