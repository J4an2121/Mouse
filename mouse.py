import pyautogui as botMouse  #Se usa para controlar el ratón (moverlo y hacer clic).
import webbrowser # Abre una página web en el navegador predeterminado.
import random
import time #Se usa para hacer pausas entre las acciones.


webbrowser.open("https://www.youtube.com/")
while True:

    print(botMouse.position())

    #x= random.randint(400,900)
    #y= random.randint(100,700)

    x=59

    y=337

    
    #botMouse.moveTo(x,y,0.5)
    time.sleep(4)
    botMouse.click()



