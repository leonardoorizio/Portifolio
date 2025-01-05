import pyautogui
from time import sleep

pyautogui.moveTo(1766, 17, duration=2)
pyautogui.click()
pyautogui.moveTo(601, 596, duration=2)
for i in range(2000):
    # sleep(0.1)
    pyautogui.click()
