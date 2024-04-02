'''
link do jogo:
https://guitarflash3.com/setlist/linkin-park/somewhere-i-belong
'''
import pyautogui
from time import sleep

pyautogui.click(1470,449, duration=1)
# botão verde
def verificar_botao_verde():
    if pyautogui.pixelMatchesColor(1312,792, (53,53,53)) == False:
        pyautogui.keyDown('a')
        pyautogui.keyUp('a')
        sleep(0.017)

# verificar o botão vermelho
def verificar_botao_vermelho():
    if pyautogui.pixelMatchesColor(1411,791, (53,53,53)) == False:
        pyautogui.keyDown('s')
        pyautogui.keyUp('s')
        sleep(0.017)

# botão amarelo
def verificar_botao_amarelo():
    if pyautogui.pixelMatchesColor(1505,791, (53,53,53)) == False:
        pyautogui.keyDown('j')
        pyautogui.keyUp('j')
        sleep(0.017)
 
# botão azul
def verificar_botao_azul():
    if pyautogui.pixelMatchesColor(1604,793, (53,53,53)) == False:
        pyautogui.keyDown('k')
        pyautogui.keyUp('k')
        sleep(0.017)

# botão laranja
def verificar_botao_laranja():
    if pyautogui.pixelMatchesColor(1701,788, (53,53,53)) == False:
        pyautogui.keyDown('l')
        pyautogui.keyUp('l')
        sleep(0.017)

while True:
    verificar_botao_verde()
    verificar_botao_vermelho()
    verificar_botao_amarelo()
    verificar_botao_azul()
    verificar_botao_laranja()
    if pyautogui.pixelMatchesColor(1506,546, (252,99,99)):
        break