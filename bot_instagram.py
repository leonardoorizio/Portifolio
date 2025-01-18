import webbrowser
import pyautogui
from time import sleep

webbrowser.open('https://www.instagram.com/')
sleep(5)
pyautogui.moveTo(116, 371, duration=0.5)
pyautogui.click()
sleep(2)
pyautogui.moveTo(178, 293, duration=0.5)
pyautogui.typewrite('nike')
pyautogui.hotkey('enter')
sleep(2)
pyautogui.moveTo(236, 354, duration=0.5)
pyautogui.click()
pyautogui.moveTo(703, 886, duration=0.5)
pyautogui.click()
sleep(2)
pyautogui.click()
sleep(2)
coracao = pyautogui.locateCenterOnScreen(
    'Captura de tela 2025-01-15 200244.png')
pyautogui.click(coracao)
