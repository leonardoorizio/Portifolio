import pyautogui
import pyperclip


def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('crtl', 'v')


pyautogui.moveTo()
pyautogui.click()
escrever_frase('Olá, bom dia')
pyautogui.click()
