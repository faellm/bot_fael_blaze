import requests
from time import sleep
from data import *

while True:
    
    url = 'https://blaze.com/api/roulette_games/recent'
    response = requests.get(url)
    
    r = response.json()
    
    ray = []
    
    for x in range(len(r)):
        
        val = r[x]['color']
        
        if val == 1:
            val = 'Vermelho'
            
        if val == 2:
            val = 'Preto'
            
        if val == 0:
            val = 'Branco'
            
        ray.append(val)
    
    
    print(ray)
    sleep(8)
    
    

    def resultado(num):
        
        import telebot
        
        token = '5909325186:AAFL1prjhjD6SzaaYYBp_hIY3V2qKAiEMdc'
        chat_id = '-766902477'
        
        #bot = telebot.TeleBot(token)
        
        if num[0:4] == a2 :
            
            text = '''Green no Preto'''
            
            #bot.send_messege(chat_id, text)
            
            url_base = f'https://api.telegram.org/bpt{token}/sendMessege?chat_id={chat_id}&text={text}'
            result = requests.get(url_base)
            sleep(5)
            
            
        if num[0:3] == a1 :
            
            text = '''Entrada confirmado no Preto'''
            #bot.send_messege(chat_id, text)
            url_base = f'https://api.telegram.org/bpt{token}/sendMessege?chat_id={chat_id}&text={text}'
            result = requests.get(url_base)
            sleep(5)
            
        if num[0:3] == a3 :
            
            text = '''Entrada confirmado no Vermelho, mas com possibilidade de Branco'''
            #bot.send_messege(chat_id, text)
            url_base = f'https://api.telegram.org/bpt{token}/sendMessege?chat_id={chat_id}&text={text}'
            result = requests.get(url_base)
            sleep(5)
            
        if num[0:3] == a4 :
            
            text = 'possibilidade no Preto'
            #bot.send_messege(chat_id, text)
            url_base = f'https://api.telegram.org/bpt{token}/sendMessege?chat_id={chat_id}&text={text}'
            result = requests.get(url_base)
            sleep(5)
        
        elif num[0:3] != [a1] :
            
            text = ''' Aguarde . . .'''
            #bot.send_messege(chat_id, text)
            url_base = f'https://api.telegram.org/bpt{token}/sendMessege?chat_id={chat_id}&text={text}'
            result = requests.get(url_base)
            sleep(5)

    resultado(ray)
    sleep(5)