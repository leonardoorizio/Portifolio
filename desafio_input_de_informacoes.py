# Crie um programa que pede o usuário e senha, na sequência, copia e cola o usuário e senha dentro de um bloco de notas.

import pyautogui
import pyperclip

email = pyautogui.prompt(text='Digite seu e-mail',
                         title='Informações Obrigatórias')
senha = pyautogui.password(text='Digite sua senha',
                           title='Informações Obrigatórias', mask='*')
pyperclip.copy(email)
pyautogui.moveTo(1135, 184, duration=0.2)
pyautogui.click()
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('Enter')
pyperclip.copy(senha)
pyautogui.moveTo(1135, 184, duration=0.2)
pyautogui.click()
pyautogui.hotkey('ctrl', 'v')
