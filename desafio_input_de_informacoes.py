# Crie um programa que pede o usuário e senha, na sequência, copia e cola o usuário e senha dentro de um bloco de notas.

import pyautogui
import pyperclip

def copiar_e_colar(texto, x, y, duracao=0.2):
    pyperclip.copy(texto)
    pyautogui.moveTo(x, y, duration=duracao)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('Enter')

# Solicita o e-mail e a senha do usuário
email = pyautogui.prompt(text='Digite seu e-mail', title='Informações Obrigatórias')
senha = pyautogui.password(text='Digite sua senha', title='Informações Obrigatórias', mask='*')

# Coordenadas e duração para mover o cursor
x, y, duracao = 1135, 184, 0.2

# Copia e cola o e-mail e a senha
copiar_e_colar(email, x, y, duracao)
copiar_e_colar(senha, x, y, duracao)