import pyautogui
import pyperclip


def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl', 'v')


pyautogui.moveTo(1397, 402, duration=0.2)
pyautogui.click()
escrever_frase('Automação é incrivel!!!')

# Caso não contenha caracteres especiais, podemos utilizar a função typewrite
