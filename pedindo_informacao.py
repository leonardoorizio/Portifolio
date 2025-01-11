import pyautogui
email = pyautogui.prompt(text='Digite seu e-mail:',
                         title='Informações obrigatórias')
print('Você digitou {}.'.format(email))
