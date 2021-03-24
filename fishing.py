from pyautogui import *
import pyautogui
import time
import keyboard
import admin
import win32api, win32con
import ctypes, sys
from datetime import datetime

# Target do peixe X:  971 Y:   44 RGB: (145,  59,  42)
#                 X:  973 Y:   58 RGB: ( 38, 112, 190)

CONFIDENCE=0.4
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    print("Aperte INSERT para <iniciar> e segure END para <fechar>")
    keyboard.wait('ins')
    while keyboard.is_pressed('end') == False:
        now = datetime.now().time()
        if pyautogui.locateOnScreen('up.png', region=(700, 0, 500, 200), confidence=CONFIDENCE) != None:
            keyboard.press_and_release('up')
            print(now, "->> SKILL seta pra CIMA")
            time.sleep(2.5)
        elif pyautogui.locateOnScreen('left.png', region=(700, 0, 500, 200), confidence=CONFIDENCE) != None:
            keyboard.press_and_release('left')
            print(now, "->> SKILL seta pra ESQUERDA")
            time.sleep(2.5)
        elif pyautogui.locateOnScreen('right.png', region=(700, 0, 500, 200), confidence=CONFIDENCE) != None:
            keyboard.press_and_release('right')
            print(now, "->> SKILL seta pra DIREITA")
            time.sleep(2.5)
        elif pyautogui.locateOnScreen('pull.png', region=(700, 0, 500, 200), confidence=CONFIDENCE) != None:
            keyboard.press_and_release('down')
            print(now, "->> SKILL PUXAR peixe")
            time.sleep(2.5)
        elif pyautogui.locateOnScreen('release.png', region=(700, 0, 500, 200), confidence=CONFIDENCE) != None:
            keyboard.press_and_release('home')
            print(now, "->> SKILL SOLTAR peixe")
            time.sleep(2.5)
        elif pyautogui.locateOnScreen('target.png', region=(700, 0, 500, 200), confidence=CONFIDENCE) != None:
            print(now, "->> AGUARDANDO SKILL")
            time.sleep(0.01)
        else:
            print(now, "->> Aguardando target do peixe")
            time.sleep(0.01)                 
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
