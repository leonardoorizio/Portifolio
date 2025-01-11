import pyautogui

resposta = pyautogui.confirm(text='Continuar rodando nossa automação?',
                             title='Confirmação', buttons=['sim', 'não', 'cancelar'])
if resposta == 'sim':
    print('a')
elif resposta == 'não':
    print('b')
else:
    print('c')
