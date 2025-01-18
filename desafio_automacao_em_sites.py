import webbrowser
import pyautogui
from time import sleep

webbrowser.open('https://cursoautomacao.netlify.app/?_gl=1*1rnfeh3*_ga*MTkxMDI3NjIzMi4xNzM1NTA1ODg5*_ga_37GXT4VGQK*MTczNjgwODU0OC4yNi4xLjE3MzY4MDg1ODMuMC4wLjA.')
pyautogui.moveTo(1614, 325, duration=0.5)
sleep(1)
pyautogui.scroll(-1070)
pyautogui.click()
pyautogui.typewrite('Leonardo Gomes Orizio')
pyautogui.moveTo(1481, 360, duration=0.5)
pyautogui.click()
pyautogui.moveTo(1170, 261, duration=0.5)
pyautogui.click()
pyautogui.hotkey('ctrl', 'home')
sleep(1)
pyautogui.scroll(-2000)
pyautogui.moveTo(359, 273, duration=0.5)
pyautogui.click()
pyautogui.moveTo(588, 269, duration=0.5)
pyautogui.click()
sleep(1)
pyautogui.alert('Desafio concluído com sucesso!')
