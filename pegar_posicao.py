import time
import pyautogui

time.sleep(5)
#descobrir posiçao do mouse no monitor
print(pyautogui.position())

#tamanho da rolangem pode ultilizar o press com home também
pyautogui.scroll(200)