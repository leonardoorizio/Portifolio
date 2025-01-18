import webbrowser
import pyautogui
from time import sleep

telefones = [5548984730135, 5548984251907]

for telefone in telefones:
    webbrowser.open('https://api.whatsapp.com/send?phone={}'.format(telefone))
    sleep(5)
    pyautogui.click(947, 459, duration=1)
    sleep(5)
    pyautogui.moveTo(948, 551, duration=1)
    pyautogui.click()
    sleep(5)
    pyautogui.moveTo(848, 964, duration=1)
    pyautogui.click()
    pyautogui.typewrite('Gostaria de participar do nosso evento?')
    sleep(5)
    pyautogui.press('enter')
    sleep(10)
