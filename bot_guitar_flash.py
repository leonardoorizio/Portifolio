import pyautogui
import keyboard
from time import sleep

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(1274,898, (90,90,90)):
        pyautogui.press('a')
        sleep(0.5)
    if pyautogui.pixelMatchesColor(1350,898, (90,90,90)):
        pyautogui.press('s')
        sleep(0.5)
    if pyautogui.pixelMatchesColor(1421,897, (90,90,90)):
        pyautogui.press('j')
        sleep(0.5)
    if pyautogui.pixelMatchesColor(1499,902, (0,152,255)):
        pyautogui.press('k')
        sleep(0.05)