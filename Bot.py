import webbrowser,pyautogui

from time import sleep

webbrowser.open('http://web.whatsapp.com/send?phone=+57 numero_whatsapp')

sleep(15)

with open('cancion.txt','r') as file:
    for line in file:
        pyautogui.typewrite(line)
        pyautogui.press("enter")
