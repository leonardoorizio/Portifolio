import pyautogui

senha = pyautogui.password(text='digite sua senha:',
                           title='dados de login', mask='*')
print(senha)
