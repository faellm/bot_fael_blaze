from main import *
from time import sleep
from data import *

token = '5641112414:AAFEWgLvhz9k9ceyIrgb185hR7wbYm_VNQQ'
chat_id = '5219044660'

def resultado(num):
        
    if num[0:4] == a2 :
            
        text = '''Green no Preto'''
        
        url_base = f'https://api.telegram.org/bpt{token}/sendMessege?chat_id={chat_id}&text={text}'
        result = requests.get(url_base)
        sleep(5)
            
            
        if num[0:3] == a1 :
            
            text = '''Entrada confirmado no Preto'''
            print(text)
            url_base = f'https://api.telegram.org/bpt{token}/sendMessege?chat_id={chat_id}&text={text}'
            result = requests.get(url_base)
            sleep(5)
            
        if num[0:3] == a3 :
            
            text = '''Entrada confirmado no Vermelho, mas com possibilidade de Branco'''
            print(text)
            url_base = f'https://api.telegram.org/bpt{token}/sendMessege?chat_id={chat_id}&text={text}'
            result = requests.get(url_base)
            sleep(5)
            
        if num[0:3] == a4 :
            
            text = ''' possibilidade no Preto'''
            print(text)
            url_base = f'https://api.telegram.org/bpt{token}/sendMessege?chat_id={chat_id}&text={text}'
            result = requests.get(url_base)
            sleep(5)
        
        if num[0:3] != [a1] :
            
            print('aguarde...')

resultado(ray)